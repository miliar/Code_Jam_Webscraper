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
int seen[10];

/* function declarations */


/* Problem */
int main() { _ // disable sync with stdio
    int t, n, tmp, s, j;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        memset(seen, 0, sizeof(seen));
        cout << "Case #" << i << ": ";
        cin >> n;
        s = 0;
        bool done = false;
        if (n == 0) {
            cout << "INSOMNIA\n";
        } else {
            j = 0;
            while (!done) {
                ++j;
                tmp = j * n;
                while (tmp) {
                    if (!seen[tmp % 10]) {
                        ++s;
                        seen[tmp % 10] = 1;
                        if (s == 10) {
                            done = true;
                            break;
                        }
                    }
                    tmp /= 10;
                }
            }
            cout << j * n << "\n";
        }
    }

    return 0;
}
