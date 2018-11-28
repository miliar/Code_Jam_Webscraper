#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>

using namespace std;

long long N;
int counter = 0;
int table[10];

void init(){

    counter = 0;
    for(int i=0;i<10;i++){
        table[i] = 0;
    }

}

long long solve(){

    long long num = N;
    while( counter < 10 ){

        long long tmp = num;
        while( tmp ){
            int digit = tmp % 10;
            tmp /= 10;

            if( !table[digit] ){
                table[digit]++;
                counter++;
            }
        }

        if( counter < 10 )
            num += N;

    }
    return num;
}


int main(){

    int T; scanf( "%d", &T );
    for(int t=1;t<=T;t++){
        scanf( "%lld", &N );
        init();
        if( N )
            printf( "Case #%d: %lld\n", t, solve() );
        else
            printf( "Case #%d: INSOMNIA\n", t );
    }

}
