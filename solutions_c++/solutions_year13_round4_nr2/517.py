#include <cstdio>
#include <iostream>

using namespace std;
int N;

long long worst (long long x){
    int T = N;
    long long c = 2;
    long long res = 0;
    while ( c - 1 <= x ){
        res |= ( 1LL << (--T));
        c <<= 1;
    }
//    cout << x << " " << c << " " << res << endl;
    return res + 1;
}

long long lowest ( int N, long long P ){
    ::N = N;
    long long l = 0, r = ( 1LL << N );
    while ( l + 1 < r ){
        long long mid = ( l + r ) / 2;
//    cout << l << " " << r << endl;

        if ( worst ( mid ) > P )
            r = mid;
        else l = mid;
    }

    while ( worst ( l ) <= P && l < ( 1LL << N ) )
            ++l;

    return l - 1;
}

long long best ( long long x ){
    return ( 1LL << N ) + 1 - worst ( ( 1LL << N ) - x - 1 );
}

long long uppest( int N, long long P ){
    ::N = N;
    long long l = 0, r = ( 1LL << N );

    while ( l + 1 < r ){
        long long mid = ( l + r ) / 2;

        if ( best ( mid ) > P )
            r = mid;
        else l = mid;
    }

    while ( best ( l ) <= P && l < ( 1LL << N ) )
            ++l;

    return l - 1;
}

void solve(int test){
    int N;
    long long P;

    cin >> N >> P;
    long long t1 = lowest ( N, P ), t2;
    t2 = uppest ( N, P );
    printf ( "Case #%d: %lld %lld\n", test, t1, t2 );
}

int main(){
    int tests;

    cin>> tests;

    for ( int i = 1; i <= tests; ++i )
        solve(i);
}
