#include <cstdio>
#include <algorithm>

using namespace std;

int T;
double curr_rate = 2;
double time[100000];
double c, f, x, ans = 10000000000;

void get_time(){
    for( int i = 1; i < 100000; ++i ){
        time[i] = time[i - 1] + c / curr_rate;
        curr_rate += f;
    }
}

int main( void ){

    scanf( "%d", &T );

    for( int k = 0; k < T; ++k ){

        ans = 10000000000;
        curr_rate = 2;

        scanf( "%lf %lf %lf", &c, &f, &x );

        get_time();

        //for( int i = 0; i < 10; ++i ) printf( "%lf\n", time[i] );

        for( int i = 0; i < 100000; ++i ){
            ans = min( ans, time[i] + x / ( 2 + i * f ) );
        }

        printf( "Case #%d: %.7lf\n", k + 1, ans );
    }

    return 0;
}
