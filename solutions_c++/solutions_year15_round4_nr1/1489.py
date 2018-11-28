#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
using namespace std;

typedef long long LL;
//typedef unsigned int ULL;
typedef pair<int,int> PII;
typedef vector<int> VI;

#define clr(a,b)    (memset(a,b,sizeof(a)))
#define PB push_back
#define MP make_pair
#define rep(i,a)    for(int i=0; i<(int)a.size(); i++)

const int INF = 0x3f3f3f3f;
const double eps = 1E-8;

int T,n ,m;

char g[111][111];
bool vis[111][111];
map<char, int> dir;
int ans;



int main()
{
//    freopen("in","r", stdin);

    freopen("A-large.in","r", stdin);
    freopen("out","w", stdout);

    scanf("%d",&T);
	int cas = 1;

	dir['>'] = 0;
	dir['v'] = 1;
	dir['<'] = 2;
	dir['^'] = 3;

    while(T--)
    {
    	scanf("%d%d",&n,&m);
    	clr(g, 0);

    	for(int i=1; i<=n; i++)
			scanf("%s", g[i] + 1);

		printf("Case #%d: ",cas++);

		bool invalid = false;

		for(int i=1; i<=n; i++)
			for(int j=1; j<=m; j++)
				if(g[i][j] != '.')
				{
					int cc = 0;
					for(int k=1; k<=m; k++)
					{
						if(k == j)	continue;
						if(g[i][k] != '.') cc++;
					}

					for(int k=1; k<=n; k++)
					{
						if(k == i)	continue;
						if(g[k][j] != '.') cc++;
					}

					if(cc == 0)	invalid = true;
				}

		if(invalid)
		{
			printf("IMPOSSIBLE\n");
			continue;
		}

		ans = 0;
		clr(vis, false);
		for(int i=1; i<=n; i++)
			for(int j=1; j<=m; j++)
			{
				if(g[i][j] != '.')
				{
					int d = dir[g[i][j]];
					if(d == 0)
					{
						int ok = 0;
						for(int k=j+1; k<=m; k++)
							if(g[i][k] != '.')
							{
								ok = 1;
							}
						if(ok == 0)	ans++;
					}
					if(d == 2)
					{
						int ok = 0;
						for(int k=j-1; k>=1; k--)
							if(g[i][k] != '.')
							{
								ok = 1;
							}
						if(ok == 0)	ans++;
					}

					if(d == 1)
					{
						int ok = 0;
						for(int k=i+1; k<=n; k++)
							if(g[k][j] != '.')
							{
								ok = 1;
							}
						if(ok == 0)	ans++;
					}
					if(d == 3)
					{
						int ok = 0;
						for(int k=i-1; k>=1; k--)
							if(g[k][j] != '.')
							{
								ok = 1;
							}
						if(ok == 0)	ans++;
					}
				}
			}
		printf("%d\n", ans);

    }
}
