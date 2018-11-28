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

int a[10][10], b[10][10], used[10], T, n;
char s[10][10];

int gen(int pos, int last) {
    if (pos == last)
        return gen(pos + 1, last);
    if (pos == n) {
        forn(i, n)
            if (b[last][i] && !used[i])
                return 1;                
        return 0;
    }
    int ok = 0;
    forn(i, n) {
        if (b[pos][i] && !used[i]) {
            ok = 1;
            used[i] = 1;
            if (!gen(pos + 1, last)) {
                used[i] = 0;
                return 0;
            }
            used[i] = 0;
        }            
    }
    return ok;
}

bool ok() {
    forn(last, n)
        if (!gen(0, last)) 
            return 0;
    return 1;
}

int main()
{
#ifdef LOCAL
    freopen(FNAME".in", "r", stdin);
    freopen(FNAME".out", "w", stdout);
#endif
double timer = clock();
    scanf("%d", &T);
    forn(qqq, T) {
        scanf("%d", &n);
        forn(i, n)  {
            scanf(" %s", s[i]);
            forn(j, n)
                a[i][j] = s[i][j] - '0';
        }
        int n2 = n * n;
        int ans = 1e9;
        forn(mask, 1<<n2) {
            int cost = 0;
            forn(i, n) {
                forn(j, n) {
                    b[i][j] = a[i][j] || (1<<(n * i + j) & mask) != 0;
                    if (b[i][j] != a[i][j])
                        cost++;
                }
            }
            if (cost < ans && ok()) {
             /*   forn(i, n){ 
                    forn(j, n)
                        printf("%d", b[i][j]);
                    puts("");
                }      */
                ans = cost;
            }
        }
        printf("Case #%d: %d\n", qqq + 1, ans);
    }
    cerr << (clock() - timer) / CLOCKS_PER_SEC << endl;
}


