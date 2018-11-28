#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>

using namespace std;

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

__int64 gcd( __int64 a, __int64 b ) { return a ? gcd( b%a, a ) : b; }

int main() {
    FileReader fin( "B-large.in" );
    FileWriter fout( "out.txt" );

    int caseCount;
    fin >> caseCount;
    fin.readLine();
    for (int cc = 0; cc < caseCount; cc ++ ) {
        int X, Y;
        fin >> X >> Y;
        fin.readLine();
        int maxX [100], maxY [100], h [100][100];
        for (int i = 0; i < X || i < Y; i ++) maxX [i] = maxY [i] = 0;
        for (int i = 0; i < X; i ++) {
            for (int j = 0; j < Y; j ++) {
                fin >> h [i][j];
                if (h [i][j] > maxX [i]) maxX[i] = h [i][j];
                if (h [i][j] > maxY [j]) maxY[j] = h [i][j];
            }
            fin.readLine();
        }
        int possible = 1;

        for (int i = 0; i < X; i ++)
            if (possible == 1) for (int j = 0; j < Y; j ++)
                if (h [i][j] < maxX [i] && h [i][j] < maxY [j]) {
                    cout << i << ' ' << j << endl;
                    possible = 0;
                    break;
                }

        stringstream ss;
        ss << "Case #" << cc + 1 << ": " << ((possible == 1) ? "YES" : "NO") << endl;
        fout << ss.str().c_str();
        cout << ss.str().c_str();
    }
    return 0;
}
