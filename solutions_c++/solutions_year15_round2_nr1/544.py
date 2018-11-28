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
int q[1000111];
int vis[1000111];
int dis[1000111];
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, cas = 0;
	int front = 0, rear = 0;
	q[++front] = 1;
	vis[1] = 1;
	dis[1] = 1;
	while(front > rear)
	{
		int now = q[++rear];
		int dd = dis[now];
		if(now <= 999999 && vis[now + 1] != 1)
		{
			vis[now + 1] = 1;
			dis[now + 1] = dis[now] + 1;
			q[++front] = now + 1;
		}
		int nn[8] = {0};
		int cnt = 0;
		while(now)
		{
			nn[cnt++] = now % 10;
			now /= 10;
		}
		int tmp = 1;
		for(int i = cnt - 1; i >= 0; i--)
			now += nn[i] * tmp, tmp *= 10;
		if(vis[now] != 1)
		{
			vis[now] = 1;
			dis[now] = dd + 1;
			q[++front] = now;
		}
	}
	scanf("%d", &T);
	while(T--)
	{
		int n;
		scanf("%d", &n);
		printf("Case #%d: %d\n", ++cas, dis[n]);
	}
}