#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <cmath>
#include <vector>
#include <set>
#include <cstring>
#include <algorithm>

using namespace std;

#define CL(x,v); memset(x,v,sizeof(x));

class FileReader : public ifstream {
public:
    FileReader( const string& filename ) { open( filename.c_str(), ios_base::in ); }
    int readInt() { int x = 0; *this >> x; return x; }
    vector<int> readInts( int n ) { vector<int> v(n); for ( int i = 0; i < n; i++ ) v[i] = readInt(); return v; }
    string readLine() { char buf[20000]; getline( buf, sizeof(buf) ); return buf; }
    string readString() { string x; *this >> x; return x; }
    vector<string> readStrings( int n ) { vector<string> v; for ( int i = 0; i < n; i++ ) v.push_back( readString() ); return v; }
    __int64 readInt64() { __int64 x; *this >> x; return x; }
};

class FileWriter : public ofstream {
public:
    FileWriter( const string& filename ) { open( filename.c_str(), ios_base::out ); }
};

int main() {
    FileReader fin ("A-small-attempt0.in");
    FileWriter fout ("out.txt");

    int caseCount;
    fin >> caseCount;
    fin.readLine();
    for (int cc = 0; cc < caseCount; cc ++ ) {
        __int64 A, m[100];
        int N;
        fin >> A >> N;
        fin.readLine();
        int solved = 0;
        int moves = 0;
        int i;
        for (i = 0; i < N; i ++) fin >> m[i];
        sort (m, m + N);
        /*solve*/
        __int64 now = A;
        for (i = 0; i < N; i ++) {
            if (m[i] < now) {
                now += m[i];
            } else {
                int d = 0;
                for (__int64 j = now - 1; (d < N - i) && (m[i] >= now); ){
                    d ++;
                    now += j;
                    j = now - 1;
                }
                if (m[i] >= now) {
                    d = N - i;
                    moves += d;
                    break;
                }
                moves += d;
                now += m[i];
            }
        }
        /*output*/
        stringstream ss;
        ss << "Case #" << cc + 1 << ": " << moves << endl;
        fout << ss.str().c_str();
        cout << ss.str().c_str();
    }
    return 0;
}
