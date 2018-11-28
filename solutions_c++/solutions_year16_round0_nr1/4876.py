/*Counting Sheep*/
#include<bits/stdc++.h>
using namespace std;
#define INF 4294967296
bitset<10> arr;
void digit(long long int n)
{
	while(n>0)
	{
		arr[n%10]=1;
		n/=10;
	}
}
int main()
{
	int t;
	long long int n;
	scanf("%d",&t);
	for(int test=1;test<=t;++test)
	{
		arr.reset();
		scanf("%lld",&n);
		if(n==0)
		{
			printf("Case #%d: INSOMNIA\n",test);
			continue;
		}	
		digit(n);
		long long int i=2*n;
		for(;i<INF;i=i+n)
		{
			if(arr.count()!=10)
			{
				digit(i);
			}
			else
				break;
		}
		printf("Case #%d: %lld\n",test,i-n);
			
	}	
	return 0;
}
