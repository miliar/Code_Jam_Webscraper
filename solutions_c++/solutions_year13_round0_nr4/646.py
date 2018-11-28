#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <cstring>
using namespace std;

vector <vector <int> > chests;
vector<int> toOpen;
int n;
int to[1 << 21];
int finish;
bool dp[1 << 21];

bool foo(int state) {
    dp[state] = true;
    map<int,int> keys;
    for (int i = 0; i <= n; ++i) {
        if (state & (1 << i)) {
            for (vector<int>::const_iterator it = chests[i].begin(); it != chests[i].end(); ++it) {
                ++keys[*it];
            }
            --keys[toOpen[i]];
        }
    }

    bool ans = false;
    for (int i = 1; i <= n; ++i) {
        if (ans) {
            break;
        }
        if ((keys[toOpen[i]] > 0) && (!(state & (1 << i)))) {
            int newState = state | (1 << i);
            if (!dp[newState]) {
                bool x = foo(newState);
                if (x && (to[state] == -1)) {
                    to[state] = i;
                }
                ans |= x;
            }
        }
    }
    return ans || (state == finish);
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        memset(dp, 0, sizeof(dp));
        memset(to, 255, sizeof(to));
        chests.clear();
        toOpen.clear();
        int k;
        cin >> k >> n;
        finish = (1 << (n + 1)) - 1;
        chests.resize(n + 1, vector<int>());
        toOpen.resize(n + 1, -1);
        set<int> set;
        for (int j = 0; j < k; ++j) {
            int x;
            cin >> x;
            chests[0].push_back(x);
        }
        for (int j = 1; j <= n; ++j) {
            int tj, kj;
            cin >> tj >> kj;
            toOpen[j] = tj;
            set.insert(tj);
            for (int k = 0; k < kj; ++k) {
                int x;
                cin >> x;
                chests[j].push_back(x);
            }
        }
        for (int j = 0; j <= n; ++j) {
            for (vector<int>::iterator it = chests[j].begin(); it != chests[j].end(); ++it) {
                if (!set.count(*it)) {
                    *it = -1;
                }
            }
        }

        if (foo(1)) {
            cout << "Case #" << i << ": ";
            for (int j = 1; j != finish; ) {
                cout << to[j] << " ";
                j |= 1 << to[j];
            }
        } else {
            cout << "Case #" << i << ": IMPOSSIBLE";
        }
        cout << "\n";
    }
}

