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
#include <iomanip>

using namespace std;

#define SZ(x) ((int) (x).size())
#define LEN(x) ((int) (x).length())
#define PB(x) push_back(x)
#define MP(x,y) make_pair(x,y)
#define MS(x, v) memset(x,v,sizeof(x))
#define FOR(i, n) for (int (i)=0; (i)<(n); ++(i))
#define FORI(i, n) for (int (i)=1; (i)<=(n); ++(i))
#define LGN 20
#define SZN 105
#define MXN 1005
#define _ ios_base::sync_with_stdio(0); // do not use scanf or printf with this

typedef long long int LLI;
typedef map<int, int> MII;
typedef pair<int, int> PII;
typedef vector<PII> VPI;
typedef vector<int> VI;

const int inf = 0x3f3f3f3f;
const int mod = 1e9 + 7;
const double eps = 1e-8;
const double pi = acos(-1.0);

/* structs */
typedef vector<double> vtr;
typedef vector<vtr> mat;

/* globals */
int cnt[SZN];
int result[SZN];
string nums[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

/* function declarations */


/* Problem */
int main() { // _ // disable sync with stdio
    int t;
    cin >> t;
    string str;
    mat A(26, vtr(15));
    FOR(i, 10) {
        str = nums[i];
        FOR(j, LEN(str)) {
            A[str[j]-'A'][i] = 1;
        }
    }
    FORI(i, t) {
        memset(cnt, 0, sizeof(cnt));
        MS(result, 0);
        cout << "Case #" << i << ": ";
        cin >> str;
        FOR(j, LEN(str)) {
            cnt[str[j]-'A']++;
        }
        result[0] = cnt[25];
        cnt[(int)'E'-'A'] -= cnt[25];
        cnt[(int)'R'-'A'] -= cnt[25];
        cnt[(int)'O'-'A'] -= result[0];

        result[2] = cnt[(int)'W'-'A'];
        cnt[(int)'T'-'A'] -= result[2];
        cnt[(int)'O'-'A'] -= result[2];

        result[6] = cnt[(int)'X'-'A'];
        cnt[(int)'S'-'A'] -= result[6];
        cnt[(int)'I'-'A'] -= result[6];

        result[4] = cnt[(int)'U'-'A'];
        cnt[(int)'F'-'A'] -= result[4];
        cnt[(int)'O'-'A'] -= result[4];
        cnt[(int)'R'-'A'] -= result[4];

        result[3] = cnt [(int)'R'-'A'];
        cnt[(int)'T'-'A'] -= result[3];
        cnt[(int)'H'-'A'] -= result[3];
        cnt[(int)'E'-'A'] -= 2*result[3];

        result[1] = cnt[(int)'O'-'A'];
        cnt[(int)'N'-'A'] -= result[1];
        cnt[(int)'E'-'A'] -= result[1];

        result[8] = cnt[(int)'G'-'A'];
        cnt[(int)'I'-'A'] -= result[8];
        cnt[(int)'E'-'A'] -= result[8];
        cnt[(int)'H'-'A'] -= result[8];
        cnt[(int)'T'-'A'] -= result[8];

        result[7] = cnt[(int)'S'-'A'];
        cnt[(int)'V'-'A'] -= result[7];
        cnt[(int)'E'-'A'] -= 2*result[7];
        cnt[(int)'N'-'A'] -= result[7];

        result[5] = cnt[(int)'V'-'A'];
        cnt[(int)'I'-'A'] -= result[5];
        cnt[(int)'E'-'A'] -= result[5];
        cnt[(int)'F'-'A'] -= result[5];

        result[9] = cnt[(int)('I'-'A')];

        FOR(j, 10) {
            while (result[j] > 0) {
                cout << j;
                result[j]--;
            }
        }
        cout << "\n";
    }

    return 0;
}

