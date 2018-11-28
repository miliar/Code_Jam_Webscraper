#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>

const int MAXS = 110;

using namespace std;

int N;
char S[MAXS];

bool check(){

    for(int i=0;i<N;i++)
        if( S[i] == '-' )
            return false;

    return true;

}

int solve(){

    int counter = 0;
    while( !check() ){

        int pos = N - 1;
        while( S[pos] == '+' )
            pos--;

        for(int i=0;i<=pos;i++){
            if( S[i] == '-' )
                S[i] = '+';
            else
                S[i] = '-';
        }
        counter++;
    }
    return counter;
}

int main(){

    int T; scanf( "%d", &T );
    for(int t=1;t<=T;t++){
        scanf( "%s", S );
        N = strlen( S );
        printf( "Case #%d: %d\n", t, solve() );
    }

}
