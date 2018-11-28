#include <iostream>
#include <string>
#include <climits>
#include <set>
#include <queue>

using namespace std;

int transf(int n, int pos, int flip) {
    int ans = pos & (~((1 << flip) - 1));
    for (int i = 0; i < flip; i++) {
        if (!(pos & (1 << (flip - i - 1))))
            ans |= 1 << i;
    }
    //printf("%d,%d,%d -> %d\n", n, pos, flip, ans);
    return ans;
}

int solve(int n, int pos) {
    queue<int> q;
    set<int> vis;
    q.push(pos);
    vis.insert(pos);
    q.push(-1);
    int moves = 0;
    while (!q.empty()) {
        int p = q.front();
        q.pop();
        if (p == -1) {
            moves++;
            q.push(-1);
            continue;
        }
        if (p == 0) {
            return moves;
        }
        for (int j = 1; j <= n; j++) {
            int npos = transf(n, p, j);
            if (vis.count(npos) == 0) {
                q.push(npos);
                vis.insert(npos);
            }
        }
    }
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        string s;
        cin >> s;
        int inp = 0;
        for (int j = 0; j < s.length(); j++) {
            if (s[j] == '-')
                inp |= 1 << j;
        }
        printf("Case #%d: %d\n", i, solve(s.length(), inp));
    }
    return 0;
}
