#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

typedef int ll;

int main ( void )
{
    ll T; cin >> T; 
    string line; getline( cin, line );
    for ( ll t = 0; t < T; ++t ) {
        ll K; char c;
        bool impossible = false; ll result = 0;
        vector<bool> v;
        
        getline( cin, line );
        istringstream iss( line );
        
        while ( iss.get(c) && c != ' ' ) {
            v.push_back( c == '+' );
        }
        iss >> K;
        
        for ( ll l = 0; l <= v.size() - K; ++l ) {
            if ( !v[ l ] ) {
                result += 1;
                for ( ll k = 0; k < K; ++k ) {
                    v[ l + k ] = !v[ l + k ];
                }
            }
        }
        
        for ( ll l = 0; l < v.size(); ++l )
            if ( !v[ l ] ) {
                impossible = true;
                break;
            }
        
        if ( !impossible ) {
            cout << "Case #" << (t + 1) << ": " << result << endl;
        } else {
            cout << "Case #" << (t + 1) << ": IMPOSSIBLE" << endl;
        }
    }
    
}