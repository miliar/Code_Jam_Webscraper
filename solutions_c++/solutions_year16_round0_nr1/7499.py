#include <bits/stdc++.h>

int main()
{
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		int k=0;
		int hashmap[10]={0};
		int n,flag=0,r;
		scanf("%d",&n);
		int num=n;
		int temp;
		if(n==0)
		{
			printf("Case #%d: INSOMNIA\n",i);
		}
		else
		{
			while(flag==0)
			{
				k++;
				flag=1;
				temp=n;
				while(n!=0)
				{
					r=n%10;
					n=n/10;
					if(hashmap[r]==0)
						hashmap[r]=1;
				}
				for(int j=0;j<10;j++)
				{
					if(hashmap[j]==0)
						flag=0;
				}
				n=num*k;
			}
			printf("Case #%d: %d\n",i,temp);
		}
	}
	return 0;
}