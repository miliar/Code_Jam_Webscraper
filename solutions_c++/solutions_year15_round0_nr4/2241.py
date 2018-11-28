//#pragma comment(linker, "/STACK:16777216") //for c++ Compiler
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <cstring>
#include <cmath>
#include <stack>
#include <string>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <vector>
#include <algorithm>
#define Max(a,b) (((a) > (b)) ? (a) : (b))
#define Min(a,b) (((a) < (b)) ? (a) : (b))
#define Abs(x) (((x) > 0) ? (x) : (-(x)))
#define MOD 1000000007
#define pi acos(-1.0)

using namespace std;

typedef long long           ll      ;
typedef unsigned long long  ull     ;
typedef unsigned int        uint    ;
typedef unsigned char       uchar   ;

template<class T> inline void checkmin(T &a,T b){if(a>b) a=b;}
template<class T> inline void checkmax(T &a,T b){if(a<b) a=b;}

const double eps = 1e-7      ;
const int N = 210            ;
const int M = 1100011*2      ;
const ll P = 10000000097ll   ;
const int MAXN = 10900000    ;
const int INF = 0x3f3f3f3f   ;

int x, r, c;

int main(){
    std::ios::sync_with_stdio(false);
    int i, j, t, k, u, v, numCase = 0;

    ofstream fout ("D-small-attempt5.out");
    ifstream fin ("D-small-attempt5.in");

    fin >> t;
    while (t--) {
        fin >> x >> r >> c;
        if (1 == x) {
            fout << "Case #" << ++numCase << ": " << "GABRIEL" << endl;
            continue;
        } else if (2 == x) {
            if (r == 1 && c == 1 || r == 1 && c == 3 || r == 3 && c == 1 || r == 3 && c == 3) {
                fout << "Case #" << ++numCase << ": " << "RICHARD" << endl;
                continue;
            } else {
                fout << "Case #" << ++numCase << ": " << "GABRIEL" << endl;
                continue;
            }
        } else if (3 == x) {
            if (r == 1 && c == 1 || r == 2 && c == 1 || r == 1 && c == 2 || r == 2 && c == 2 || \
                r == 3 && c == 1 || r == 1 && c == 3 || r == 1 && c == 4 || r == 4 && c == 1 || \
                r == 2 && c == 4 || r == 4 && c == 2 || r == 4 && c == 4) {
                fout << "Case #" << ++numCase << ": " << "RICHARD" << endl;
                continue;
            } else {
                fout << "Case #" << ++numCase << ": " << "GABRIEL" << endl;
                continue;
            }
        } else if (4 == x){
            if (r == 3 && c == 4 || r == 4 && c == 3 || r == 4 && c == 4) {
                fout << "Case #" << ++numCase << ": " << "GABRIEL" << endl;
                continue;
            } else {
                fout << "Case #" << ++numCase << ": " << "RICHARD" << endl;
                continue;
            }
        }
    }

    return 0;
}












