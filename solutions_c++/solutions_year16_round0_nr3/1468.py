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
long long convert(long long p, long long q)
{
	long long k = 1;
	long long res = 0;
	while(p)
	{
		if(p % 2)
			res += k;
		k *= 10;
		p /= 2;
	}
	return res;
}
long long convert2(long long p, long long q)
{
	long long res = 0;
	long long k = 1;
	while(p)
	{
		if(p % 2)
			res += k;
		k *= q;
		p /= 2;
	}
	return res;
}
int main()
{
	freopen("out1.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	int n, m;
	scanf("%d%d", &n, &m);
	int bit = n / 2;
	puts("Case #1:");
	for(long long i = (1ll << bit - 1) + 1; (i <= (1ll << bit) - 1) && m; i += 2)
	{
		printf("%lld%lld", convert(i, 2), convert(i, 2));
		for(int j = 2; j <= 10; j++)
		{
			printf(" %lld", convert2(i, j));
		}
		puts("");
		m--;
	}
}