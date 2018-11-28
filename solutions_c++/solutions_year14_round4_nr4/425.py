#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>

using namespace std;

int m, n, x, y;
string s[10];
int p[10];

void check(int num) {
    if (num == m) {
        int cnt = 0;
        for (int i = 0; i < n; ++i) {
            set<string> t;
            for (int j = 0; j < m; ++j) {
                if (p[j] == i) {
                    string tmp = "";
                    for (int k = 0; k < (int)s[j].length(); ++k) {
                        tmp += s[j][k];
                        t.insert(tmp);
                    }
                }
            }
            if (t.size() == 0)
                return;
            cnt += (int)t.size() + 1;
        }
        if (cnt > x) {
            x = cnt;
            y = 1;
        } else if (cnt == x)
            ++y;
        return;
    }
    for (int i = 0; i < n; ++i) {
        p[num] = i;
        check(num + 1);
    }
}

void solve() {
    cin >> m >> n;
    for (int i = 0; i < m; ++i)
        cin >> s[i];
    x = 0; y = 0;
    check(0);
    printf("%d %d\n", x, y);
}

int main() {
    int numCases;
    cin >> numCases;
    for (int caseNo = 1; caseNo <= numCases; ++caseNo) {
        printf("Case #%d: ", caseNo);
        solve();
    }
    return 0;
}


