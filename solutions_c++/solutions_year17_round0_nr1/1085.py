/******************************************************************************\
*                         Author:  Dumbear                                     *
*                         Email:   dumbear[#at]163.com                         *
*                         Website: http://dumbear.com                          *
\******************************************************************************/
#include <algorithm>
#include <bitset>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
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
#include <typeinfo>
#include <utility>
#include <vector>

using namespace std;

#define output(x) cout << #x << ": " << (x) << endl;

typedef long long LL;
typedef vector<int> VI;
typedef vector<long long> VL;
typedef vector<double> VD;
typedef vector<string> VS;

const int max_n = 1000 + 10;

int t, k;
char s[max_n];

int get_min_flips() {
    int cnt = 0;
    int n = strlen(s);
    for (int i = 0; i < n; ++i) {
        if (s[i] == '-') {
            if (i + k > n) {
                return -1;
            }
            ++cnt;
            for (int j = 0; j < k; ++j) {
                s[i + j] = (s[i + j] == '+' ? '-' : '+');
            }
        }
    }
    return cnt;
}

void solve() {
    scanf("%s%d", s, &k);
    int res = get_min_flips();
    printf("Case #%d: ", ++t);
    if (res == -1) {
        puts("IMPOSSIBLE");
    } else {
        printf("%d\n", res);
    }
}

int main() {
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i)
        solve();
    return 0;
}
