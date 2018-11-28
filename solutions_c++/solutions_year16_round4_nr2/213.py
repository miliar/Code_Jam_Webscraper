#define FNAME ""

#include <bits/stdc++.h>

#define hash padjf9srpi
#define y0 sdkfaslhagaklsldk
#define y1 aasdfasdfasdf
#define yn askfhwqriuperikldjk
#define j1 assdgsdgasghsf
#define tm sdfjahlfasfh
#define lr asgasgash
#define pb push_back
#define mp make_pair
#define forn(i, n) for (int i = 0; i < (n); i++)
#define fornr(i, n) for (int i = (n) - 1; i >= 0; i--)
#define forab(i, a, b) for (int i = (a); i < (b); i++)
#define gcd __gcd
#define all(a) (a).begin(), (a).end()
 
#ifdef _WIN32
    #define I64 "%I64d"
#else
    #define I64 "%lld"
#endif

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef pair <int, int> pii;
typedef vector <int> vi;

template <class T> T sqr(const T &a) {return a * a;}

const int MAXN = 205;

int T;
double a[MAXN], b[MAXN], d[MAXN][MAXN];

int main() {
#ifdef LOCAL
    freopen(FNAME".in", "r", stdin);
    freopen(FNAME".out", "w", stdout);
#endif
    scanf("%d", &T);
        
    forn(qqq, T) {
        int n, k;
        scanf("%d%d", &n, &k);
        forn(i, n)
            scanf("%lf", &a[i]);
        sort(a, a + n);
        double ans = -1;
        forn(pref, k + 1) {
            forn(i, pref)
                b[i] = a[i];                    
            forn(i, k - pref)
                b[i + pref] = a[n - i - 1];
            forn(i, n + 1) {
                forn(j, n + 1) {
                        d[i][j] = 0;
                }
            }
            d[0][0] = 1;
            forn(i, k) {
                forn(j, k) {
                    d[i + 1][j + 1] += d[i][j] * b[i];
                    d[i + 1][j] += d[i][j] * (1 - b[i]);
                }
            } 
            if (d[k][k / 2] > ans)
                ans = d[k][k / 2];
        }
        printf("Case #%d: %.10f\n", qqq + 1, ans);
    }
}

