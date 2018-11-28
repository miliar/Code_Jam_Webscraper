#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

#define FOREACH(i, c) for(__typeof( (c).begin() ) i = (c).begin(); i != (c).end(); ++i)
#define FOR(i, a, n) for(__typeof(n) i = (a); i<(n); ++i)
#define REP(i, a, n) for(__typeof(n) i = (a); i<=(n); ++i)
#define ROF(i, n, a) for(__typeof(n) i = (n); i>=(a); --i)
#define error(n) cout << #n << " = " << n << endl
#define all(c) c.begin(), c.end()
#define pb push_back
#define po pop_back
#define Size(n) ((int)(n).size())
#define X first
#define Y second
#define scanf _ = scanf
// #define X real()
// #define Y imag()

typedef long long   ll ;
typedef long double ld ;
typedef pair<int,int> pii ;

const int maxn = 1111;

double a[maxn] , b[maxn];

int main() {
    int T;
    cin >> T;
    REP (lv,1,T) {
        int n;
        cin >> n;
        FOR (i,0,n)
            cin >> a[i];
        FOR (i,0,n)
            cin >> b[i];
        cout << "Case #" << lv << ": ";
        sort (a,a+n);
        sort (b,b+n);
//         FOR (i,0,n)
//             cerr << a[i] << " " ;cerr << endl;
//         FOR (i,0,n)
//             cerr << b[i] << " " ;cerr << endl;
        
        //
        int ptr = n-1;
        ROF (i,n-1,0) {
            if (ptr >= 0 && b[i] < a[ptr]) {
                --ptr;
            }
        }
        cout << n-(ptr+1) << " ";
        //
        ptr = n-1;
        ROF (i,n-1,0) {
            if (ptr >= 0 && a[i] < b[ptr])
                --ptr;
        }
        cout << ptr+1 << endl;
    }
    return 0 ;
}
