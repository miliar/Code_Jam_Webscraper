#include <bits/stdc++.h>
using namespace std;

#define N 10
typedef long long ll;

bool b[N];
void updateDigits(long long n, int & c);

long long solve(long long & n)
{
	int count = 0;
	for (int i = 0; i < N; ++i)
		b[i] = 0;
	ll ans = 0;
	while(count!=N)
	{
		ans += n;
		updateDigits(ans,count);
	}
	return ans;
}

void updateDigits(long long n, int & c)
{
	while(n!=0){
		if(!b[n%10]){
			b[n%10] = 1;
			c++;
		}
		n /=10;
	}
}


int main()
{
	int t;
	long long n,ans; 
	scanf("%d",&t);
	for (int i = 1; i <= t; ++i)
	{
		scanf("%lld",&n);
		if(n!=0)
			printf("Case #%d: %lld\n",i,solve(n));
		else
			 printf("Case #%d: INSOMNIA\n",i);
	}
}