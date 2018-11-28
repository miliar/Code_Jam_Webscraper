#include <set>
#include <cmath>
#include <stack>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <numeric>
#include <vector>
#include <ctime>
#include <queue>
#include <list>
#include <map>
#define pi acos(-1.0)
#define INF 0x3f3f3f3f
#define clr(x)  memset(x,0,sizeof(x));
#define clrto(x,siz,y)  for(int xx=0;xx<=siz;xx++)  x[xx]=y;
#define clrset(x,siz)  for(int xx=0;xx<=siz;xx++)  x[xx]=xx;
#define clr_1(x) memset(x,-1,sizeof(x));
#define clrmax(x) memset(x,0x3f,sizeof(x));
#define clrvec(x,siz) for(int xx=0;xx<=siz;xx++)  x[xx].clear();
#define fop2   freopen(".in","r",stdin); //freopen(".out","w",stdout);
#define fop   freopen("in.txt","r",stdin);//freopen("out.txt","w",stdout);
#define getfile sprintf(fin, "%d.in", i); sprintf(fout, "%d.out", i); freopen(fin, "r", stdin); freopen(fout, "w", stdout);
#define myprogram By_135678942570
#define clrcpy(x,siz,y)  for(int xx=0;xx<siz;xx++)  x[xx]=y[xx];
#define pb push_back
using namespace std;
char mp[111][111];
int cnt[111][111];
int res[111][111];
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, cas = 0;
	scanf("%d", &T);
	while(T--)
	{
		clr(cnt);
		clr(res);
		int n, m;
		scanf("%d%d", &n, &m);
		for(int i = 0; i < n; i++)
			scanf("%s", mp[i]);
		for(int i = 0; i < n; i++)
		{
			for(int j = 0; j < m; j++)
			{
				if(mp[i][j] != '.')
				{
					cnt[i][j]++;
					if(mp[i][j] == '<')
						res[i][j] = 1;
					break;
				}
			}
			for(int j = m - 1; j >= 0; j--)
			{
				if(mp[i][j] != '.')
				{
					cnt[i][j]++;
					if(mp[i][j] == '>')
						res[i][j] = 1;
					break;
				}
			}
		}
		for(int j = 0; j < m; j++)
		{
			for(int i = 0; i < n; i++)
			{
				if(mp[i][j] != '.')
				{
					cnt[i][j]++;
					if(mp[i][j] == '^')
						res[i][j] = 1;
					break;
				}
			}
			for(int i = n - 1; i >= 0; i--)
			{
				if(mp[i][j] != '.')
				{
					cnt[i][j]++;
					if(mp[i][j] == 'v')
						res[i][j] = 1;
					break;
				}
			}
		}
		int flag = 1;
		int r = 0;
		for(int i = 0; i < n; i++)
			for(int j = 0; j < m; j++)
				if(cnt[i][j] == 4)
				{
					flag = 0;
					i = n;
					break;
				}
				else
					r += res[i][j];
		printf("Case #%d: ", ++cas);
		if(flag == 0)
			puts("IMPOSSIBLE");
		else printf("%d\n", r);
	}
}