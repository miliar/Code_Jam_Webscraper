#include <bits/stdc++.h>
using namespace std;

#define two(x) (1<<(x))
int mark[1<<25], pr[1<<23], k;

void sieve()
{
	for( int i = 2 ; i * i < two(25) ; i ++ )
		if( !mark[i] )
			for( int j = i*i ; j < two(25) ; j += i )
				mark[j] = 1;
	pr[k++] = 2;
	for( int i = 3 ; i < two(25) ; i += 2 )
		if( !mark[i] )
			pr[k++] = i;
}
int isprime( long long a, int out )
{
	if( a == 1 )
		return 0;
	for( int i = 0 ; i < k && pr[i] * 1ll * pr[i] <= a ; i ++ )
		if( a % pr[i] == 0 )
		{
			if( out )
				// cout << a << " " << pr[i] << endl;
				cout << " " << pr[i];
			return 0;
		}
	return 1;
}
int ok( int x, int out = 0 )
{
	for( int b = 2 ; b < 11 ; b ++ )
	{
		long long cur = 0, p = 1;
		int xx = x;
		while( xx )
		{
			cur += (xx%2) * p;
			p *= b;
			xx /= 2;
		}
		if( isprime( cur, out ) )
			return 0;
	}
	return 1;
}
void show( int x )
{
	string r = "";
	while( x )
	{
		r += char('0'+x%2);
		x /= 2;
	}
	reverse( r.begin(), r.end() );
	cout << r;
}

int main()
{
	sieve();
	int t, cc = 0;
	cin >> t;
	while( t -- )
	{
		int n, J;
		cin >> n >> J;
		vector < int > ans;
		for( int i = two(15)+1 ; i < two(n) && ans.size() < J ; i += 2 )
			if( ok(i) )
				ans.push_back(i);
		cout << "Case #" << ++cc << ":" << endl;
		for( int i = 0 ; i < ans.size() ; i ++ )
		{
			show( ans[i] );
			ok( ans[i], 1 );
			cout << endl;
		}
	}
	return 0;
}
