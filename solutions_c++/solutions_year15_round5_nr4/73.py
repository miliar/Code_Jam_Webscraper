#include <cstdio>
#include <map>
#include <algorithm>
#include <vector>
using namespace std;

int p;
int x[1 << 17];
int y[1 << 17];
map<int, int> mp;

void read() {
    mp.clear();
    scanf("%d", &p);
    for (int i = 0; i < p; i++) {
        scanf("%d", &x[i]);
        mp[ x[i] ] = i;
    }
    for (int i = 0; i < p; i++) scanf("%d", &y[i]);
}

void solve() {
    vector<int> ans;

    /*
    y[0] --;
    while (y[0] > 0) {
        -- y[0];
        ans.push_back(0);
        for (int i = 0; i < p; i++) y[i] /= 2;
    }
    */
    y[0] --;

    while (1) {
        int idx = -1;
        for (int i = 0; i < p; i++) {
            if (y[i] > 0) {
                idx = i;
                break;
            }
        }
        if (idx == -1) break;

        for (int i = 0; i < (1 << (int)ans.size()); i++) {
            int sum = 0;

            for (int j = 0; j < (int)ans.size(); j++) {
                if (i & (1 << j)) {
                    sum += ans[j];
                }
            }

            y[ mp[ sum + x[idx] ] ] --;
        }
        ans.push_back(x[idx]);
    }

    sort(ans.begin(), ans.end());
    for (int i = 0; i < (int)ans.size(); i++) {
        printf ("%d%c", ans[i], (i + 1 == (int)ans.size()) ? '\n' : ' ');
    }
}

int main() {
    int cases;
    
    scanf("%d", &cases);
    for (int i = 1; i <= cases; i++) {
        read();
        printf ("Case #%d: ", i);
        solve();
    }
    
    return 0;
}
