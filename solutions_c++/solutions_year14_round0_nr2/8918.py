#include<cstdio>

int main()
{
int i,j,k,l,m,n,t;
double x,c,f,ans;

scanf("%d",&t);
for(m=1;m<=t;m++)
	{
	scanf("%lf%lf%lf",&c,&f,&x);
	i= x/c-2/f;

	if(i<0) i=0;

	ans=0;
	for(j=0;j<i;j++)
	{
	ans+= c/(2+j*f);
	}
	ans+= x/(2+i*f);

	printf("Case #%d: %.7lf\n",m,ans);
	}
return 0;
}
