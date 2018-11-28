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
    freopen ("A2.in", "r", stdin);
    freopen ("A2.out", "w", stdout);
#else
    //freopen("trie.in", "r", stdin);
    //freopen("trie.out", "w", stdout);
#endif

    in(t);
    int counter = 0;
    while (t--) {
        ++counter;
        in(n); in(p); in(q); in(r); in(ss);
        vector <long long> a(n);
        vector <long long> s(n + 1);
        s[0] = 0;
        for (int i = 0; i < n; ++i) {
            a[i] = ((long long)i * p + q) % r + ss;
            s[i + 1] = a[i];
            s[i + 1] += s[i];
        }
        long double best = 0;
        for (int i = 0; i < n; ++i) {
            long long rem = s[n] - s[i + 1];
            long long need = (s[i + 1]) / 2;
            int pos = lower_bound(s.begin(), s.begin() + i + 1, need) - s.begin();
            for (int j = max(1, pos - 5); j <= min(pos + 5, i + 1); ++j) {
                long long aa = s[j - 1];
                long long bb = s[n] - rem - aa;
                long long cc = rem;
                if (aa > bb) {
                    swap(aa, bb);
                }
                if (bb > cc) {
                    swap(bb, cc);
                }
                if (aa > bb) {
                    swap(aa, bb);
                }
                best = max(best, (long double)(aa + bb) / s[n]);
            }
        }
        printf("Case #%d: %.10Lf\n", counter, best);
    }
    return 0;
}
