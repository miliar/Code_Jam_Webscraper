#include<stdio.h>
int main()
{
	int t,n,i,m=1;
	scanf("%d",&t);
	while(t!=0)
	{
		int sum=0,c=0;
		scanf("%d",&n);
		int a[(n+1)];
		char ch,b[(n+1)];
		scanf("%s",b);
		for(i=0;i<=n;i++)
		{
			ch=b[i];
			a[i]=(int)ch-48;
		}
		for(i=1;i<=n;i++)
		{
			sum=sum+a[i-1];
			if(sum<i)
			{
				c++;
				sum=sum+1;
			}
		}
		printf("\nCase #%d: %d",m,c);
		m++;
		t--;
	}
	return 0;
}
