#include<stdio.h>
int main()
{
	int T,i=1,a[10],s,p,k;
	long n,b,m;
	scanf("%d",&T);
	while(i<=T)
	{
		scanf("%d",&n);
		s=10;
		for(k=0;k<10;k++)
		a[k]=1;
		k=1;
		m=n;
		if(n==0)
		printf("Case #%d: INSOMNIA\n",i);
		else
		{
			if(m%10==0)
			{
				a[0]=0;
				s--;
				while((m%10)==0)
				m=m/10;
			}
			while(s!=0)
			{
				b=m*k;
				while(b)
				{
					p=b%10;
					b=b/10;
					if(a[p]!=0)
					{
						a[p]=0;
						s--;
					}
				}
				k++;
			}
			printf("Case #%d: %ld\n",i,n*(k-1));
		}
		i++;
	}
	return 0;
}
