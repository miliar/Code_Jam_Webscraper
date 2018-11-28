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
int main()
{
	int T,cas = 0;
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &T);
	while(T--)
	{
		int n, m, c;
		scanf("%d%d%d", &n, &m, &c);
		int res = 99999;
		for(int i = 0; i < 1 << n * m; i++)
		{
			int cnt = 0;
			if(__builtin_popcount(i) != c)
				continue;
			for(int j = 0; j < n * m; j++)
			if(i & (1 << j))
			{
				if(j >= m && (i & (1 << j - m)))
					cnt++;
				if(j % m && (i & (1 << j - 1)))
					cnt++;
				if(j + m < n * m && (i & (1 << j + m)))
					cnt++;
				if(j % m != m - 1 && (i & (1 << j + 1)))
					cnt++;
			}
			res = min(res, cnt);
		}
		printf("Case #%d: %d\n", ++cas, res / 2);
	}
}