#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
#include<math.h>
#include<vector>
using namespace std;
const int N = 1000;
char line[N];
double total;
int n;

bool hash[1<<22];
double rec[1<<22];

void dp ( int s , int c ) {
    if ( hash[s] ) return;
    rec[s] = 0.0;
    for ( int i = 0;i < n;++i ) {
        int j = i, pay = n;
        do {
            if ( line[j] == '.' && ( s & ( 1 << j ) ) == 0 ) {
                int t = ( s | ( 1 << j ) );
                //printf ( "(%d) -> (%d) + %d\n", s, t, pay );
                dp ( t , c - 1 );
                rec[s] += rec [t] + pay * pow ( n, c - 1 );
                break;
            }
            --pay;
            j = ( j + 1 ) % n;
        } while ( j != i );
    }
    //printf ( "rec[%d] = %f\n", s, rec[s] );
    hash[s] = true;
    return;
}

void solve() {
    scanf ( "%s", line );
    n = strlen ( line ), total = 0.0;
    memset ( hash, false, sizeof ( hash ) );
    int t = 0;
    for ( int i = 0;i < n;++i )
        if ( line[i] == '.' )
            ++t;
    dp ( 0, t );
    double total = rec[0];
    //dfs ( 0, 0 );
    //printf ( "%f\n", total );
    for ( int i = 0;i < n;++i )
        if ( line[i] == '.' )
            total /= n;
    printf ( "%.12f\n", total );
    //exit ( -1 );
    return;
}

int main() {
    int T;
    scanf ( "%d", &T );
    for ( int t = 1;t <= T;++t ) {
        printf ( "Case #%d: ", t );
        solve();
    }
}