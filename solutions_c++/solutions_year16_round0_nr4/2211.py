#include <vector>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <string>
#include <bitset>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>

using namespace std;

const char* NO = " IMPOSSIBLE";

void solve() {
    int k, c, s;
    cin >> k >> c >> s;
    for (int i = 0; i < k; ++i) {
        cout << ' ' << i + 1;
    }
    cout << endl;
    /*
    if (c == 1) {
        if (s < k) {
            puts(NO);
        } else {
            for (int i = 0; i < k; ++i) {
                cout << ' ' << i + 1;
            }
            cout << endl;
        }
    } else {
        if (s < k - 1) {
            puts(NO);
        } else {
            for (int i = 1; i < k; ++i) {
                cout << ' ' << i + 1;
            }
            cout << endl;
        }
    }
    */
}

int main() {
    //freopen("D.in", "r", stdin);
    //freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small-attempt1.in", "r", stdin);
    freopen("D.out", "w", stdout);

    int T;
    cin >> T;
    for (int caseId = 1; caseId <= T; ++caseId) {
        printf("Case #%d:", caseId);
        solve();
        fflush(stdout);
    }
}
