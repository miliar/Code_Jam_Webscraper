#include <string>
#include <vector>
#include <map>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <deque>
#include <iomanip>

using namespace std ;

int main(){
    ifstream in( "C:\\gjam\\p4l.txt", ios::in ) ;
    ofstream out( "C:\\gjam\\p4l_out.txt", ios::out ) ;
    int tests ; in >> tests ;
    for ( int test = 0 ; test < tests ; ++test ){
        int N ; in >> N ;
        vector< double > nao( N ), ken( N ) ;
        for ( int i = 0 ; i < N ; ++i ){
            in >> nao[ i ] ;
        }
        for ( int i = 0 ; i < N ; ++i ){
            in >> ken[ i ] ;
        }
        sort( nao.begin(), nao.end() ) ;
        sort( ken.begin(), ken.end() ) ;
        int dw = 0, depth = 0 ;
        for ( int inao = 0, iken = 0 ; inao < N && iken < N ; ){
                if ( nao[ inao ] < ken[ iken ] ){
                        if ( depth == 0 ) {
                                dw += 1 ;
                        }
                        depth = max( 0, depth - 1 ) ;
                        inao += 1 ;
                } else {
                        depth += 1 ;
                        iken += 1 ;
                }
        }
        dw = N - dw ;
        depth = 0 ;
        int w = 0 ;
        for ( int inao = N - 1, iken = N - 1 ; ( inao >= 0 ) && ( iken >= 0 ) ; ){
                if ( nao[ inao ] > ken[ iken ] ){
                        //cout << nao[ inao ] << " nao " << depth << "\n" ;
                        if ( depth == 0 ){
                                w += 1 ;
                        }
                        depth = max( 0, depth - 1 ) ;
                        --inao ;
                } else {
                        // cout << ken[ iken ] << " " << iken << " ken\n" ;
                        depth += 1 ;
                        --iken ;
                }

        }
        w = ( w < 0 ) ? 0 : w ;
        out << "Case #" << test + 1 << ": " << dw << " " << w << "\n" ;
    }
    return 0 ;
}












