#include<stdio.h>
int main()
{
	long int t,l,i,j,a,b=0;
	double c,f,x,n[100000],pr=2.0;
	freopen("B-large.in","rt",stdin);
	freopen("large.out","wt",stdout);
	scanf("%ld",&t);
	for(l=0;l<t;l++)
	{
		scanf("%lf",&c);
		scanf("%lf",&f);
		scanf("%lf",&x);
		n[0]=(x/pr);
		i=1;
		do
		{
			n[i]=(x/((i*f)+pr));
			for(j=1;j<=i;j++)
				n[i]+=(c/(((i-j)*f)+pr));
			if(n[i]<n[i-1])
			{
				a=i;
				b++;
			}
			i++;
		}while(n[i-1]<n[i-2]);
		if(b==0)
			a=0;
		printf("case #%ld: %.7f\n",l+1,n[a]);
		a=0;
	}
	return 0;
}
