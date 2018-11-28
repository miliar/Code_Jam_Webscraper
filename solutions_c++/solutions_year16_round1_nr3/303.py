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
#define getfile char fin[11], fout[11]; sprintf(fin, "%d.in", i); sprintf(fout, "%d.out", i); freopen(fin, "r", stdin); freopen(fout, "w", stdout);
#define makefile char fout[11]; sprintf(fout, "%d.in", i); freopen(fout, "w", stdout);
#define myprogram By_135678942570
#define clrcpy(x,siz,y)  for(int xx=0;xx<siz;xx++)  x[xx]=y[xx];
#define pb push_back
using namespace std;
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, cas = 0;
	scanf("%d", &T);
	while(T--)
	{
		int fri[2222];
		int n;
		scanf("%d", &n);
		for(int i = 1; i <= n; i++)
			scanf("%d", &fri[i]);
		int res = 1;
		vector<pair<int, int> >V;
		int rr = 0;
		for(int i = 1; i <= n; i++)
		{
			int tmp = i;
			int vis[1111] = {0};
			int cnt = 0;
			while(!vis[tmp])
			{
				vis[tmp] = 1;
				cnt++;
				tmp = fri[tmp];
			}
			if(tmp == fri[fri[tmp]])
			{
				V.push_back(make_pair(tmp, cnt));
				res = max(res, cnt);
			}
			else if(tmp == i)
			{
				res = max(res, cnt);
			}
		}
		int len = V.size();
		for(int i = 0; i < len; i++)
			for(int j = i + 1; j < len; j++)
				if(V[i].first == fri[V[j].first])
				{
					res = max(res, V[i].second + V[j].second - 2);
				}
		int maxn[1111] = {0};
		for(int i = 0; i < len; i++)
		{
			//printf("%d %d\n", V[i].first, V[i].second);
			int cc = V[i].first;
			maxn[cc] = max(maxn[cc], V[i].second); 
		}
		for(int i = 0; i <= n; i++)
		if(maxn[i])
		{
			rr += maxn[i] - 1;
		}
		res = max(res, rr);
		printf("Case #%d: %d\n", ++cas, res);
	}
}