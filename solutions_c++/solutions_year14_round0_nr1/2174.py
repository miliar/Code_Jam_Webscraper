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
int _ ;
#define scanf _ = scanf
// #define X real()
// #define Y imag()

typedef long long   ll ;
typedef long double ld ;

typedef pair<int,int> pii ;

int sum[17];

int T;

void Read() {
    int r;
    cin >> r;
    FOR (i,0,4) {
        FOR (j,0,4) {
            int x;
            cin >> x;
            if (r == i+1)
                ++sum[x];
        }
    }
}

int main() {
    cin  >> T;
    REP (lv,1,T) {
        memset (sum,0,sizeof(sum));
        Read();
        Read();
        int num = 0 , last = 0;
        REP (i,0,17)
            if (sum[i] == 2) {
                num++;
                last = i;
            }
        cout << "Case #" << lv << ": ";
        if (num == 0)
            cout << "Volunteer cheated!" << endl;
        else if (num == 1)
            cout << last << endl;
        else
            cout << "Bad magician!" << endl;
    }
    return 0 ;
}
