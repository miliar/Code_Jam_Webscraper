#include <bits/stdc++.h>

using namespace std;
int cal( int n )
{
	if( n == 0 ) return -1;
	int mask = 0;
	int m = n;
	while( mask != ((1 << 10) - 1) )
	{
		int tmp = n;
		while( tmp != 0 )
		{
			int digit = tmp % 10;
			mask |= ( 1 << digit );
			tmp /= 10;
		}
		//cerr << mask << endl;
		n += m;
	}
	return n - m;
}
int main()
{
	//freopen("A-large.in","r",stdin);
	//freopen("A-large.out","w",stdout);
	
	int T;
	int n;
	scanf("%d",&T);
	for( int i = 1 ; i <= T ; i++ )
	{
		scanf( "%d",&n );
		//cerr << n << endl;
		printf( "Case #%d: ", i);
		if( cal(n) == -1 ) printf("INSOMNIA\n");
		else printf( "%d\n" , cal(n) );
	}
	return 0;
}
