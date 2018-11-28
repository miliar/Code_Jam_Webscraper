#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <string>
using namespace std;

int m, n, num[8], ans, cnt;
vector<string> s;
set<string> d[5];

void search(int step) {
    if (step == m) {
        for (int i = 1; i <= n; i++) {
            d[i].clear();
        }
        for (int i = 0; i < m; i++) {
            for (int j = 1; j <= s[i].length(); j++) {
                string t = s[i].substr(0, j);
                d[num[i]].insert(t);
            }
        }
        int cur = 0;
        for (int i = 1; i <= n; i++) {
            if (d[i].size() == 0) {
                return;
            }
            cur += d[i].size() + 1;
        }
        if (cur == ans) {
            cnt++;
        }
        if (cur > ans) {
            ans = cur;
            cnt = 1;
        }
    } else {
        for (int i = 1; i <= n; i++) {
            num[step] = i;
            search(step + 1);
        }
    }
}

int main() {
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    int T;
    cin >> T;
    for (int task = 1; task <= T; task++) {
        cin >> m >> n;
        s.clear();
        for (int i = 0; i < m; i++) {
            string t;
            cin >> t;
            s.push_back(t);
        }
        ans = 0;
        cnt = 0;
        search(0);
        printf("Case #%d: %d %d\n", task, ans, cnt);
    }
    
    return 0;
}
