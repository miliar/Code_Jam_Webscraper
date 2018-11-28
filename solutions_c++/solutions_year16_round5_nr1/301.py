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

const int MAXN = 2e4 + 100;
short d[MAXN][MAXN][2];
int T;
char s[MAXN];

int main()
{
#ifdef LOCAL
    freopen(FNAME".in", "r", stdin);
    freopen(FNAME".out", "w", stdout);
#endif
    scanf("%d ", &T);
    forn(qqq, T) {
        gets(s);
        int n = strlen(s);
        assert(n % 2 == 0);
        forn(i,n + 10)
            forn(j, n + 10)
                d[i][j][0] = -1e9, d[i][j][1] = 0;
        forn(i, n + 10)
            d[i][i][0] = 0;
        fornr(i, n) {
            forab(j, i + 1, n + 1) {
                d[i][j][1] = max(d[i + 1][j][1], d[i + 1][j][0]);                
                forab(m, i + 1, j) {
                    int cost = 0;
                    if (s[i]  == s[m])
                        cost = 10;
                    else
                        cost = 5;
                    d[i][j][0] = max((int) d[i][j][0], d[i + 1][m][0] + d[m + 1][j][0] + cost);
                    d[i][j][1] = max((int) d[i][j][1], d[i + 1][m][0] + d[m + 1][j][1] + cost);
                }
    //        printf("%d %d %d\n", i, j, d[i][j][0]);
            }
        }
        printf("Case #%d: %d\n", qqq + 1, max(d[0][n][0], d[0][n][1]));
    }
}

