#include <stdio.h>

int main()
{
	//freopen("in.in","r",stdin);
	//freopen("in.out","w",stdout);

	int T,time=0;
	double c,f,x,ans,pos;

	scanf("%d",&T);

	while(T--)
	{
		ans=0.0;
		pos=2.0;
		scanf("%lf %lf %lf",&c,&f,&x);
		while( x/pos>=c/pos+x/(pos+f)  )
		{
			ans+=c/pos;
			pos+=f;
		}
		ans+=x/pos;
		printf("Case #%d: %.7lf\n",++time,ans);
	}
	return 0;
}