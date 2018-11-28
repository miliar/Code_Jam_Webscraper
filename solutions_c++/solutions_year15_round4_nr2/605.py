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
#define fop   freopen("in.txt","r",stdin);freopen("out2.txt","w",stdout);
#define getfile sprintf(fin, "%d.in", i); sprintf(fout, "%d.out", i); freopen(fin, "r", stdin); freopen(fout, "w", stdout);
#define myprogram By_135678942570
#define clrcpy(x,siz,y)  for(int xx=0;xx<siz;xx++)  x[xx]=y[xx];
#define pb push_back
using namespace std;
int main()
{
	fop;
	int T, cas = 0;
	scanf("%d", &T);
	while(T--)
	{
		int n;
		scanf("%d", &n);
		double V, X;
		double v1, x1, v2, x2;
		scanf("%lf%lf%lf%lf", &V, &X, &v1, &x1);
		if(n == 1)
		{
        	if(fabs(x1 - X) > 1e-8)
        		printf("Case #%d: IMPOSSIBLE\n", ++cas);
        	else
        		printf("Case #%d: %.10f\n", ++cas, V / v1);
        	continue;
		}
		else
		{
			scanf("%lf%lf", &v2, &x2);
			long double P = (V * X - V * x2) / (x1 - x2);
			if(fabs(x1 - x2) < 1e-8)
			{
				if(fabs(X - x1) < 1e-8)
        			printf("Case #%d: %.10f\n", ++cas, (double)(V / max(v1, v2)));
        		else
        			printf("Case #%d: IMPOSSIBLE\n", ++cas);
			}
			else if(P < -1e-8 || P > V + 1e-8)
        		printf("Case #%d: IMPOSSIBLE\n", ++cas);
        	else printf("Case #%d: %.10f\n", ++cas, (double)max(P / v1, (V - P) / v2));
		}
	}
}
