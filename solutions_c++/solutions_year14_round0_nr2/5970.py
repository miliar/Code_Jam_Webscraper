include <stdio.h>
int main()
{
	//freopen("A-small-attempt0.in","r",stdin);
	//freopen("A-small-attempt0.out","w",stdout);
	double c,f,x,t,mint;
	int k,nCases,i,j;
	scanf("%d",&nCases);
	for(i=1;i<=nCases;i++)
	{
		scanf("%lf %lf %lf",&c,&f,&x);
		mint=x/2.0;
		for(k=1;;k++)
		{
			//t=(double)k*c/2.0+x/(2.0+(double)k*f);
			t=x/(2.0+(double)k*f);
			for(j=0;j<k;j++)
			{
				t+=c/(2.0+j*f);
			}
			if(t<mint)
			{
				mint=t;

			}
			else
			{
				printf("Case #%d: %.7lf\n",i,mint);
				break;
			}
		}
	}
	
	return 0;
}