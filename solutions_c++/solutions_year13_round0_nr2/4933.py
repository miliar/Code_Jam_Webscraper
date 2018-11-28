#include <iostream>
#include <vector>

using namespace std;

int n, m;
vector< vector< int > > v;

bool verify_position( int i0, int j0 ) {
    bool resLine = true, resCol = true;
    int x = v[i0][j0];
    for( int i = 0 ; i < n ; i++ ) {
        if( v[i][j0] > x ) {
            resCol = false;
        }
    }
    for( int j = 0 ; j < m ; j++ ) {
        if( v[i0][j] > x ) {
            resLine = false;
        }
    }
    return (resLine or resCol);
}

bool solve_case( void )
{
    bool res = true;
    for( int i = 0 ; i < n ; i++ ) {
        for( int j = 0 ; j < m ; j++ ) {
            res = verify_position( i, j ) and res;
        }
    }
    return res;
}

void parse_case( void ) {
    int x;
    cin >> n >> m;
    v.resize( n );
    for( int i = 0 ; i < n ; i++ ) {
        v[i].resize( m );
        for( int j = 0 ; j < m ; j++ ) {
            cin >> x;
            v[i][j] = x;
        }
    }
}

int main( int argc, char *argv[] )
{
    int nCases;
    cin >> nCases;
    for( int t = 1 ; t <= nCases ; t++ ) {
        parse_case();
        cout << "Case #" << t << ": ";
        if( solve_case() ) {
            cout << "YES";
        } else {
            cout << "NO";
        }
        cout << endl;
    }
    return 0;
}
