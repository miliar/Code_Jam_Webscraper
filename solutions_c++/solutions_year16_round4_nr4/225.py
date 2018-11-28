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
#define fop   freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
#define getfile char fin[11], fout[11]; sprintf(fin, "%d.in", i); sprintf(fout, "%d.out", i); freopen(fin, "r", stdin); freopen(fout, "w", stdout);
#define makefile char fout[11]; sprintf(fout, "%d.in", i); freopen(fout, "w", stdout);
#define myprogram By_135678942570
#define clrcpy(x,siz,y)  for(int xx=0;xx<siz;xx++)  x[xx]=y[xx];
#define pb push_back
using namespace std;
int n;
int per[6];
int dfs(int p, int now, int init)
{
	if(p == n && now == (1 << n) - 1)
		return 1;
	int flag = 0;
	int res = 1;
	for(int i = 0; i < n; i++)
	{
		if((now & (1 << i)) == 0)
		{
			if(init & (1 << (per[p] * n + i)))
			{
				if(!dfs(p + 1, now | (1 << i), init))
					res = 0;
				flag = 1;
			}
		}
	}
	return res && flag;
}
int main()
{
	int T, cas = 0;
	fop;
	scanf("%d", &T);
	while(T--)
	{
		scanf("%d", &n);
		string s[5];
		int init = 0;
		for(int i = 0; i < n; i++)
		{
			cin>>s[i];
			for(int j = 0; j < n; j++)
				if(s[i][j] == '1')
					init |= (1 << (i * n + j));
		}
		int bit = n * n;
		int res = 0x3f3f3f3f;
		for(int i = 0; i < 1 << bit; i++)
			if((i & init) == init)
			{
				int flag = 1;
				for(int i = 0; i < n; i++)
					per[i] = i;
				do
				{
					flag &= dfs(0, 0, i);
				}while(next_permutation(per, per + n));
				if(flag)
					res = min(res, __builtin_popcount(i));
			}
		printf("Case #%d: %d\n", ++cas, res - __builtin_popcount(init));
	}
}