#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <cmath>
#include <vector>
#include <set>

using namespace std;

#define MAXN 200
#define PI 3.141592653589793238462643383;
#define CL(x,v); memset(x,v,sizeof(x));

int m, N;
int g [MAXN][MAXN];
set <int> ss;

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
        cout << "!!\n";
    for (int cc = 0; cc < caseCount; cc ++ ) {
        __int64 r, t, x;
        double s;
        fin >> r >> t;
        fin.readLine();
        /*solve*/
        x = floor((1 - 2 * r + sqrt (1 - 4 * r + 4 * r * r + 8 * t))/4);
        /*output*/
        stringstream ss;
        ss << "Case #" << cc + 1 << ": " << x << endl;
        fout << ss.str().c_str();
        cout << ss.str().c_str();
    }
    return 0;
}
