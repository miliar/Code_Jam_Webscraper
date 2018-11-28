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

struct Checker {
    int n, mask;
    bool used[4];
    vector<int> order;

    Checker() {
        memset(used, 0, sizeof(used));
    }

    bool go(int num)  {
        if (num == n)
            return true;
        int im = order[num];

        int cango = 0, allok = 0;
        for (int i = 0; i < n; ++i)
            if (!used[i] && (mask & bit(im * n + i))) {
                ++cango;
                used[i]  = true;
                if (go(num + 1))
                    ++allok;
                used[i] = false;
            }
        return cango > 0 && cango == allok;
    }

    bool checkMask(int nn, int mm) {
        n = nn;
        mask = mm;
        order = vector<int>(n, 0);
        iota(All(order), 0);
        do {
            if (!go(0))
                return false;
        } while (next_permutation(All(order)));
        return true;
    }
};

int main() {
    // FREOPEN("d");
    ios_base::sync_with_stdio(false); cin.tie(0);

    int tests; cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        int n; cin >> n;
        int mask = 0;
        for (int i = 0; i < n; ++i) {
            string s; cin >> s;
            for (int j = 0; j < n; ++j)
                if (s[j] == '1')
                    mask |= bit(i * n + j);
        }
        //Eo(mask);

        Checker checker;

        int best = inf;
        for (int i = 0; i < bit(n * n); ++i) {
            if ((i & mask) == mask && checker.checkMask(n, i)) {
                int cnt = i ^ mask;
                int cost = __builtin_popcount(cnt);
                //E(i); E(cnt); Eo(cost);
                best = min(best, cost);
            }
        }

        cout << "Case #" << test << ": " << best << endl;
    }

    return 0;
}
