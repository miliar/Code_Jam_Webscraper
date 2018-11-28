#include <iostream>
#include <algorithm>
#include <cstdlib>
using namespace std;
long long test = 0;
long long chk[11];
inline void cc(long long n)
{
	long long t = 1;
	while(t<=n) t *= 10;
	t /= 10;
	while(t>0)
	{
		chk[n/t] = 1;
		n %= t;
		t /= 10;
	}
	return;
}
inline bool ccc()
{
	for( int i = 0 ; i <= 9 ; i++ )
	{
		if(chk[i]==0)
			return false;
	}
	return true;
}
void solve()
{
	test++;
	memset(chk,0,sizeof(chk));
	long long n; cin >> n;
	if( n == 0 )
	{
		cout << "Case #" << test << ": INSOMNIA" << endl;
		return;
	}
	cc(n);
	long long ii = 2;
	long long nn = n;
	while(ccc()!=true)
	{
		n = nn*ii;
		ii++;
		cc(n);
	}
	cout << "Case #" << test << ": " << n << endl;
	return;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t;
	cin >> t;
	while(t--)
	{
		solve();
	}
	return 0;
}