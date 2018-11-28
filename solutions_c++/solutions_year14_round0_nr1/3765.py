#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;
vector < int > v;
int f ( bool c )
{
	if ( !c ) v.clear();
	int a, b;
	scanf ( "%d", &a );
	for ( int i = 1; i <= 4; i ++ )
		for ( int j = 1; j <= 4; j ++ )
		{
			scanf ( "%d", &b );
			if ( i == a ) v.push_back ( b );
		}
	int ans = -1;
	if ( c )
	{
		sort ( v.begin(), v.end() );
		for ( int i = 1; i < v.size() and ans; i ++ )
		{
			if ( v[i] == v[i - 1] ) 
			{
				if ( ans > 0 ) ans = 0;
				else ans = v[i];
			}
		}
		return ans;
	}
	else return f(1);
}
int main ()
{
	int t;
	scanf ( "%d", &t );
	for ( int i = 1; i <= t; i ++ )
	{
		printf ( "Case #%d: ", i );
		int p = f (0);
		if ( p < 0 ) puts ( "Volunteer cheated!" );
		if ( p == 0 ) puts ( "Bad magician!" );
		if ( p > 0 ) printf ( "%d\n", p );
	}
}