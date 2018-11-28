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

int n;
int a[1200];
char b[1200];

int main(){
    std::ios::sync_with_stdio(false);
    int i, j, t, k, u, v, numCase = 0;

    ofstream fout ("A-large.out");
    ifstream fin ("A-large.in");

    fin >> t;
    while (t--) {
        fin >> n;
        for (i = 0; i <= n; ++i) fin >> b[i];
        for (i = 0; i <= n; ++i) {
            a[i] = b[i] - '0';
        }
        int cur = 0;
        int ans = 0;
        for (i = 0; i <= n; ++i) {
            if (cur < i && a[i] > 0) {
                int delta = i - cur;
                ans += delta;
                cur += delta;
            }
            cur += a[i];
            //cout << i << ": " << cur << ' ' << ans << endl;
        }
        fout << "Case #" << ++numCase << ": " << ans << endl;
    }

    return 0;
}












