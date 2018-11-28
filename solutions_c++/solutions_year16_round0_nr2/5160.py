#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;
typedef unsigned long long ull;

int T;

//#define ___IN___ cin
//#define ___OUT___ cout

ifstream fin;
ofstream fout;
#define ___IN___ fin
#define ___OUT___ fout


void solve(int testNum, string& input) {
    int res = 0;
//    int N=(int)input.size();
    
    char head='+';
    
    while( true ) {
        head = input[0];
        int headSeq = 1;
        bool flip = false;
        for( int i=1; i<input.size(); i++ ) {
            if( head == input[i] ) {
                headSeq++;
            } else {
                flip = true;
                break;
            }
        }

        if( flip ) {
            // flip
            res++;
            int flipPos=headSeq;
            reverse(input.begin(), input.begin() + flipPos);
            for( int j=0; j < flipPos; j++ ) {
                if( input[j] == '+' ) {
                    input[j] = '-';
                } else {
                    input[j] = '+';
                }
            }
            //___OUT___ << input << endl;
        }
        
        if( !flip ) {
            if( head == '-' ) {
                res++;
            }
            break;
        }
    }
    ___OUT___ << "Case #" << testNum << ": " << res << endl;
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
    //cout << "end" << endl;
    return 0;
}


