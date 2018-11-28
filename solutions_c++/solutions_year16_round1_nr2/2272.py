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

using namespace std;

/*
#define VI vector<int>
#define PII pair<int, int>
#define VPI vector<PII>
#define MII map<int, int>
#define LLI long long int
*/
#define SZ(x) ((int) (x).size())
#define PB(x) push_back(x)
#define MP(x,y) make_pair(x,y)
#define MS(x, v) memset(x,v,sizeof(x))
#define FOR(n) for(int (i)=0;(i)<(n);++(i))
#define FORI(n) for(int (i)=1;(i)<=(n);++(i))
#define LGN 20
#define SZN 105
#define MXN 2505
#define _ ios_base::sync_with_stdio(0); // do not use scanf or printf with this

typedef long long int LLI;
typedef map<int, int> MII;
typedef pair<int, int> PII;
typedef vector<PII> VPI;
typedef vector<int> VI;

const int inf = 0x3f3f3f3f;
const double eps = 1e-6;
const double pi = acos(-1.0);

/* structs */

/* globals */
int p[SZN*2][SZN];
int arr[MXN];
set<int> nums;

/* function declarations */


/* Problem */
int main() { _ // disable sync with stdio
    int t;
    cin >> t;
    int n;
    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ":";
        cin >> n;
        int f;
        // MS(arr, 0);
        memset(arr, 0, sizeof(arr));
        for (int j = 0; j < 2*n-1; ++j) {
            for (int k = 0; k < n; ++k) {
                cin >> f;
                arr[f]++;
            }
        }

        for (int j = 1; j < MXN; ++j) {
            if (arr[j] % 2 == 1) {
                nums.insert(j);
            }
        }

        for (set<int>::iterator it = nums.begin(); it != nums.end(); ++it) {
            cout << " " << *it;
        }
        cout << "\n";
        nums.clear();
    }

    return 0;
}

