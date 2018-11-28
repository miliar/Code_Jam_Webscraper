#include <cstdio>
#include <cstring>

using namespace std;

int T, K;
int niz[20];

int main( void ){

    scanf( "%d", &T );

    for( int i = 0; i < T; ++i ){
        memset( niz, -1, sizeof niz );

        for( int z = 0; z < 2; ++z ){
            scanf( "%d", &K );

            int x;
            for( int j = 0; j < 4; ++j )
                for( int k = 0; k < 4; ++k ){
                    scanf( "%d", &x );

                    if( j == K - 1 && z == 1 ){
                        if( niz[x] != -1 ) ++niz[x];
                    }
                    if( j == K - 1 && z != 1 ) ++niz[x];
                }
        }

        int cnt = 0, ans;

        for( int j = 1; j <= 16; ++j ){ if( niz[j] == 1 ) ++cnt, ans = j; }

        printf( "Case #%d: ", i + 1 );

        if( cnt == 1 ) printf( "%d\n", ans );
        else if( cnt == 0 ) printf( "Volunteer cheated!\n" );
        else printf( "Bad magician!\n" );
    }

    return 0;
}
