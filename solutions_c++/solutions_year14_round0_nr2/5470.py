#include<cstdio>
#include<cmath>
#include<cstring>

int main()
{
	//freopen("2.in","r",stdin);
	//freopen("22.txt","w",stdout);
	int t,T;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		double C,F,X;
		scanf("%lf%lf%lf",&C,&F,&X);
		int m=(int)(ceil(X/C-2.0/F-1.0));
		m = m>=0?m:0;
		double ans=0.0;
		int i;
		for(i=0;i<m;i++)
			ans+=C/(2.0+F*i);
		ans+=X/(2+i*F);
		printf("Case #%d: %.7lf\n",t,ans);
	}
	return 0;
}