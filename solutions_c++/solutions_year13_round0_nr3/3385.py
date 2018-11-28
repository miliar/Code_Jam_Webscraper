#include<cstdio>
#include<cstring>
#include<cmath>
using namespace std;
int a[1001];
int b[1001];
int c[10];
int main()
{
	a[0] = 0;
	b[0] = 0;
	for ( int i = 1; i <= 1000; i++ )
	{
		if ( i == 1 )
		{
			a[i] = 1;
			b[i] = 1;
		}
		else
		{
			int j = i;
			c[0] = 0;
			while ( j != 0 )
			{
				c[++c[0]] = j % 10;
				j /= 10;
			}
			bool u = true;
			for ( j = 1; j <= c[0]; j++ )
			if ( c[j] != c[c[0]-j+1] ) u = false;
			if ( u )
			{
				a[i] = 1;
				j = sqrt(i);
				if ( j * j == i )
				if ( a[j] == 1 )
				b[i] = 1;	
			}
		}
	}
	a[0] = 0;
	for ( int i = 1; i <= 1000; i++ )
		if ( b[i] ) a[i] = a[i-1] + 1;
		else a[i] = a[i-1];
	int cas;
	int ca = 0;
	scanf( "%d", &cas );
	while ( cas-- )
	{
		int l,r;		
		scanf( "%d%d", &l, &r );
		printf("Case #%d: ",++ca);
		printf("%d\n",a[r] - a[l-1] );
	}
	return 0;
}
