#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t, n, cnt, cur, tmp;
    cin >> t;
    for (int casenum = 1; casenum <= t; ++casenum) {
        bool vis[10] = {0};
        cin >> n;
        cnt = cur = 0;
        cout << "Case #" << casenum << ": ";
        if (!n) {
            cout << "INSOMNIA" << endl;
        } else {
            while (cnt < 10) {
                cur += n;
                tmp = cur;
                while (tmp) {
                    if (!vis[tmp%10]) {
                        cnt++;
                        vis[tmp%10] = true;
                    }
                    tmp /= 10;
                }
            }
            cout << cur << endl;
        }

    }
    return 0;
}
