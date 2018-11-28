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

int n, num, ans;
vector <int> a;

void dfs (int level) {
    int i, j;
    int MAX = -INF;
    int flag;

    if (level > ans) {
        return;
    }
    for (i = 0; i < a.size (); ++i) {
        if (a[i] > MAX) {
            flag = i;
            MAX = a[i];
        }
    }
    if (MAX <= 3) {
        checkmin (ans, level + MAX);
        return;
    }
    for (i = 0; i < a.size (); ++i) {
        --a[i];
    }
    dfs (level + 1);
    for (i = 0; i < a.size (); ++i) {
        ++a[i];
    }
    for (i = 1; i <= a[flag] / 2; ++i) {
        a[flag] -= i;
        a.push_back (i);
        dfs (level + 1);
        a.pop_back ();
        a[flag] += i;
    }

    /*
    bool flagi = true;
    if (MAX & 1) {
        int cur = a[flag];
        a[flag] = (cur + 1) / 2;
        a.push_back (cur - a[flag]);
    } else {
        flagi = false;
        int cur = a[flag];
        a[flag] /= 2;
        a.push_back (cur / 2);
    }
    dfs (level + 1);
    if (flagi) {
        a[flag] += a[flag] - 1;
        a.pop_back ();
    } else {
        a[flag] *= 2;
        a.pop_back ();
    }
    */
}

int main(){
    std::ios::sync_with_stdio(false);
    int i, j, t, k, u, v, numCase = 0;

    ofstream fout ("B-small-attempt4.out");
    ifstream fin ("B-small-attempt4.in");

    fin >> t;
    while (t--) {
        a.clear ();
        fin >> n;
        while (n--) {
            fin >> num;
            a.push_back (num);
        }

        ans = INF;
        dfs (0);

        fout << "Case #" << ++numCase << ": " << ans << endl;
    }

    return 0;
}












