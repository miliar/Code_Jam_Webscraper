#include <cstdio>

const int MAXS = 2000;

int main()
{
    int T, S;
    char str[MAXS];

    scanf( "%d", &T );

    for ( int t = 1; t <= T; t++ )
    {
        int counter = 0, total = 0;
        scanf( "%d %s", &S, str );

        for ( int i = 0; i <= S; i++ )
        {
            if ( str[i] != '0' and i > total )
            {
                counter += ( i - total );
                total   += ( i - total );
            }
            total += str[i] - '0';
        }

        printf( "Case #%d: %d\n", t, counter );
    }

    return 0;
}
