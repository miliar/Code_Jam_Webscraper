#include <cstdio>
#include <cstdlib>



void solve( int caseId )
{
    int a,b,k;
    scanf( "%d %d %d\n", & a, & b, &k );

    int cnt = 0;

    for( int i = 0; i < a; i ++ )
    {
        for( int j = 0; j < b; j ++ )
        {
            if( ( i & j ) < k )
                cnt ++;
        }
    }

    printf("Case #%d: %d\n", caseId, cnt );
}

int main( void )
{
    int cases = 0;
    scanf( "%d\n", & cases );

    for( int i = 1; i <= cases; i++ )
        solve( i );


    return EXIT_SUCCESS;
}

