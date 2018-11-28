#include<cstdio>
#include<algorithm>
using namespace std;
int N;
double T,X,C,F,R,ans,newans;
bool greater(double a,double b)
{
	if(a-b>1e-8)return true;
	return false;
}
int main()
{
	scanf("%d",&N);
	for(int i=1;i<=N;i++)
	{
		scanf("%lf%lf%lf",&C,&F,&X);
		T=0;
		R=2.0;
		ans=T+X/R;
		newans=ans;
		do
		{
			ans=newans;
			T+=C/R;
			R+=F;
			newans=T+X/R;
		}
		while(greater(ans,newans));
		printf("Case #%d: %.7lf\n",i,ans);
	}
	return 0;
}
