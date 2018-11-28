#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#pragma warning( disable : 4244 4267 4018 4996 4800 )
//#pragma comment( linker, "/stack:10000000" )
using namespace std; 
typedef vector< int > vi; typedef vector< vector< int > > vvi; typedef vector< string > vs; typedef vector< double > vd;
typedef vector< vd > vvd; typedef long long ll; typedef vector< ll > vll; typedef vector< vll > vvll; typedef pair< int, int > pii;
#define all( v ) (v).begin( ), (v).end( )

ifstream in( "b.in" );
ofstream out( "b.out" );

double const eps = 1e-10;

int main() {
    int ntests;
    in >> ntests;
    for (int test = 1; test <= ntests; ++test) {        
        int n;
        double V, X;
        in >> n >> V >> X;
        vd v(n), x(n);
        for (int i = 0; i < n; ++i) {
            in >> v[i] >> x[i];
        }
        double res = -1;        
        if (n == 1) {
            if (x[0] == X)
                res = V / v[0];
        } else {
            if (x[0] == X && x[1] == X)
                res = V / (v[0] + v[1]);
            else if (x[0] == X)
                res = V / v[0];
            else if (x[1] == X)
                res = V / v[1];            
            else if (x[0] != x[1]) {
                double t1 = (X - x[0]) * V / (v[1] * (x[1] - x[0]));
                double t0 = (V - v[1] * t1) / v[0];
                if (t0 >= -eps && t1 >= -eps)
                    res = max(t0, t1);
            }
        }
        out.setf(ios::fixed);
        out.precision(10);
        out << "Case #" << test << ": ";
        if (res == -1)
            out << "IMPOSSIBLE";
        else
            out << res;
        out << "\n";
    }
    return 0;
}