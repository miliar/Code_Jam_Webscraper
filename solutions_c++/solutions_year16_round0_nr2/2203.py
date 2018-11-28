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

char s[1000];

int main()
{
    freopen(FNAME".in", "r", stdin);
    freopen(FNAME".out", "w", stdout);
    int T;
    scanf("%d", &T);
    forn(tt, T) {
        scanf(" ");
        gets(s);
        int n = strlen(s);
        int ans = 0;
        fornr(i, n) {
            if (s[i] == '-') {
           //     reverse(s, s + i + 1);
                forn(j, i + 1)
                    if (s[j] == '+')
                        s[j] = '-';
                    else
                        s[j] = '+';
                ans++;
            }
        }
        printf("Case #%d: %d\n", tt + 1, ans);
    }
}

