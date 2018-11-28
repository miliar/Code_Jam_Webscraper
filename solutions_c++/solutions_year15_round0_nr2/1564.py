#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;

int n;
vector<int> v;
map<vector<int>, int> dp;

int solve(const vector<int>& v) {
    if (dp.count(v) > 0)
        return dp[v];
    if (v.empty())
        return dp[v] = 0;
    vector<int> nv;
    for (int i = 0; i < v.size() && v[i] > 1; i++)
        nv.push_back(v[i] - 1);
    int ret = solve(nv);
    for (int j = 1; j <= v[0]/2; j++) {
        nv = v;
        nv.push_back(j);
        nv[0] = v[0] - j;
        sort(nv.rbegin(), nv.rend());
        ret = min(ret, solve(nv));
    }
    return dp[v] = ret + 1;
}

void traceback(const vector<int>& v) {
    printf("%d: ", dp[v]);
    for (int i = 0; i < v.size(); i++)
        printf("%d ", v[i]);
    puts("");
    if (v.empty())
        return;
    vector<int> nv;
    for (int i = 0; i < v.size() && v[i] > 1; i++)
        nv.push_back(v[i] - 1);
    if (dp[nv] == dp[v] - 1) {
        traceback(nv);
        return;
    }
    for (int i = 0; i < v.size() && v[i] > 1; i++) {
        for (int j = 1; j <= v[i]/2; j++) {
            nv = v;
            nv.push_back(j);
            nv[i] = v[i] - j;
            sort(nv.rbegin(), nv.rend());
            if (dp[nv] == dp[v] - 1) {
                traceback(nv);
                return;
            }
        }
    }
}

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d", &n);
        v.resize(n);
        for (int i = 0; i < n; i++)
            scanf("%d", &v[i]);
        dp.clear();
        sort(v.rbegin(), v.rend());
        printf("Case #%d: %d\n", t, solve(v));
        //traceback(v);
        //puts("done");
    }
}
