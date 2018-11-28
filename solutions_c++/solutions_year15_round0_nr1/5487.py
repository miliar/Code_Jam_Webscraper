#include<iostream>
using namespace std;
#include<stdio.h>
#include<algorithm>
#include<vector>
#include<queue>
#include<utility>
#include<stack>
#include<map>
#include<set>
#include<string.h>
#include<math.h>
#define MOD 1000000007
#define MIN -100000000
#define MAX 100000000
#define ll long long int
/* HOPE n WILL :)
	NGU :)
	_/\_ 	*/
// MG

char a[1005];

int main()
{
	ll n,i,t,k=1,sum,temp,ans;
	scanf("%lld",&t);
	while(t--)
	{
		sum=ans=0;
		scanf("%lld",&n);
		scanf("%s",a);
		for(i=0;i<=n;i++)
		{
			temp=a[i]-'0';
			if(sum<i)
				{
					ans=ans+i-sum;
					sum=i;
				}
			sum=sum+a[i]-'0';	
		}
	printf("Case #%lld: %lld\n",k,ans);
	k++;
	}
	return 0;
}