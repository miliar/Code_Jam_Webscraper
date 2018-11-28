#include<bits/stdc++.h>
using namespace std;

int main()
{
	long long n,t,i,j,k,temp;
	scanf("%lld",&t);
	for(j=1;j<=t;j++)
	{
		set<long long> myset;
		scanf("%lld",&n);
		printf("Case #%lld: ",j);
		if(n==0)
		{
			printf("INSOMNIA\n");
			continue;
		}
		i=1;
		while(myset.size()!=10)
		{
			temp=n*i;
			while(temp!=0)
			{
				k=temp%10;
				temp=temp/10;
				myset.insert(k);
			}
			i++;
		}
		printf("%lld\n",n*(i-1));
	}

	return 0;
}
