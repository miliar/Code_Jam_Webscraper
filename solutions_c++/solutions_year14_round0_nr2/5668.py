#include<stdio.h>

int main()
{
	freopen("C:\\Users\\Fred\\Downloads\\B-small-attempt0.in","r",stdin);
	freopen("C:\\Users\\Fred\\Downloads\\B-small-attempt0.out","w",stdout);
	int t;
	double c,f,x,g,time;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		g=2;
		time=0;
		scanf("%lf",&c);
		scanf("%lf",&f);
		scanf("%lf",&x);
		while((c/g)+(x/(g+f))<(x/g))
		{
			time+=c/g;
			g+=f;
		}
		time+=x/g;
		printf("Case #%d: %.7lf\n",i+1,time);
	}
	return 0;
}