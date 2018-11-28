#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <fstream>
using namespace std;

ifstream fcin ("in.in");
ofstream fcout ("out.txt");
// i, j , k , 2, 3, 4

int gimme ( char c ) {
    if ( c == 'i' ) return 2;
    else if ( c == 'j' ) return 3;
    return 4;
}

int mnozi ( int a, int b ) {
    int n = -1;
    if ( (a < 0 and b < 0) or ( a > 0 and b > 0 ) ) n = 1;
        if ( abs( a ) == 1 ) {
            if ( abs( b ) == 1 )
                return 1 * n;
            if ( abs( b ) == 2 )
                return 2 * n;
            if ( abs( b ) == 3 )
                return 3 * n;
            if ( abs( b ) == 4 )
                return 4 * n;
        }
        if ( abs( a ) == 2 ) {
            if ( abs( b ) == 1 )
                return 2 * n;
            if ( abs( b ) == 2 )
                return -1 * n;
            if ( abs( b ) == 3 )
                return 4 * n;
            if ( abs( b ) == 4 )
                return -3 * n;
        }
        if ( abs( a ) == 3 ) {
            if ( abs( b ) == 1 )
                return 3 * n;
            if ( abs( b ) == 2 )
                return -4 * n;
            if ( abs( b ) == 3 )
                return -1 * n;
            if ( abs( b ) == 4 )
                return 2 * n;
        }
        else {
            if ( abs( b ) == 1 )
                return 4 * n;
            if ( abs( b ) == 2 )
                return 3 * n;
            if ( abs( b ) == 3 )
                return -2 * n;
            if ( abs( b ) == 4 )
                return -1 * n;
        }


}

int l;
int prefix[ 10005 ][ 10005 ];

void build_prefix( string s ) {
    for ( int start = 0; start < l; start++ ) {
        int umnozak = gimme( s[ start ] );
        prefix[ start ][ start ] = umnozak;
        for ( int j = start + 1; j < l; j++ ) {
            umnozak = mnozi( umnozak, gimme( s[ j ] ) );
            prefix[ start ][ j ] = umnozak;
        }
    }
}
string solve ( string s ) {
    string ret = "NO";
    build_prefix( s );
    for ( int i = 0; i < l - 2; i++ )
    for ( int j = i + 1; j < l - 1; j++ ) {
        if ( prefix[ 0 ][ i ] == 2 and
             prefix[ i + 1 ][ j ] == 3 and
             prefix [ j + 1 ][ l - 1 ] == 4 ) {
                 ret = "YES";
                 break;
             }
    }
    return ret;
}

int main () {
    int t; fcin >> t; int oldt = t;
    while ( t-- ) {
        string ans;
        int x; fcin >> l >> x;
        l *= x;
        string bla;
        fcin >> bla;
        string s;
        for ( int i = 0; i < x; i++ ) s += bla;
        ans = solve( s );
        fcout << "Case #" << oldt - t << ": " << ans << endl;
    }
    return 0;
}
