#include <cstdio>
#include <iostream>
#include <string.h>
using namespace std;

int m[100];
int nil[100];


int counter = 0;

int getablebyadd( int a, int *m, int size )
{
	int i;
	int r = 0;
	for( i = 0; i < size; i ++ )
	{
		if( m[i] == 0 )
			continue;
		if( m[i] < a + a - 1 )
			r ++;
	}
	return r;
}

int absorbable( int a, int *m, int size, int depth )
{
	int m2[100] = {0,};
	int i;
	int r = 0;

	memcpy( m2, m, sizeof(int) * size );

	for( i = 0; i < depth; i ++ )
		a += a - 1;

	for( i = 0; i < size; i ++ )
	{
		if( m2[i] != 0 && m2[i] < a )
		{
			a += m2[i];
			m2[i] = 0;
			r ++;
			i = -1;
		}
	}

	return r;
}

int countleft( int *m, int size )
{
	int i;
	int count = 0;
	for( i = 0; i < size; i ++ )
		if( m[i] != 0 )
			count ++;
	return count;
}

void deletemax( int *m, int size )
{
	int maxind = 0;
	int i;
	for( i = 1; i < size; i ++ )
	{
		if( m[i] > m[maxind] )
			maxind = i;
	}
	m[maxind] = 0;
}

void make() {
	int i;
	int k;
	int r = 0;
	printf("Case #%d: ", ++counter);

	int a, n; scanf("%d %d", &a, &n);
	memset( m, 0, sizeof(m) );
	memset( nil, 0, sizeof(nil) );
	for (i=0; i<n; ++i) {
		scanf("%d", &m[i]);
	}

	if( a == 1 )
		r = n;
	else
	{
		while( true )
		{
			// absorb all smaller motes
			for( i = 0; i < n; i ++ )
			{
				if( m[i] == 0 )
					continue;

				if( m[i] < a )
				{
					a += m[i];
					m[i] = 0;
					// startover
					i = -1;
				}
			}
			for( i = 0; i < n; i ++ )
			{
				if( m[i] != 0 )
				{
					if( getablebyadd( a, m, n ) > 0 )
					{
						// add mot
						a += a - 1;
						r ++;
						break;
					}
					else
					{
						int left = countleft( m, n );
						for( k = 1; k < left; k ++ )
						{
							if( absorbable( a, m, n, k ) >= k )
								break;
						}
						if( k < left )
						{
							// add mot
							a += a - 1;
							r ++;
							break;
						}
						else
						{
							// remove mot
							deletemax( m, n );
							r ++;
							break;
						}
					}
				}
			}
			// check fin
			if( memcmp( m, nil, sizeof(m) ) == 0 )
				break;
		}
	}

	printf("%d\n", r<n?r:n );
	return;
}

int main() {
	int t; scanf("%d", &t);
	while(t--) {
		make();
	}
	return 0;
}
