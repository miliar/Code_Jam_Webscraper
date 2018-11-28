#include<stdio.h>
#include<iostream>
using namespace std;

#define sc scanf
#define sc1(a) scanf( "%d", &a )
#define pr printf
#define pr1(a) printf( "%ld\n", a )
#define fr( i, n ) for( __typeof(n) i=0; i<n; i++ )
#define rv( i, n ) for( __typeof(n) i=n-1; i>=0; i-- )
#define fo( i, m, n ) for( __typeof(n) i=m; i<=n; i++ )
#define ms( a, val ) memset( a, val, sizeof(a) )
#define re return

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);

    int i, j, k, x, a[4], b[4], t, p, q;

    scanf("%d", &t);

    for( i = 1; i <= t; i++ )
    {
        sc1(x);
        fr( j, 4 )
        {
            if( j == x-1 )
            {
                fr( k, 4 )
                sc1(a[k]);
            }
            else
            {
                fr( k, 4 )
                sc1(p);
            }
        }
        sc1(x);
        fr( j, 4 )
        {
            if( j == x-1 )
            {
                fr( k, 4 )
                sc1(b[k]);
            }
            else
            {
                fr( k, 4 )
                sc1(p);
            }
        }
        p = 0;
        fr( j, 4 )
        {
            fr( k, 4 )
            {
                if( a[j] == b[k] )
                {
                    x = a[j];
                    p++;
                    if( p>1 )   break;
                }
            }

        }
        if( !p )
            pr( "Case #%d: Volunteer cheated!\n", i );
        else if( p == 1 )
            pr( "Case #%d: %d\n", i, x );
        else
            pr( "Case #%d: Bad magician!\n", i );
    }
    return 0;
}
