#pragma comment (linker, "/STACK:256000000")
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <functional>
using namespace std;

struct TTestCase {
    int n;
    vector<int> a;
    vector<int> b;
    typedef vector<int> vi;
    vector<vi> edges;
    vector<vi> redges;
    vi rorder;
    vi been;
    void dfs(int p) {
        if (been[p])
            return;
        been[p] = 1;
        for (vector<int>::const_iterator it = redges[p].begin(); it != redges[p].end(); ++it) {
            dfs(*it);
        }
        //rorder.push_back(p);
    }
    void run() {
        cin >> n;
        a.resize(n);
        b.resize(n);
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
        }
        for (int i = 0; i < n; ++i) {
            cin >> b[i];
        }
        edges.resize(n);
        redges.resize(n);
        vector<int> last;
        last.assign(n + 1, -1);
        for (int i = 0; i < n; ++i) {
            int cur = a[i];
            if (last[cur] != -1) {
                edges[i].push_back(last[cur]);
                redges[last[cur]].push_back(i);
            }
            if (last[cur-1] != -1) {
                edges[last[cur-1]].push_back(i);
                redges[i].push_back(last[cur-1]);
            }
            last[cur] = i;
        }
        last.assign(n + 1, -1);
        for (int i = n - 1; i >= 0; --i) {
            int cur = b[i];
            if (last[cur] != -1) {
                edges[i].push_back(last[cur]);
                redges[last[cur]].push_back(i);
            }
            if (last[cur-1] != -1) {
                edges[last[cur-1]].push_back(i);
                redges[i].push_back(last[cur-1]);
            }
            last[cur] = i;
        }
        vector< vi > dependent(n, vi(n));
        for (int i = 0; i < n; ++i) {
            been.assign(n, 0);
            dfs(i);
            dependent[i] = been;
        }
        vector<int> result(n);
        for (int i = 0; i < n; ++i) {
            result[i] = accumulate(dependent[i].begin(), dependent[i].end(), 0);
            for (int j = 0; j < n; ++j) {
                if (dependent[i][j] == 0)
                    dependent[j][i] = 1;
            }
            cout << " " << result[i];
        }
        cout << endl;
    }
};

int main(void) {
    int T;
    ios::sync_with_stdio(false);
    cin >> T;
    for (int testNo = 1; testNo <= T; ++testNo) {
        cout << "Case #" << testNo << ":";
        TTestCase().run();
    }
    return 0;
}