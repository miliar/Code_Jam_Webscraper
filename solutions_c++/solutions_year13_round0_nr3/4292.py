#include<cstdio>
#include<vector>
using namespace std;
vector < long long > v;
long long x [] = { 1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004 };
bool pal ( long long a )
{
	vector < long long > z;
	long long c = a, d = a;
	while ( c )
	{
		z.push_back ( c % 10 );
		c /= 10;
	}
	while ( a >= 10 )
	{
		if ( a % 10 != z.back() ) return 0;
		z.pop_back();
		a /= 10;
	}
// 	printf ( "%lld ", d );
	return 1;
}
void don ()
{
	for ( long long i = 1; i <= 10000000; i ++ )
 	{
		if ( pal ( i ) and pal ( i * i ) ) 
		{
			v.push_back ( i * i );	
			printf ( "%lld, ", i * i );
		}
	}
}
int main ()
{
/*
	printf ( "int x [] = { " );
	don ();
	puts ( " } " );
	printf ( "%d", v.size() );
*/	
	int t;
	scanf ( "%d", &t );
	for ( int i = 1; i <= t; i ++ )
	{
		printf ( "Case #%d: ", i );
		long long a, b;
		scanf ( "%lld %lld", &a, &b );
		
		int w = 0;
		for ( int k = 0; k < 39 and x[k] <= b; k ++ ) if ( x[k] >= a ) w ++;
		
		printf ( "%d\n", w );
	}
	return 0;
}