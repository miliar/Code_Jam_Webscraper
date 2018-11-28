// WHY NOT PUT THIS IN SHADER + OFMAIN + TOPCODER ALL THE SAME RIGHT

#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <deque>
#include <fstream>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define MP make_pair
#define PB push_back
#define REP(k,a) for(int k=0; k < (a); ++k)
#define SZ(a) ((int)((a.size())
#define TR(c,i) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)

#define INF (int)1e9
#define EULER 2.718281828459045
#define EPS 1e-9
#define PI 3.14159265358979
#define TAU 6.28318530717959

#define LD long double
#define LL long long
#define PII pair<int,int>
#define VI vector<int>
#define VLL vector<long long>
#define VS vector<string>

#ifdef DEBUG
    #define debug(args...) {dbg,args; cout<<endl;}
#else
    #define debug(args...)
#endif

struct debugger {
    template<typename T> debugger& operator , (const T& v) {
        cout << v << " ";
        return *this;
    }
} dbg;

/////////////////////////////////////////////////////////////////////////////// 
int
main (int argc, char *argv[]) {
    fstream infile("large_input.txt");
    string line;
    int T;
    int Smax;
    int min;
    int sum;

    infile >> T;
    debug("T=", T);

    REP (i, T) {

        sum = 0;
        min = 0;

        infile >> Smax;
        debug("Smax=", Smax);
        getline(infile, line);
        line = line.substr(1, string::npos);
        debug("line=", line);

        REP (j, line.size()) {
            if ( j == 0 ) {
                if ( line[j] == '0') { sum++; min++; }
                else { }
            } else if ( sum < j ) {
                min++;
                sum++;
                debug("sum is ", sum, " so adding one to min");
            }

            sum += line[j] - '0';
            debug("sum:", sum, "min:", min);
        }

        cout << "Case #" << i+1 << ": " << min << endl;
    }

    return 0;
}

















