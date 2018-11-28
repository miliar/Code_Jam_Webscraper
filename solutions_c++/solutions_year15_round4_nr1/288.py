#include <bits/stdc++.h> 

using namespace std;
 
#define sz(c) (int)(c).size()
 
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
 
#define forn(i,n) for( int i = 0 ; i < (n) ; i++ )
#define forit(it,c) for( __typeof((c).begin()) it = (c).begin() ; it != (c).end() ; it++ )
 
typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef unsigned int uint;

#ifdef WIN32
#define I64 "%I64d"
#else
#define I64 "%lld"
#endif

#define FNAME "1"

const int MAXN = 205;
const int turn[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
const char *alpha = "^>v<.";

int n, m;
int a[MAXN][MAXN];
char s[MAXN];

bool good(int x, int y)
{
    return x >= 0 && y >= 0 && x < n && y < m;
}

int main() 
{
    freopen(FNAME".in", "r", stdin);
    freopen(FNAME".out", "w", stdout); 
    int T;
    scanf("%d", &T);
    for (int t = 0; t < T; t++)
    {
        scanf("%d%d\n", &n, &m);
        for (int i = 0; i < n; i++)
        {
            gets(s);
            for (int j = 0; j < m; j++)
                a[i][j] = strchr(alpha, s[j]) - alpha;
        }
        int possible = 1, ans = 0;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                if (a[i][j] == 4)
                    continue;
                int dx = turn[a[i][j]][0], dy = turn[a[i][j]][1];
                int x = i + dx, y = j + dy;
                while (good(x, y) && a[x][y] == 4)
                    x += dx, y += dy;
                if (!good(x, y))
                {
                    int ok = 0;
                    for (int g = 0; g < 4; g++)
                    {
                        dx = turn[g][0], dy = turn[g][1];
                        x = i + dx, y = j + dy;
                        while (good(x, y) && a[x][y] == 4)
                            x += dx, y += dy;
                        if (good(x, y))
                            ok = 1;
                    }
                    if (!ok)
                        possible = 0;
                    ans++;
                }

            }
        }
        printf("Case #%d: ", t + 1);
        if (!possible)
            puts("IMPOSSIBLE");
        else
            printf("%d\n", ans);    
    } 

    return 0;
}