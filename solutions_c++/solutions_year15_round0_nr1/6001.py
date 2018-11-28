#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <map>
#include <set>
#include <list>
#include <vector>
#include <stack>
#include <queue>
#include <bitset>
#include <iterator>
#include <cstring>
#include <climits>
#include <cmath>
#include <cassert>

using namespace std;

#define ALL(x) x.begin(),x.end()
#define REP(i,n) for (int i=0; i<(n); ++i)
#define FOR(var,start,end) for (int var=(start); var<=(end); ++var)
#define FORD(var,start,end) for (int var=(start); var>=(end); --var)
#define FOREACH(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define PB push_back
#define PF push_front
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define SIZE(x) ((int)((x).size()))

// typedef long long LL;
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<bool> VB;
typedef vector< vector<int> > VVI;
typedef vector< vector<bool> > VVB;

int main() {
    int nTests = 0; cin >> nTests;
    FOR (test, 1, nTests) {
        int smax = 0; cin >> smax;
        string shynessCounts; cin >> shynessCounts;
        int prefixSum = 0;
        int ans = 0;
        REP (i, smax + 1) {
            int currCount = static_cast<int>(shynessCounts.at(i) - '0');
            if (prefixSum < i) {
                ans += i - prefixSum;
                prefixSum += i - prefixSum;
            }
            prefixSum += currCount;
        }
        cout << "Case #" << test << ": ";
        cout << ans << "\n";
    }

    return 0;
}

