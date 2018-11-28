#include<cstdio>
long double a,b,c,s,ans;
int ii,test,i,j;
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&test);
	while (test)
	{
		ans=1000000000;
		test--;
		ii++;

    scanf("%lf%lf%lf",&a,&b,&c);
    if (a<c)
	{
		for (i=0;i<=2000;i++)
		{
			s=0;
			for (j=1;j<=i;j++)
				s=s+a/(2+(j-1)*b);
			s=s+c/(i*b+2);
			if (s<ans) ans=s;
		}
	}
	else
	ans=c/2;
    printf("Case #%d: %.7f\n",ii,ans);
	}
}