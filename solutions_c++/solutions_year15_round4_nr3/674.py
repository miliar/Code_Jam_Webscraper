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
#define SMAX (1000 * 11)


char str[SMAX];
vector<int> ary[MAX];
int vis[2][SMAX];

void solve(int testi)
{
    fprintf(stderr, "%d\n", testi);
    int n;
    scanf("%d", &n);
    gets(str);

    map<string, int> mp;
    for (int i = 0; i < n; ++i)
    {
        gets(str);

        ary[i].clear();
        for (char *p = strtok(str, " "); p; p = strtok(NULL, " "))
        {
            int id = mp.size();
            if (not mp.count(p))
                mp[p] = id;
            ary[i].PB(mp[p]);
        }
    }
    int N = max((1 << (n - 2)) - 1, 1);

    int ans = SMAX;
    memset(vis, 0, sizeof(vis));
    int flag = 0;
    for (int j = 0; j < N; ++j)
    {
        flag++;
        for (int i = 0; i < 2; ++i)
            for (int v : ary[i])
                vis[i][v] = flag;

        for (int i = 2; i < n; ++i)
        {
            bool g = j & (1 << (i - 2));

            for (int v : ary[i])
                vis[g][v] = flag;
        }

        int cnt = 0;
        for (int i = 0; i < SZ(mp); ++i)
            if(vis[0][i] == flag and vis[1][i] == flag)
                cnt++;
        ans = min(cnt, ans);
    }
    printf("Case #%d: %d\n", testi, ans);
}

int main()
{
    int z;
    scanf("%d", &z);
    for (int zi = 1; zi <= z; ++zi)
        solve(zi);
}

