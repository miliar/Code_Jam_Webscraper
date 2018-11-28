#include <stdio.h>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	scanf("%d", &T);
	for( int t=1; t<=T; t++ )
	{
		int n;
		double a[1005], b[1005];
		scanf("%d", &n);
		for( int i=0; i<n; i++ )
			scanf("%lf", &a[i]);
		for( int i=0; i<n; i++ )
			scanf("%lf", &b[i]);
		sort(a, a+n);
		sort(b, b+n);
		int x = 0, y = 0;
		int an = n, bn = n;
		int s1 = 0;
		while( x<an && y<bn )
		{
			if ( a[x] < b[y] ) { x++; bn--; }
			else { s1++; x++; y++; }
		}
		x = y = 0;
		int s2 = n;
		while( x<n && y<n )
		{
			if ( a[x] < b[y] ) { x++; y++; s2--; }
			else { y++; }
		}
//		int s2 = s1 / 2;
		printf("Case #%d: %d %d\n", t, s1, s2);
	}
	return 0;
}

