#include <bits/stdc++.h>
using namespace std;

#ifdef ILIKEGENTOO
#   define Eo(x) { cerr << #x << " = " << (x) << endl; }
#   define E(x) { cerr << #x << " = " << (x) << "   "; }
#   define FREOPEN(x)
#else
#   define Eo(x) {}
#   define E(x) {}
#   define FREOPEN(x) (void)freopen(x ".in", "r", stdin);(void)freopen(x ".out", "w", stdout);
#endif
#define EO(x) Eo(x)
#define Sz(x) (int((x).size()))
#define All(x) (x).begin(),(x).end()

template<class A, class B> ostream &operator<<(ostream &os, const pair<A, B>& p) { return os << '(' << p.first << ", " << p.second << ')'; }

template<class C> void operator<<(vector<C> &v, const C &x){v.push_back(x);}
template<class D> void operator>>(vector<D> &v, D &x){assert(!v.empty()); x=v.back(); v.pop_back();}
template<class E> void operator<<(set<E> &v, const E &x){v.insert(x);}

typedef long double flt;
typedef long long int64;
typedef unsigned long long uint64;
typedef pair<int, int> pii;

const int inf = 0x3f3f3f3f;
const int64 inf64 = 0x3f3f3f3f3f3f3f3fLL;
const flt eps = 1e-8;
const flt pi = acos(-1.0);
const int dir[4][2] = { {0, 1}, {1, 0}, {0, -1}, {-1, 0} };

random_device rdev; mt19937 rmt(rdev()); uniform_int_distribution<> rnd(0, 0x7fffffff);
inline int mrand(int mod = 0x7fffffff) { return rnd(rmt) % mod; }

const int maxn = 111;
flt r[maxn];
flt x[maxn];
flt reqv, reqx; 
int n;

flt solve() {
    flt res = -1;
    // 1
    for (int i = 0; i < n; ++i) {
        if (abs(reqx - x[i]) > eps) continue;
        flt t = reqv / r[i];
        if (res < 0 || t < res) res = t;
    }
    // 2
    const flt right = reqv * reqx;
    for (int i = 0; i < n; ++i) for (int j = 0; j < n; ++j) if (i != j) {
        //assert(abs(x[i] - x[j]) > eps);
        if (abs(x[i] - x[j]) > eps) {
            flt beta = (right - x[i] * reqv) / (r[j] * (x[j] - x[i]));
            if (beta < 0) continue;
            flt alpha = (reqv - beta * r[j]) / r[i];
            if (alpha < 0) continue;
            flt cur = max(beta, alpha);

            if (res < 0 || cur < res) res = cur;
        } else if (abs(x[i] - reqx) < eps) {
            flt sumr = r[i] + r[j];
            flt t = reqv / sumr;
            if (res < 0 || t < res) res = t;
        }
    }
    
    return res;
}

int main() {
    //ios_base::sync_with_stdio(false); cin.tie(0);

    int ts; cin >> ts;
    for (int test = 1; test <= ts; ++test) {
        cin >> n;
        cin >> reqv >> reqx;
        for (int i = 0; i < n; ++i) {
            cin >> r[i] >> x[i];
        }
        flt res = solve();
        cout << "Case #" << test << ": ";
        if (res < 0)
            cout << "IMPOSSIBLE";
        else
            printf("%.10lf", double(res));
        cout << endl;
    }

    return 0;
}
