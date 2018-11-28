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

vector<int> primes;

vector<int> check(const string& s) {
    vector<int> res;

    for (int i = 2; i <= 10; ++i) {
        const int64 val = stoll(s, 0, i);
        bool ok = false;
        for (int j : primes)
            if (val % j == 0) {
                if (val == j) continue;
                res.push_back(j);
                ok = true;
                break;
            }
        if (!ok)
            return vector<int>();
    }

    return res;
}

int main() {
    primes.push_back(2);
    for (int j = 3; j < int(1e8); j += 2) {
        if (!(j&0xffffe)) { E(j); Eo(flt(j)/1e8); }
        bool ok = true;
        for (int ii = 0; ii < Sz(primes); ++ii) {
            const int64 i = primes[ii];
            if (i * i > j) break;
            if (j % i == 0) {
                ok = false;
                break;
            }
        }
        if (ok)
            primes.push_back(j);
    }
    Eo("primes");

    int t, n, j; cin >> t >> n >> j;

    puts("Case #1:");
    for (int i = bit(15); i < bit(16); ++i) {
        if (!(i&1)) continue;

        int num = i;
        string s = "";
        while (num) {
            s += '0' + num % 2;
            num /= 2;
        }
        reverse(All(s));

        vector<int> res = check(s);
        if (res.empty()) continue;

        cout << s;
        for (int jj : res) cout << ' ' << jj;
        cout << endl;

        --j;
        if (!j) break;
    }

    return 0;
}
