// @author cebrusfs
// headers {{{
#include<bits/stdc++.h>
using namespace std;
// }}}
// macros {{{
#ifdef WIN32
    #define LLD "%I64d"
#else
    #define LLD "%lld"
#endif

#define FOR(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)

#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())
#define UNIQUE(x) (sort(ALL(x)), ((x).erase(unique(ALL(x)), (x).end())))
#define MS(x, v) std::fill(ALL(x), (v));


#define IOS ios_base::sync_with_stdio(false)

#define REP(i,n) for(int i=0;i<(n);i++)
#define REP1(i,a,b) for(int i=(a);i<=(b);i++)

#define PER(i,n) for(int i=(n)-1;i>=0;i--)
#define PER1(i,a,b) for(int i=(a);i>=(b);i--)

#ifdef ONLINE_JUDGE
#define FILEIO(x) freopen(#x ".in","r",stdin);freopen(#x ".out","w",stdout);
#define FILEIOS freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
#else
#define FILEIO(x) ;
#define FILEIOS ;
#endif

typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

typedef pair<int, int> PII;
#define MP make_pair
#define F first
#define S second

typedef vector<int> VI;
#define PB push_back
#define PF push_front

#define PPB pop_back
#define PPF pop_front


// C++11
#if __cplusplus >= 201103L
#define MT make_tuple
typedef tuple<int, int> TII;
#endif

#define runtime() ((double)clock() / CLOCKS_PER_SEC)

const double eps = 1e-7;
// }}}

#define MAX 105

int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

char mp[MAX][MAX];

bool fail[MAX][MAX][4];
int ctod[256];


int n, m;

void trace(int x, int y, int d)
{
    int rd = (d + 2) % 4;

    while (x >= 0 and x < n and y >= 0 and y < m)
    {
        if (mp[x][y] != '.')
        {
            fail[x][y][d] = true;
            return ;
        }
        x += dx[rd];
        y += dy[rd];
    }
}
void solve(int testi)
{
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; ++i)
        scanf("%s", mp[i]);

    memset(fail, 0, sizeof(fail));
    for (int i = 0; i < n; ++i)
    {
        trace(i, 0, 3);
        trace(i, m - 1, 1);
    }
    for (int i = 0; i < m; ++i)
    {
        trace(0, i, 2);
        trace(n - 1, i, 0);
    }

    int ans = 0;
    bool noans = false;
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
        {
            if(mp[i][j] != '.')
            {
                int d = ctod[mp[i][j]];
                if (fail[i][j][d])
                {
                    ans++;
                    bool flag = true;
                    for (int k = 0; k < 4; ++k)
                        flag &= fail[i][j][k];
                    if (flag) noans = true;
                }
            }
        }

    printf("Case #%d: ", testi);
    if (noans)
        printf("IMPOSSIBLE\n");
    else
        printf("%d\n", ans);
}

int main()
{
    ctod['v'] = 0;
    ctod['^'] = 2;
    ctod['>'] = 1;
    ctod['<'] = 3;

    int z;
    scanf("%d", &z);
    for (int zi = 1; zi <= z; ++zi)
        solve(zi);
}

