#include <bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define fi first
#define prev asfansjfansjabfasjlbfa
#define se second
#define I "%d"
#define II "%d%d"
#define III "%d%d%d"
#define out_files freopen("B-large.in", "r", stdin);freopen("output.txt", "w", stdout)
#define all(x) (x).begin(), (x).end()
#define fast ios_base::sync_with_stdio(0)
#define sqr(x) (x)*(x)
#define y1 asnflainflawnfaw
#define y0 snalfklawnfasdaspqw

using namespace std;

typedef vector <int> vi;
typedef long long ll;
typedef unsigned long long ull;
typedef pair <ll, ll> pii;
typedef vector <pii> vii;
typedef long double ld;

#ifdef WIN32
    #define I64 "%I64d"
#else
    #define I64 "%lld"
#endif // WIN32

const int inf = 1000000000;
const ll INF = 1LL*inf*inf;
const double eps = 1e-9;
const int MAXN = 2500;
const int md = (int)1e9 ;
const double EPS = 1e-5;

ll step[2000], a[200][200], n, m;
int t;

int main()
{
    fast;
    out_files;
    scanf(I, &t);
    step[0] = 1;
    for (int i=1; i<=50; i++)
        step[i] = step[i-1]*2ll;
    for (int test = 1; test<=t; test++)
    {
        scanf(I64 I64, &n, &m);
        printf("Case #%d: ", test);
        for (int i=1; i<=n; i++)
            for (int j=1; j<=n; j++)
                a[i][j] = 0;
        ll q = step[n-2];
        if (q < m)
        {
            printf("IMPOSSIBLE\n");
            continue;
        }
        for (int i=1; i<n; i++)
            for (int j=i+1; j<=n; j++)
                if (i!=j) a[i][j] = 1;
        for (int i=n-1; i>=1; i--)
        {
            if (m >= step[max(i-2,0)]) m-=step[i-2]; else a[i][n] = 0;
        }
        printf("POSSIBLE\n");
        for (int i=1; i<=n; i++)
        {
            for (int j=1; j<=n; j++)
                printf(I64, a[i][j]);
            printf("\n");
        }
    }
    return 0;
}
