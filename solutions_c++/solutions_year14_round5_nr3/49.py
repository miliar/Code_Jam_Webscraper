#include <bits/stdc++.h>
#include <ext/rope>
#pragma GCC optimize ("O3")
#define clr(x) memset((x), 0, sizeof(x))
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define For(i, st, en) for(int i=(st); i<=(int)(en); i++)
#define Ford(i, st, en) for(int i=(st); i>=(int)(en); i--)
#define forn(i, n) for(int i=0; i<(int)(n); i++)
#define ford(i, n) for(int i=(n)-1; i>=0; i--)
#define fori(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); it++)
#define in(x) int (x); input((x));
#define x first
#define y second
#define less(a,b) ((a) < (b) - EPS)
#define more(a,b) ((a) > (b) + EPS)
#define eq(a,b) (fabs((a) - (b)) < EPS)
#define remax(a, b) ((a) = (b) > (a) ? (b) : (a))
#define remin(a, b) ((a) = (b) < (a) ? (b) : (a))

using namespace std;

using namespace __gnu_cxx;

template <typename T>
T gcd(T a, T b) {
    while (b > 0) {
        a %= b;
        swap(a, b);
    }
    return a;
}
typedef long double ld; template <class _T> inline _T sqr(const _T& x) {return x * x;} template <class _T> inline string tostr(const _T& a) {ostringstream os(""); os << a; return os.str();} const ld PI = 3.1415926535897932384626433832795L; const double EPS = 1e-9; char TEMPORARY_CHAR; typedef long long ll; typedef unsigned long long ull; typedef set < int > SI; typedef vector < int > VI; typedef vector < vector < int > > VVI; typedef map < string, int > MSI; typedef pair < int, int > PII; const int INF = 1e9; inline void input(int &a) {a = 0; while (((TEMPORARY_CHAR = getchar()) > '9' || TEMPORARY_CHAR < '0') && (TEMPORARY_CHAR != '-')){} char neg = 0; if (TEMPORARY_CHAR == '-') {neg = 1; TEMPORARY_CHAR = getchar();} while (TEMPORARY_CHAR <= '9' && TEMPORARY_CHAR >= '0') {a = 10 * a + TEMPORARY_CHAR - '0'; TEMPORARY_CHAR = getchar();} if (neg) a = -a;} inline void out(long long a) {if (!a) putchar('0'); if (a < 0) {putchar('-'); a = -a;} char s[20]; int i; for(i = 0; a; ++i) {s[i] = '0' + a % 10; a /= 10;} ford(j, i) putchar(s[j]);} inline int nxt() {in(ret); return ret;}




int main()
{
#ifdef LOCAL
    freopen ("C1.in", "r", stdin);
    //freopen ("in.txt", "r", stdin);
    freopen ("C1.out", "w", stdout);
#else
    //freopen("trie.in", "r", stdin);
    //freopen("trie.out", "w", stdout);
#endif

    in(t);
    int counter = 0;
    while (t--) {
        ++counter;
        in(n);
        int b[n];

        int type[n];
        int who[n];

        vector <int> people;

        for (int i = 0; i < n; ++i) {
            string t;
            cin >> t;
            if (t == "E") {
                type[i] = 0;
            } else {
                type[i] = 1;
            }
            who[i] = nxt();
            if (who[i] > 0) {
                people.push_back(who[i]);
            }
        }
        sort(all(people));
        people.resize(unique(all(people)) - people.begin());
        for (int i = 0; i < n; ++i) {
            if (who[i] > 0) {
                who[i] = lower_bound(all(people), who[i]) - people.begin();
            } else {
                who[i] = -1;
            }
        }

        char A[1 << (n + 1)];
        char B[1 << (n + 1)];

        char * d1 = A, * d2 = B;

        memset(d1, 1, sizeof(char) * (1 << (n + 1)));

        for (int i = 0; i < n; ++i) {
            memset(d2, 0, sizeof(char) * (1 << (n + 1)));
            if (type[i] == 0) {
                for (int j = 0; j < (1 << (n + 1)); ++j) {
                    if (d1[j]) {
                        if (who[i] != -1) {
                            if (!((j >> who[i]) & 1)) {
                                d2[j ^ (1 << who[i])] = 1;
                            }
                        } else {
                            for (int k = 0; k < (n + 1); ++k) {
                                if (!((j >> k) & 1)) {
                                    d2[j ^ (1 << k)] = 1;
                                }
                            }
                        }
                    }
                }
            } else {
                for (int j = 0; j < (1 << (n + 1)); ++j) {
                    if (d1[j]) {
                        if (who[i] != -1) {
                            if (((j >> who[i]) & 1)) {
                                d2[j ^ (1 << who[i])] = 1;
                            }
                        } else {
                            for (int k = 0; k < (n + 1); ++k) {
                                if (((j >> k) & 1)) {
                                    d2[j ^ (1 << k)] = 1;
                                }
                            }
                        }
                    }
                }
            }
            swap(d1, d2);
        }

        int ans = 1000;

        for (int i = 0; i < (1 << (n + 1)); ++i) {
            if (d1[i]) {
                ans = min(ans, __builtin_popcount(i));
            }
        }
        if (ans != 1000) {
            printf("Case #%d: %d\n", counter, ans);
        } else {
            printf("Case #%d: CRIME TIME\n", counter);
        }
    }
    return 0;
}
