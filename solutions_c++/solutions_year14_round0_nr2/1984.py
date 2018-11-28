#include<stdio.h>

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	double c,f,x,time,g;
	int n,farm;
	scanf("%d",&n);
	for(int i=0;i<n;i++)
	{
		g=2;
		scanf("%lf",&c);
		scanf("%lf",&f);
		scanf("%lf",&x);
		time=0;
		while( (c/g)+(x/(f+g)) < (x/g) )
		{
			time+=c/(g);
			g+=f;
		}
		time+=x/g;
		printf("Case #%d: %.7lf\n",i+1,time);
	}
	return 0;
}