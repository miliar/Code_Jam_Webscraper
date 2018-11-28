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
    ifstream in( "C:\\gjam\\p2l.txt", ios::in ) ;
    ofstream out( "C:\\gjam\\p2l_out.txt", ios::out ) ;
    out << setprecision( 10 ) ;
    int tests ; in >> tests ;
    for ( int test = 0 ; test < tests ; ++test ){
        double P = 2.0, C, F, X ; in >> C >> F >> X ;
        double tTotal = 0.0 ;
        while ( true ) {
            double tNext = C / P, tCut = X / P, tAftercut = X / ( P + F ) ;
            if ( tNext + tAftercut >= tCut ){
                    tTotal += tCut ;
                    break ;
            } else {
                tTotal += tNext ;
                P += F ;
            }
        }
        out << "Case #" << test + 1 << ": " << tTotal << "\n" ;
    }
    return 0 ;
}












