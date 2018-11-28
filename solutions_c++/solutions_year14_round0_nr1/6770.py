#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <cstdlib>
#include <cstdio>

using namespace std;

class Solution {
private:
    int a[4][4], b[4][4];
    int u, v;
public:
    void read() {
        cin >> u;
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                cin >> a[i][j];
            }
        }
        cin >> v;
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                cin >> b[i][j];
            }
        }
    }
    void solve(int kcase) {
        int cnt = 0, res;
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                if (a[u - 1][i] == b[v - 1][j]) {
                    ++cnt;
                    res = a[u - 1][i];
                }
            }
        }
        if (cnt == 1) {
            cout << "Case #" << kcase << ": " << res << endl;
        } else if (!cnt) {
            cout << "Case #" << kcase << ": Volunteer cheated!" << endl;
        } else {
            cout << "Case #" << kcase << ": Bad magician!" << endl;
        }
    }
};

Solution* solver = new Solution();

int main() {
    //freopen("a.in", "r", stdin);
    //freopen("a.out", "w", stdout);
    int Q;
    cin >> Q;
    for (int kcase = 1; kcase <= Q; ++kcase) {
        solver -> read();
        solver -> solve(kcase);
    }
    return 0;
}
