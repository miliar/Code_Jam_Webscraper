#include <cstdio>
#include <vector>

using namespace std;

long long int divisor( long long int n ){
    for( long long int i = 2; i * i <= n; i++ ){
        if( n % i == 0 )
            return i;
    }
    return -1;
}

bool check( int n  ){
    
    vector< long long int > divs;

    for( long long int i = 2; i <= 10; i++ ){ 
        long long int num = 0;
        long long int base = 1;
        for( int j = 0; j < 16; j++ ){
            if( ( n & ( 1 << j ) ) != 0 )
                num += base;
            base *= i;
        }
        long long int div = divisor( num );
        if( div != -1 )
            divs.push_back( div );
    }
    if( divs.size() == 9 ){
        for( int i = ( 1 << 15 ); i >= 1; i >>= 1 ){
            if( ( n & i ) != 0 )
                printf( "1" );
            else
                printf( "0" );
        }
        printf( " " );
        for( int i = 0; i < 9; i++ )
            printf( "%d ", divs[ i ] );
        printf( "\n" );
        return true;
    }
    return false;    
}

int main(){

    int j = 50;
    printf( "Case #1:\n" );
    for( int i = ( 1 << 15 ) + 1; i <= ( 1 << 16 ) - 1; i += 2 ){
        if( check( i ) )
            j--;
        if( j == 0 )
            break;
    }
}
