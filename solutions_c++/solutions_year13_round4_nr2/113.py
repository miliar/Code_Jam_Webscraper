#include <vector>
#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <set>
using namespace std;
#define REP(i,n) for(int i=0;i<(n);i++)

typedef long long ll;

int get_best_place(ll n, ll k)
{
	ll better=k-1;
	ll worse=n-k;
	//if can win
	if(worse!=0)
	{
		worse--;
		better=(better+1)/2;
		return get_best_place(n/2,better+1);
	}
	//if cant win
	else
	{
		return n;
	}
}

int get_worst_place(ll n, ll k)
{
	ll better=k-1;
	ll worse=n-k;
	//if can lose
	if(better!=0)
	{
		better--;
		better=(better)/2;
		return get_worst_place(n/2,better+1)+n/2;
	}
	else
		return 1;
}

int main()
{
	int t;
	scanf("%d",&t);
	for(int test=1;test<=t;test++)
	{
		int n;
		ll p;
		scanf("%d%lld",&n,&p);
		int res1=0, res2=0;
		for(int i=1;i<=(1<<n);i++)
		{
			if(get_worst_place(1<<n,i)<=p)
				res1=i-1;
			if(get_best_place(1<<n,i)<=p)
				res2=i-1;
		}
		printf("Case #%d: %d %d\n",test,res1,res2);
	}
	return 0;
}
