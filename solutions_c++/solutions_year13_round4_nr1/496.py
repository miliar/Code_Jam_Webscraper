#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int MAXN = 1005;
const long long MOD = 1000002013ll;

struct Node{
    long long x, p;
    bool operator < (const Node &a) const{
        return x < a.x;
    }
}c[MAXN], d[MAXN], _v[MAXN];

bool cmp(Node a, Node b){
    return a.x > b.x;
}

struct heap{
    int size;
    void push(Node a){
        _v[size++]=a;
        if(size>1)push_heap(_v,_v+size,cmp);
    }
    void pop(){
        pop_heap(_v,_v+size,cmp);
        --size;
    }
    Node top(){return _v[0];}
    void init(){size=0;}
}hp;

int m;
long long n, ans;
inline long long f(long long x){
    return ((n + (n - x + 1)) * x / 2) % MOD;
}

void init(){
    ans = 0;
    scanf("%lld%d", &n, &m);
    hp.init();
    for (int i = 0; i < m; i++){
        scanf("%lld%lld%lld", &c[i].x, &d[i].x, &c[i].p);
        d[i].p = c[i].p;
        ans += f(d[i].x - c[i].x) * c[i].p;
    }
    ans %= MOD;
}

void work(){
    sort(d, d + m);
    sort(c, c + m);
    int j = m - 1;
    for (int i = m - 1; i >= 0; i--){
        while (j >= 0 && d[j].x >= c[i].x){
            hp.push(d[j]);
            j--;
        }
        while (c[i].p){
            int pp = min(c[i].p, _v[0].p);
            c[i].p -= pp;
            _v[0].p -= pp;
            ans += MOD - (f(_v[0].x - c[i].x) * pp) % MOD;
            ans %= MOD;
            if (_v[0].p == 0) hp.pop();
        }
    }
}

int main(){
#ifdef LATTE
//    freopen("a.in", "r", stdin);
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
//    freopen("A-large.in", "r", stdin);
//    freopen("out.txt", "w", stdout);
#endif
    int T, t = 1;
    scanf("%d", &T);
    while (T--){
        init();
        work();
        printf("Case #%d: %lld\n", t++, ans);
    }
    return 0;
}
