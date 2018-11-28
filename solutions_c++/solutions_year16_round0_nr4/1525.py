#include <iostream>
#include <vector>
#define MAXN 100000
#define INF 1000000000
using namespace std;


long long exp(int a, int b)
{
	if(b==0)
		return 1;
	long long temp = exp(a,b/2);
	if(b%2==0)
		return temp*temp;
	else
		return a*temp*temp;
}


void solve(long long k, long long c, long long s)
{
	if(k==1)
	{
		if(s==0)
			cout<<"IMPOSSIBLE\n";
		else
			cout<<1<<"\n";
		return;
	}
	long long n = k;
	long long ans = 0;
	long long count = 0;
	long long x = 1;
	int temp = 1;
	while(temp != c)
	{
		x = k*x + 1;
		temp++;
	}
	long long y = exp(k,c) - x + 1;
	long long z = exp(k,c-1);
	long long l = 2;
	long long r = n-1;
	
	ans++;
	count++;
	while( l<=n && (l-1)*z + 1 <= x)
	{
		l++;
		count++;
	}
	if(count == n)
	{
		if(ans<=s)
			cout<<x<<"\n";
		else
			cout<<"IMPOSSIBLE\n";
		return;
	}
	ans++;
	count++;
	while(r>=l && r*z >= y)
	{
		r--;
		count++;
	}
	if(count == n)
	{
		if(ans<=s)
			cout<<x<<" "<<y<<"\n";
		else
			cout<<"IMPOSSIBLE\n";
		return;
	}
	if(ans + n - count > s)
		cout<<"IMPOSSIBLE\n";
	else
	{
		cout<<x<<" "<<y<<" ";
		for(long long i=l;i<=r;i++)
			cout<<i*z<<" ";
		cout<<"\n";
	}
}

int main()
{
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		long long k, c, s;
		cin>>k>>c>>s;
		cout<<"Case #"<<t<<": ";
		solve(k, c, s);		
	}
}
