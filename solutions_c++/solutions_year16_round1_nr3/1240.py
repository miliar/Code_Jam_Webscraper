#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int a[1005];
int ans = -1;
int n;
bool used[15];
vector<int> v;

bool ok(int x) {
    int l = (x == 0) ? v.back() : v[x-1];
    int r = (x == v.size() - 1) ? v[0] : v[x+1];
    if(a[v[x]] == l || a[v[x]] == r) return 1;
    return 0;
}

void dfs(int x) {
    if(x == n) {
        return ;
    }
    for(int i = 0; i < n; i ++) if(!used[i]) {
        used[i] = 1;
        v.push_back(i);
        if(ok(0) && ok(x-1) && ok(x) && ans < x+1) ans = x+1;
        if(x < 2) dfs(x+1);
        else if(ok(x-1)) dfs(x+1);
        v.pop_back();
        used[i] = 0;
    }
}

int solve() {
    scanf("%d", &n);
    for(int i = 0; i < n; i ++) {
        scanf("%d", &a[i]);
        a[i] --;
    }
    ans = -1;
    memset(used, 0, sizeof(used));
    v.clear();
    dfs(0);
    return ans;
}


int main() {
    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int t = 1; t <= T; t ++) {
        printf("Case #%d: %d\n", t, solve());
    }
    return 0;
}
