#include <bits/stdc++.h>

#define all(x) (x).begin(), (x).end()

#ifdef KAZAR
    #define eprintf(...) fprintf(stderr,__VA_ARGS__)
#else
    #define eprintf(...) 0
#endif

using namespace std;

template<class T> inline void umax(T &a,T b){if(a<b) a = b ; }
template<class T> inline void umin(T &a,T b){if(a>b) a = b ; }
template<class T> inline T abs(T a){return a>0 ? a : -a;}
template<class T> inline T gcd(T a,T b){return __gcd(a, b);}
template<class T> inline T lcm(T a,T b){return a/gcd(a,b)*b;}

typedef long long ll;
typedef pair<int, int> ii;

const int inf = 1e9 + 143;
const ll longinf = 1e18 + 143;

inline int read(){int x;scanf(" %d",&x);return x;}

const int N = 111;

const double eps = 1e-15;

double r[N], t[N];

bool zero(double x){
    return abs(x) < eps;
}

bool eq(double x,double y){
    return zero(x - y);
}

double calc(double r0, double t0, double r1, double t1, double v, double x){
    if(t0 > t1){
        swap(t0, t1);
        swap(r0, r1);
    }
    if(x < t0 || x > t1)
        return longinf;
    double ans = longinf;
    if(eq(t[0], x)){
        umin(ans, v / r[0]);
    }
    if(eq(t[1], x)){
        umin(ans, v / r[1]);
    }
    if(eq(t[0], x) && eq(t[1], x)){
        return v / (r0 + r1);
    }
    double l = 0, r = v;
    for(int i = 0; i < 100; i++){
        double m = (l + r) / 2;
        if(m * t0 + (v - m) * t1 > v * x)
            l = m;
        else
            r = m;
    }
    umin(ans, max(l / r0, (v - l) / r1));
    return ans;
}

void solve(){
    int n = read();
    double v, x;
    scanf(" %lf %lf", &v, &x);
    for(int i = 0; i < n; i++){
        scanf(" %lf %lf", r + i, t + i);
    }
    double ans;
    if(n == 2){
        ans = calc(r[0], t[0], r[1], t[1], v, x);
    }else{
        if(eq(t[0], x)){
            ans = v / r[0];
        }else{
            ans = longinf;
        }
    }
    if(ans > 1e15){
        puts("IMPOSSIBLE");
    }else{
        printf("%.10f\n", ans);
    }
}

int main(){

#ifdef KAZAR
    freopen("f.input","r",stdin);
    freopen("f.output","w",stdout);
    freopen("error","w",stderr);
#endif

    int t = read();

    for(int i = 1; i <= t; i++){
        printf("Case #%d: ", i);
        solve();
        eprintf("test = %d\n", i);
    }

    return 0;
}
