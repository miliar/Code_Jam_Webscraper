#include<stdio.h>
#include<iostream>
using namespace std;
int sum(int a[],int n)
{
	int i,sum=0;
	for(i=0;i<=n;i++)
	sum=sum+a[i];
	return sum;
}
int main()
{
	int t;
	scanf("%d",&t);
	int n=t;
	while(t--)
	{
		int smax,count=0;
		scanf("%d",&smax);
		int a[smax+1];
		int i=0;
    getchar();
    while((a[i]=getchar())!='\n')
    {
    	i++;
    }
    for(i=0;i<=smax;i++)
    	a[i]=a[i]-'0';
		if(a[0]==0)
		{
			count++;
			a[0]=1;
		}
			for(i=1;i<=smax;i++)
				{
					if(i<=sum(a,i-1))
						count=count;
					else
					{
						count=count+i-sum(a,i-1);
						a[i-1]=a[i-1]+i-sum(a,i-1);
						
					}
				}

		printf("Case #%d: %d\n",n-t,count);
	}
}