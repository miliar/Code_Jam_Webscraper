#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;
typedef long long ll;
int test=1;
ll dp[22];
void solve()
{
	ll n;
	cin >> n;
	ll res = 0;
	if(n<=20)
	{
		cout << "Case #" << test++ << ": " << n << endl;
		return;
	}
	int p;
	for( p=1 ; p <= 15 ; p++ ) 
		if( n % (ll)pow(10,p) == n )
			break;
	ll tt = pow(10,p-1);
	ll ff = 1;
	ll temp = n;
	ll nnn;
	if(p%2) nnn = n%(ll)pow(10,(p/2+1));
	else nnn = n%(ll)pow(10,(p/2));
	ll aa = n - nnn;
	if(nnn==0)
	{
		res++;
		n--;
		for( p=1 ; p <= 15 ; p++ ) 
			if( n % (ll)pow(10,p) == n )
				break;
		tt = pow(10,p-1);
		if(p%2) nnn = n%(ll)pow(10,(p/2+1));
		else nnn = n%(ll)pow(10,(p/2));
		aa = n - nnn;
		temp = n;
	}
	if( aa == tt )
	{
		res += nnn;
	}
	else
	{
		res += nnn;
		for( int i = 0 ; i < p/2 ; i++ )
		{
			res += ff*(temp/tt);
			temp %= tt;
			tt /= 10;
			ff *= 10;
		}
	}
	res += dp[p];
	cout << "Case #" << test++ << ": " << res << endl;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;
	cin >> t;
	dp[1] = 1;
	dp[2] = 10;
	int ii;
	for( int i = 3 ; i <= 14 ; i++ )
	{
		ii = (i-1)/2;
		dp[i] = dp[i-1] + pow(10,i-1-ii) + pow(10,ii)-1;
	}
	while(t--)
	{
		solve();
	}
	return 0;
}