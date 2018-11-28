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

typedef double flt;
typedef long long int64;
typedef unsigned long long uint64;
typedef pair<int, int> pii;

const int inf = 0x3f3f3f3f;
const int64 inf64 = 0x3f3f3f3f3f3f3f3fLL;
const flt eps = 1e-8;
const flt pi = acos(-1.0);
const int dir[4][2] = { {0, 1}, {1, 0}, {0, -1}, {-1, 0} };

constexpr inline int bit(int t) { return 1 << t; }

random_device rdev; mt19937 rmt(rdev()); uniform_int_distribution<> rnd(0, 0x7fffffff);
inline int mrand(int mod = 0x7fffffff) { return rnd(rmt) % mod; }

const int maxn = 202;

flt dp[maxn][maxn][maxn];
flt p[maxn];

flt ndp[maxn], pdp[maxn];

void updmax(flt& a, const flt& b) {
    a = max(a, b);
}

int main() {
    // FREOPEN("b");
    ios_base::sync_with_stdio(false); cin.tie(0);

    int tests; cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        int n, k; cin >> n >> k;
        for (int i = 0; i < n; ++i) cin >> p[i];

#if 0
        memset(dp, 0, sizeof(dp));

        dp[0][0][0] = 1.0;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                for (int d = 0; d < n; ++d)
                    if (dp[i][j][d] > eps) {
                        E(i); E(j);  E(d); Eo(dp[i][j][d]);

                        updmax(dp[i + 1][j][d], dp[i][j][d]);

                        updmax(dp[i + 1][j + 1][d], (1.0 - p[i]) * dp[i][j][d]);
                        updmax(dp[i + 1][j + 1][d + 1], p[i] * dp[i][j][d]);
                    }


        flt maxProb = 0.0;
        Eo(dp[n][k][3]);
#endif
        flt best = 0.0;
        for (int i = 0; i < bit(n); ++i) if (__builtin_popcount(i) == k) {
            memset(pdp, 0, sizeof(pdp));
            pdp[0] = 1.0;
            for (int j = 0; j < n; ++j) if (i & bit(j)) {
                memset(ndp, 0, sizeof(ndp));
                for (int d = 0; d < n; ++d) {
                    ndp[d] += pdp[d] * (1.0 - p[j]);
                    ndp[d + 1] += pdp[d] * p[j];
                }
                memcpy(pdp, ndp, sizeof(pdp));
            }

            best = max(best, pdp[k/2]);
        }

        //cout << "Case #" << test << ": ";
        printf("Case #%d: %.10lf\n", test, double(best));
    }

    return 0;
}
