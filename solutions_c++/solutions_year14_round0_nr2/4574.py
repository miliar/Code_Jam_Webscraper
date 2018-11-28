#include<cstdio>
#include<iostream>
using namespace std;
int main()
{
	//freopen("a.in","r",stdin);
//	freopen("a.out","w",stdout);
	double c,f,x;
	int T,Case=0;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%lf%lf%lf",&c,&f,&x);
		int k=(x-2)/f;
		double ans=x/2,fans=ans;
		for(int i=1;i<=k+200000;i++)
		{
			ans-=x/(2+(i-1)*f);
			ans+=c/(2+(i-1)*f)+x/(2+i*f);
			if(fans>ans)fans=ans;
		}
		printf("Case #%d: %.7lf\n",++Case,fans);
	}
	return 0;
}

