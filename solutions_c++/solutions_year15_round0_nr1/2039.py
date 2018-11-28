#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
using namespace std;

ifstream fin ("in.in");
ofstream fout ("out.txt");
int main () {
    int t; fin >> t; int oldt = t;
    while( t-- ) {
        int smax; fin >> smax;
        string s;
        fin >> s;
        int publike = 0;
        for ( int i = 0; i < s.size(); i++ ) {
            publike += s[ i ] - '0';
        }
        int diglo = 0;
        for ( int i = 0; i < s.size(); i++ ) {
            if ( i > diglo ) {
                diglo = i;
            }
            diglo += s[ i ] - '0';
        }
        fout << "Case #" << oldt - t << ": " << max ( 0, diglo - publike ) << endl;
    }
    return 0;
}
