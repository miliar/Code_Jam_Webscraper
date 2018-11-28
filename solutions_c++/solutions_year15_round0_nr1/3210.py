#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <numeric>
#include <fstream>
#include <iostream>
#include <utility>
#include <iomanip>
#include <stack>
#include <list>
#include <sstream>
using namespace std;
#define PB push_back
#define MP make_pair
#define REP(i, n) for (int i(0); i < n; ++i)
#define REP1(i, n) for (int i(1); i < n; ++i)
#define FOR(i, a, b) for (int i(a); i <= b; ++i)

int tc;
int m;
string s;
int cnt[1024];

int solve() {
    int res = 0;
    REP(i, s.length()) {
        if (i == 0) {
            cnt[i] = s[i] - '0';
            continue;
        }
        cnt[i] = cnt[i-1] + (s[i] - '0');
        if (i > cnt[i-1] + res) {
            res += (i - cnt[i-1] - res);
        }
    }
    return res;
}

int main(int argc, char* argv[]) {
    cin >> tc;
    int tcIndex = 1;
    REP(i, tc) {
        cin >> m;
        cin >> s;
        memset(cnt, 0, sizeof(cnt));
        printf("Case #%d: %d\n", tcIndex, solve());
        tcIndex++;
    }
    return 0;
}
