#include<stdio.h>
#include<math.h>
int main()
{
	int p,n,l,x;
	unsigned long long b;
	double a;
	freopen("C-small-practice.in","rt",stdin);
	freopen("csmall.out","wt",stdout);
	scanf("%d",&n);
	for(l=0;l<n;l++)
	{
		scanf("%d",&p);
		a=(3+sqrt(5));
		b=pow(a,p);
		//printf("\n%lld",b);
		x=b%1000;
		if(x>0&&x<10)
			printf("\ncase #%d: 00%d",l+1,x);
		else if(x>9&&x<100)
			printf("\ncase #%d: 0%d",l+1,x);
		else 
			printf("\ncase #%d: %d",l+1,x);
		//printf("case #%d: %d\n",l+1,);
	}
	return 0;
}
