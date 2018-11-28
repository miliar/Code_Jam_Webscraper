#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <stdlib.h>

using namespace std;
typedef long long int ll;

int T;


int main(int argc, char** argv) {
    if( argc != 3 ) {
        cout << "usage:exe in out" << endl;
    }
    ifstream fin;
    string infile=argv[1];
    fin.open(infile, std::ios::in);
    
    ofstream fout;
    string outfile=argv[2];
    fout.open(outfile, std::ios::out);
    
    // The first line of the input gives the number of test cases, T.
    //cin >> T;
    fin >> T;
    // T test cases follow.
    // Each consists of one line with a single number N, the number Bleatrix has chosen.
    int t=0;
    bool ok[11];
    while( T-- ) {
        t++;
        set<ll> used;
        bool bEnd = false;
        memset( ok, 0x00, sizeof(ok) );
        string strN;
        //cin >> strN;
        fin >> strN;
        
        string tmpN=strN;
        ll trycnt=0;
        while(true) {
            trycnt++;
            for( char i='0'; i<='9'; i++ ) {
                if( !ok[i-'0'] ) {
                    if( string::npos != tmpN.find( i ) ) {
                        ok[i-'0'] = true;
                        continue;
                    }
                }
            }
            bEnd = true;
            for( int i=0;i<=9;i++) {
                if( !ok[i] ) {
                    bEnd = false;
                    break;
                }
            }
            if( bEnd ) {
//                cout << "Case #" << t << ": " << atoll(tmpN.c_str()) << endl;
                fout << "Case #" << t << ": " << atoll(tmpN.c_str()) << endl;
                break;
            }
            // go to next
            ll next = trycnt*atoll(strN.c_str());
            if( used.find(next) != used.end() ) {
//                cout << "Case #" << t << ": " << "INSOMNIA" << endl;
                fout << "Case #" << t << ": " << "INSOMNIA" << endl;
                break;
            }
            used.insert(atoll(tmpN.c_str()));
            tmpN = to_string(next);
            //cout << tmpN << endl;
        }
    }
    fin.close();
    fout.close();
    //cout << "end" << endl;
    return 0;
}


