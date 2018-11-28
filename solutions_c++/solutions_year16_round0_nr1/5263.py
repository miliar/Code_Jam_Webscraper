#include<bits/stdc++.h>
using namespace std;
int *hash[10];

bool check()
{
	for(int i=0;i<10;i++)
	{
		if(hash[i] == 0)
		return false;
	}
	return true;
}
int main()
{
	int n,temp,m,t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		scanf("%d",&n);
		if(n==0)
		printf("Case #%d: INSOMNIA\n",i);
		else
		{
			memset(hash,0,sizeof(hash));
			m=1;
			while(m<=100)
			{
				temp=m*n;
				while(temp >0)	
				{
					hash[temp%10]++;
					temp/=10;
				}
				if(check())
				{
					printf("Case #%d: %d\n",i,m*n);
					break;
				}
				m++;
			}
		}
	}
	
}
