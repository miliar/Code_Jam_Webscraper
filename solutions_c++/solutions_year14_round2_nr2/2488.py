#include <cstdio>

using namespace std;

int A, B, K;

void solve( int test ){

    scanf( "%d%d%d", &A, &B, &K );

    int sol = 0;

    for( int i = 0; i < A; ++i ){
        for( int j = 0; j < B; ++j ){
            if( (i & j) < K ) ++sol;
        }
    }

    printf( "Case #%d: %d\n", test, sol );

}

int main( void ){

    int T; scanf( "%d", &T );

    for( int i = 0; i < T; ++i ) solve( i + 1 );

    return 0;
}
