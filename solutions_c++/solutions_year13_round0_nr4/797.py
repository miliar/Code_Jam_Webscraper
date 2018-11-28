#include <iostream>
#include <vector>
#include <cstring>
#include <map>
using namespace std;

int N, K;
vector<int> initkeys;
vector< vector<int> > chest;
vector< int > opener;

int cache[1<<20];
int goal;
int solve( int state ) {
        // cout << __builtin_popcount( state ) << " " << state << endl;
        if( state == goal ) {
                return ( cache[state] = 500 );
        }

        map< int, int > keys;

        for( int i = 0 ; i < initkeys.size() ; ++i ) keys[ initkeys[i] ]++;

        for( int i = 0 ; i < N ; ++i ) if( (state>>i)&1 ) {
                keys[ opener[i] ]--;
                for( int j = 0 ; j < chest[i].size() ; ++j ) keys[ chest[i][j] ]++;
        }

        int &ret = cache[state];
        if( ret != -1 ) return ret;
        ret = -2;

        for( int i = 0 ; i < N ; ++i ) {
                if( (state>>i)&1 ) continue;
                if( keys[opener[i]] <= 0 ) continue;
                ret = i;
                int next = solve( state | (1<<i) );
                if( next != -2 ) {
                        break;
                }
                ret = -2;
        }

        return ret;
}

int main() {
        int ncase;
        cin >> ncase;

        for( int caseno = 1 ; caseno <= ncase ; ++caseno ) {
                cin >> K >> N;
                initkeys.clear();
                initkeys.resize( K );
                for( int i = 0 ; i < K ; ++i ) cin >> initkeys[i];

                chest.clear();
                chest.resize( N );
                opener.clear();
                opener.resize( N );
                for( int i = 0 ; i < N ; ++i ) {
                        cin >> opener[i];
                        int nkeys;
                        cin >> nkeys;
                        chest[i].resize( nkeys );
                        for( int j = 0 ; j < nkeys ; ++j ) {
                                cin >> chest[i][j];
                        }
                }
                memset( cache, -1, sizeof cache );
                goal = (1<<N)-1;
                int ret = solve( 0 );
                cout << "Case #" << caseno << ": ";

                // for( int i = 0 ; i <= goal ; ++i ) cout << cache[i] << " "; cout << endl;
                if( ret == -2 ) cout << "IMPOSSIBLE";
                else {
                        int next = 0;
                        while( next != goal ) {
                                cout << cache[next]+1 << " ";
                                next |= (1<<cache[next]);
                        }
                }
                cout << endl;
        }
}
