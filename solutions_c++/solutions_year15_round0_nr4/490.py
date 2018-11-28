#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
#ifdef __GXX_EXPERIMENTAL_CXX0X__
#include <unordered_map>
#include <unordered_set>
#endif

using namespace std;

#define ALL(x) (x).begin(), (x).end()
#define EACH(itr,c) for(__typeof((c).begin()) itr=(c).begin(); itr!=(c).end(); itr++)  
#define FOR(i,b,e) for (int i=(int)(b); i<(int)(e); i++)
#define MP(x,y) make_pair(x,y)
#define REP(i,n) for(int i=0; i<(int)(n); i++)

// can you fill a tile no matter what Richard chooses?
bool check(int x, int r, int c) {

    // there exists an isolated empty cell
    if (x >= 7)
        return false;
    
    // make sure r > c
    if (r < c)
        swap(r, c);

    if (r * c % x)
        return false;
    return r >= x && c >= (x-1);

    return false;
}


void solve() {

    int x, r, c;
    cin >> x >> r >> c;

    if (check(x, r, c))
        cout << "GABRIEL" << endl;
    else
        cout << "RICHARD" << endl;

}

int main() {
    ios_base::sync_with_stdio(0);

    int T;
    cin >> T;
    REP (i, T) {
        cerr << "Case #" << i+1 << ": " << endl;
        cout << "Case #" << i+1 << ": ";
        solve();
    }

    return 0;
}
