#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
	int t,i,temp;
	cin>>t;
	for(i=1; i<=t; i++)
	{
		long long int n,no,j;
		int mark[10]={0},ml=10;  //ml=marks left
		scanf("%lld",&n);
		if(n==0)
		{
			printf("Case #%d: INSOMNIA\n",i);
			continue;
		}
		for(j=1; ml!=0; j++)
		{
			no=n*j;
			while(no!=0)
			{
				temp=no%10;
				if(mark[temp]==0)
				{
					ml--;
					mark[temp]=1;
				}
				no/=10;
			}
		}
		printf("Case #%d: %lld\n",i,n*(j-1));
	}
}
