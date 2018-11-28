#include<iostream>
#include<cstdio>
#include<cstdlib>

using namespace std;

bool isAllVisited(int hash[],int n)
{
	for(int i=0;i<n;i++)
	{
		if(hash[i]!=true)
			return false;
	}
	return true;
}
int main()
{
	int test,t,n;
	
	scanf("%d",&test);
	
	for(t=1;t<=test;t++)
	{
		scanf("%d",&n);
		if(n==0)
			printf("Case #%d: INSOMNIA\n",t);
		else
		{

			int hash[10];
			for(int i=0;i<10;i++)
				hash[i]=0;
		
			int temp,num=1;
			while(isAllVisited(hash,10)==false)
			{
				temp=num*n;
				while(temp!=0)
				{
					hash[temp%10]=1;
					temp=temp/10;
				}
				num++;
			}
			printf("Case #%d: %d\n",t,n*(num-1));
		}
	}
	return 0;
}
