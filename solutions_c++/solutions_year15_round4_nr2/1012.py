#include<iostream>
#include<cstdlib>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<ctime>
#include<algorithm>
#include<list>
#include<queue>
#include<stack>
#include<vector>
#include<set>
#include<map>
#include<string>
#define REP(it,end) for (int it = 1; it <= (end); it++)
#define FOR(it,begin,end) for (int it = (begin); it <= (end); it++)
#define ROF(it,begin,end) for (int it = (begin); it >= (end); it--)
using namespace std;
double r[102],c[102];
const double eps=1e-10;
double sgn(double v)
{
	if(abs(v)<eps)return 0;
	else return v<0?-1:1;
}
int main()
{
	int n,T,i;
	scanf("%d",&T);
	double v,x;
	for(int cas=1;cas<=T;cas++)
	{
		scanf("%d %lf %lf",&n,&v,&x);
		for(i=0;i<n;i++)
			scanf("%lf %lf",&r[i],&c[i]);
		//cout <<n<<" "<<v<<" "<<x<<endl;for(i=0;i<n;i++)cout <<r[i]<<" "<<c[i]<<endl;
		if(n==1)
		{
			if(sgn(x-c[0])==0)
				printf("Case #%d: %.7f\n",cas,v/r[0]);
			else 
			{
				//cout <<x<<" "<<c[0]<<endl;
				printf("Case #%d: IMPOSSIBLE\n",cas);
			}
		}
		else if(n==2)
		{
			double delta=r[0]*r[1]*c[1]-r[0]*r[1]*c[0];
			if(sgn(c[1]-c[0])==0)
			{
				if(sgn(x-c[0])==0)
					printf("Case #%d: %.7f\n",cas,v/(r[0]+r[1]));
				else 
					printf("Case #%d: IMPOSSIBLE\n",cas);
				continue;
			}
			double v1=r[0]*v*x-v*r[0]*c[0],v2=v*r[1]*c[1]-v*x*r[1];
			v1/=delta;
			v2/=delta;
			if(sgn(v1)<0||sgn(v2)<0)
			{
				printf("Case #%d: IMPOSSIBLE\n",cas);
				continue;
			}
			//cout <<v1<<" "<<v2<<endl;
			printf("Case #%d: %.7f\n",cas,max(v1,v2));
		}
	}
	return 0;
}
