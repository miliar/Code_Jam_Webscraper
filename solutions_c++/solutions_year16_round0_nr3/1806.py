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

LL divs[100];


int main()
{
    freopen(FNAME".in", "r", stdin);
    freopen(FNAME".out", "w", stdout);
    int n = 32, CNT = 500;
    puts("Case #1:");
    for (LL mask = 0;  mask < (1ll<<n); mask++) {
        int ok = 1;
        if ((mask & (1ll<<(n - 1))) == 0 || mask % 2 == 0)
            continue;
        for (int base = 2; base <= 10; base++) {
            __int128 num = 0;
            fornr(i, n) {
                num *= base;    
                if (mask & (1ll << i))
                    num += 1;
            }
//            printf("%lld\n", (LL) num);
            int found = 0;
            for (LL x = 2; x * x <= num && x <= 1000; x++)
                if (num % x == 0) {
                    divs[base] = x;
                    found = 1;
                    break;
                }
            if (!found)
                ok = 0;
        }
        if (ok) {
            int found = 0;
            fornr(i, n) {
//                if( mask & (1ll << i))
  //                  found = 1;
    //            if (found || (mask & (1ll << (n - i - 1))))
                    printf("%d", (mask & (1ll<<i)) != 0);            
            }
            for (int base = 2; base <= 10; base++)
                printf(" %lld", divs[base]);
            puts("");
            CNT--;
            if (CNT == 0)
                return 0;
        }
    }
}

