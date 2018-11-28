#include <cstdio>
#include <cstdlib>
#include <climits>
#include <cmath>
#include <cctype>
#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <map>
#include <set>
#include <vector>
#include <stack>
#include <queue>
#include <utility>
#include <algorithm>
#include <bitset>

#define VI vector<int>
#define PII pair<int, int>
#define VPI vector<PII>
#define MII map<int, int>
#define LLI long long int
#define SZN 105
#define MXN 1005
#define _ ios_base::sync_with_stdio(0); // do not use scanf or printf with this

const int inf = 0x3f3f3f3f;
const double eps = 1e-6;
const double pi = acos(-1.0);

using namespace std;

/* structs */

/* globals */

/* function declarations */


/* Problem */
int main() { _ // disable sync with stdio
    int t, k, c, s;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ":";
        cin >> k >> c >> s;
        for (int j = 1; j <= s; ++j) {
            cout << " " << j;
        }
        cout << "\n";
    }

    return 0;
}
