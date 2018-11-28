#include <cstdio>

int main()
{
    int T = 0;
    int N = 0;
    scanf( "%d", &T );
    for ( int t = 1; t <= T; ++t )
    {
        scanf( "%d", &N );
        if ( N == 0 )
        {
            printf( "Case #%d: INSOMNIA\n", t );
            continue;
        }
        bool digits[10]={0,0,0,0,0,0,0,0,0,0};
        int number = 0;
        while ( true )
        {
            number += N;
            int h = number;
            while( h > 0 )
            {
                digits[h%10] = true;
                h /= 10;
            }
            int sum = 0;
            for ( int i = 0; i < 10; ++i )
            {
                sum += digits[i];
            }
            if ( sum == 10 )
            {
                printf( "Case #%d: %d\n", t, number );
                break;
            }
        }
    }
}
