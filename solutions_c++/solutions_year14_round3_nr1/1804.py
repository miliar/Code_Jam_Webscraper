#include<cstdio>
int test,ii,j;
double w;
long long bb,a,b,p;
long long gcd(long long a,long long b)
{
	long long w;
	if (b==0) return a;
	w=gcd(b,a%b);
	return w;
}
int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&test);
	for (ii=1;ii<=test;ii++)
	{
		scanf("%lld/%lld",&a,&b);
		p=gcd(a,b);
		a=a/p;
		b=b/p;
		
		bb=b;
	    while (bb%2==0)
	    {
	    	bb=bb/2;
	    }
	    
	    if (bb!=1)
	    {
	    	printf("Case #%d: impossible\n",ii);
	    	continue;
	    }
	    w=1;
	    if (a/b!=1)
	    for (j=1;j<=40;j++)
	    {
	    	w=w/2;
	    	if (w<=a*1.0/b)
	    	break;
	    }
	    if (j<=40)
	    printf("Case #%d: %d\n",ii,j);
	    else
	    printf("Case #%d: impossible\n");
	}
}
