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

int T, used[20];

int main()
{
    freopen(FNAME".in", "r", stdin);
    freopen(FNAME".out", "w", stdout);

    scanf("%d", &T);
    forn(tt, T) {
        int n1;
        scanf("%d", &n1);
        LL n = n1;
        forn(i, 10)
            used[i] = 0;
        LL ans = 0;
        forn(qq, n) {
            LL x = n;        
            while (x > 0)
                used[x % 10] = 1, x /= 10;
            int ok = 1;
            forn(i, 10)
                if (!used[i])
                    ok = 0;                
            if (ok) {
                ans = n;
                break;
            }
            n += n1;
        }
        printf("Case #%d: ", tt + 1);
        if (!ans)
            puts("INSOMNIA");
        else    
            printf("%lld\n", ans);
    }
}

