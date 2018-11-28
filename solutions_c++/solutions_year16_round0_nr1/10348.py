#include<bits/stdc++.h>
using namespace std;
int main()
{
     freopen("A-large.in","r",stdin);
     freopen("output.txt","w",stdout);
     long long int t,p,n,i,j,k=0,x;
	 scanf("%lld",&t);
	while(t--)
	{
		scanf("%lld",&n);
		if(n==0)
		printf("case #%lld: INSOMNIA\n",++k);
		else
		{
		long long int arr[10]={0};
		for(i=1;i<=100;i++)
		{
			x=n*i;
			while(x>0)
			{
				p=x%10;
				arr[p]=1;
				x=x/10;
			}
			for(j=0;j<11;j++)
			{
				if(arr[j]==0)
				break;
			}
			if(j==11)
			break;
		}
		printf("case #%lld: %lld\n",++k,n*i);
	}
	}
}
