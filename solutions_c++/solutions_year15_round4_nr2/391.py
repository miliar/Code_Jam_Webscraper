#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<string>
#include<map>
#include<cmath>
#include<iostream>
#include<vector>
#include<ctime>
#include<algorithm>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> per;
#define mp(x,y) make_pair(x,y)
inline int readT(){
    int ret = 0; char c;
    while(c = getchar(), c < '0' || c > '9') ; ret = c - 48;
    while(c = getchar(), c >= '0' && c <= '9') ret = ret * 10 + c - 48;
    return ret;
}
const int MOD = 1000000007;
const int INF = 1000000007;
const int M = 100005;
const int N = 105;
double x[N],y[N];
int main()
{
	//ios_base::sync_with_stdio(0);
	freopen("B-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,ca=1;
	scanf("%d",&T);
	while(T--)
	{
		printf("Case #%d: ",ca++);
		int n;
		double X,V;
		scanf("%d%lf%lf",&n,&V,&X);
		for(int i=0;i<n;i++)
		{
			scanf("%lf%lf",&x[i],&y[i]);
		}
		if(n==1)
		{
			if(y[0]==X)
			{
				printf("%.9lf\n",V/x[0]);
			}
			else puts("IMPOSSIBLE");
		}
		else
		{
			if(y[0]==y[1])
			{
				if(y[0]==X)
				{
					printf("%.9lf\n",V/(x[0]+x[1]));
				}
				else puts("IMPOSSIBLE");
			}
			else
			{
				double a=V*(X-y[1])/(y[0]-y[1]),b=V-a;
				//printf("a:%lf b:%lf a+b:%lf 1:%lf 2:%lf \n",a,b,a+b,(X-y[1]),(y[0]-y[1]));
				if(a>=0.0&&b>=0.0&&a<=V&&b<=V)
				{
					double ret=max(a/x[0],b/x[1]);
					printf("%.9lf\n",ret);
				}
				else if(y[0]==X)
				{
					printf("%.9lf\n",V/x[0]);
				}
				else if(y[1]==X)
				{
					printf("%.9lf\n",V/x[1]);
				}
				else puts("IMPOSSIBLE");
			}
		}
	}
    return 0;
}




















