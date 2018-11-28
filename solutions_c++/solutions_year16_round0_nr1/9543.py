#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;



int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T, N;
    scanf("%d", &T);
    int c = 1;
    int br[10];
    while( c <= T )
    {
        scanf("%d", &N);
        if( N == 0 )
            printf("Case #%d: INSOMNIA\n", c);
        else
        {
            memset(br, 0, sizeof(br));
            int cnt = 0;

            int i = 1;
            while( cnt < 10 )
            {
                int N1 = N*i;
                while( N1 > 0 )
                {
                    int r = N1%10;
                    br[r]++;
                    N1 /= 10;
                }
                cnt = 0;
                for( int j = 0; j < 10; j++ )
                    if( br[j] )
                        cnt++;
                i++;
            }
            i--;
            printf("Case #%d: %d\n", c, i*N);
        }

        c++;
    }

    return 0;
}
