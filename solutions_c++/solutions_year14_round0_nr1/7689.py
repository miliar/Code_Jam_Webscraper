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
        vector< set<int> > rowSets1(4);
        int firstAns = 0; cin >> firstAns;
        REP (row, 4) {
            REP (col, 4) {
                int val = 0; cin >> val;
                rowSets1.at(row).insert(val);
            }
        }
        vector< set<int> > rowSets2(4);
        int secondAns = 0; cin >> secondAns;
        REP (row, 4) {
            REP (col, 4) {
                int val = 0; cin >> val;
                rowSets2.at(row).insert(val);
            }
        }

        vector<int> intersection;
        set_intersection(ALL(rowSets1.at(firstAns - 1)),
                         ALL(rowSets2.at(secondAns - 1)),
                         inserter(intersection, intersection.begin()));
        int nElems = SIZE(intersection);
        cout << "Case #" << test << ": ";
        if (nElems == 1) {
            cout << *intersection.begin() << "\n";
        } else if (nElems == 0) {
            cout << "Volunteer cheated!\n";
        } else {
            cout << "Bad magician!\n";
        }
    }

    return 0;
}
