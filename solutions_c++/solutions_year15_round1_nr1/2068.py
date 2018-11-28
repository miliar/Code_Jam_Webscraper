#include<stdio.h>
int main()
{
	int t;
	scanf("%d",&t);
	for(int z=1;z<=t;z++)
	{
		int n,a,b,s1,s2;
		a=0;
		b=0;
		s1=0;
		s2=0;
		scanf("%d",&n);
		int st[n];
		int m=0;
		for(int j=0;j<n;j++)
		{
			scanf("%d",&b);
			st[j]=b;
			if(a>b)
			{
				s1+=a-b;
			}
			if(m<(a-b))
			{
				m=a-b;
			}
			a=b;
		}
		//printf("%d\n",m);
		for(int j=0;j<n-1;j++)
		{
			if(st[j]>=m)
			{
				s2+=m;
			}
			else
			{
				s2+=st[j];
			}
		}	
		printf("Case #%d: %d %d\n",z,s1,s2);
	}
	return 0;
}
