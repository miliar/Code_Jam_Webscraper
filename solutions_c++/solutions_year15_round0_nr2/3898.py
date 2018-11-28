#include <string>
#include <vector>
#include <cstring>
#include <iostream>
using namespace std;
#define MAXP 1010


int TC, D;

int getmax(const vector<int> &v) {
    for (int i = v.size()-1; i >= 1; i--) {
        if (v[i] > 0) return i;
    }
    return 0;
}


int dfs(vector<int> nostacks) {
    int res1, res2;
    int maxx = getmax(nostacks);
    /* cout << "(" << maxx << endl; //DEB */
    if (maxx <= 0) return 0;

    // Do nothing
    vector<int> nostacks1(nostacks.begin()+1, nostacks.end());
    res1 = 1 + dfs(nostacks1);

    if (maxx <= 1) return res1;
    // Have an optimal special minute(s)
    for (int takeoff = 1; takeoff <= maxx/2; ++takeoff) {
        vector<int> nostacks2(nostacks.begin(), nostacks.end());
        int back = nostacks2[maxx];
        nostacks2[takeoff] += nostacks2[maxx];
        nostacks2[maxx-takeoff] += nostacks2[maxx];
        nostacks2[maxx] = 0;
        nostacks2.resize(getmax(nostacks2)+1);
        res2 = min(res2, back + dfs(nostacks2));
    }

    return min(res1, res2);
}


int main() {
    cin >> TC;
    for (int tc = 1; tc <= TC; tc++) {
        vector<int> nostacks(10);
        cin >> D;
        for (int i = 1; i <= D; i++) {
            int t;
            cin >> t;
            ++nostacks[t];
        }
        nostacks.resize(getmax(nostacks)+1);
        cout << "Case #" << tc << ": " << dfs(nostacks) << endl;
    }
    return 0;
}
