#include <iostream>
#include <cstdlib>
#include <cstdio>

using namespace std;

int gcd( int a, int b )
{
	return (a%b)?gcd(b,a%b):b;
}

int test_2( int n )
{
	int b = 1;
	while ( b < n ) b <<= 1;
	if ( b == n ) return 1;
	else return 0;
}

int deal( int n, int m )
{
	int b = 1,count = 0;
	while ( b*n < m ) {
		b <<= 1;
		count ++;
	}
	return count;
}

int main()
{
	int t,n,m,r,i;
	while ( scanf("%d",&t) != EOF )
	for ( i = 1 ; i <= t ; ++ i ) {
		scanf("%d/%d",&n,&m);
		r = gcd( n, m );
		printf("Case #%d: ",i);
		if ( !test_2( m/r ) ) 
			printf("impossible\n");
		else printf("%d\n",deal(n/r,m/r));
	}
	return 0;
}
