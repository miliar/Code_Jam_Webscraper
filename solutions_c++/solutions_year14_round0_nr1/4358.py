#include <string>
#include <vector>
#include <map>
#include <fstream>
#include <algorithm>
#include <deque>

using namespace std ;

int main(){
    ifstream in( "C:\\gjam\\p1s.txt", ios::in ) ;
    ofstream out( "C:\\gjam\\p1s_out.txt", ios::out ) ;
    int tests ; in >> tests ;
    for ( int test = 0 ; test < tests ; ++test ){
        vector< int > versions ;
        int guess1 ; in >> guess1 ;
        map< int, int > n2g ;
        for ( int row = 1 ; row <= 4 ; ++row ){
                for ( int col = 1 ; col <= 4 ; ++col ){
                        int num ; in >> num ;
                        if ( row == guess1 ) {
                                n2g[ num ] = 1 ;
                        }
                }
        }
        int guess2 ; in >> guess2 ;
        for ( int row = 1 ; row <= 4 ; ++row ){
                for ( int col = 1 ; col <= 4 ; ++col ){
                        int num ; in >> num ;
                        if ( row == guess2 ) {
                                if ( n2g.find( num ) != n2g.end() ){
                                        versions.push_back( num ) ;
                                }
                        }
                }
        }
        out << "Case #" << test + 1 << ": " ;
        if ( versions.size() == 0 ){
            out << "Volunteer cheated!" ;
        } else if ( versions.size() == 1 ){
            out << versions[ 0 ] ;
        } else {
            out << "Bad magician!" ;
        }
        out << "\n" ;
    }
    return 0 ;
}












