#include <iostream>
#include <cstdio>
#include <algorithm>
#include <memory.h>
#include <map>
#include <vector>

using namespace std;

int a[1111], mem[1111][1111];
map<vector<int>, int> memv;

inline int brute(vector<int> v){
    if (!v.size()) return 0;
    sort(v.begin(), v.end());
    if (!v.back()) return 0;
    if (memv.find(v) != memv.end()) return memv[v];
    int res = 2e9;
    for(int i = 0; i < v.size(); i++) if (v[i] > 1){
        int m = v[i];
        v.push_back(m/2);
        v[i] = m - m/2;
        res = min(res, brute(v) + 1);
        v.pop_back();
        v[i] = m;
    }
    vector<int> vv = v;
    for(int i = 0; i < vv.size(); i++) if (vv[i]) vv[i]--;
    res = min(res, brute(vv) + 1);
    memv[v] = res;
    return res;
}

inline int rec(int n, int t){
    if (t >= n) return 0;
    if (mem[n][t] != -1) return mem[n][t];
    int res = rec(n/2, t) + rec(n/2 + (n%2), t) + 1;
    return mem[n][t] = res;
}

inline void solve(int cs){
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; i++) scanf("%d", &a[i]);
    int ans = 2e9;
    for(int t = 1; t <= 1000; t++) {
        int cur = 0;
        for(int i = 0; i < n; i++) cur += (a[i] - 1) / t;
        ans = min(ans, cur + t);
    }
    printf("Case #%d: %d\n", cs, ans);
}

int main(int argc, const char * argv[]) {
    memset(mem, -1, sizeof(mem));
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    int ttt;
    scanf("%d", &ttt);
    for(int cs = 1; cs <= ttt; cs++) solve(cs);
    return 0;
}
