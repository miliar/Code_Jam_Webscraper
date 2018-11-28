#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <stdlib.h>

using namespace std;
typedef long long int ll;

int T;

//#define ___IN___ cin
//#define ___OUT___ cout

ifstream fin;
ofstream fout;
#define ___IN___ fin
#define ___OUT___ fout



void solve(int testNum, string& input) {
    ___OUT___ << "Case #" << testNum << ": ";
    
    string sRes;
    char front = 'Z'+1;
    
    string::iterator it = input.begin();
    
    for( ; it!=input.end(); ++it ) {
        if( *it < front ) {
            sRes.append( 1, *it );
        } else {
            sRes.insert( 0, 1, *it );
        }
        front = sRes.front();
    }
    
    ___OUT___ << sRes << endl;
}


int main(int argc, char** argv) {
        if( argc != 3 ) {
            cout << "usage:exe in out" << endl;
        }
        string infile=argv[1];
        fin.open(infile, std::ios::in);
    
        string outfile=argv[2];
        fout.open(outfile, std::ios::out);
    
    // The first line of the input gives the number of test cases, T.
    //cin >> T;
    ___IN___ >> T;
    // T test cases follow.
    int t=0;
    string inputLine;
    while( T-- ) {
        ___IN___ >> inputLine;
        solve(++t, inputLine);
    }
        fin.close();
        fout.close();
    cout << "end" << endl;
    return 0;
}


