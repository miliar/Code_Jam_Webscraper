#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

const int N = 4;

typedef pair<int, int> pii;

char mp[N][N + 1];
int n;
bool vis_C[4];
int idx[4];

bool dfs(int x) {
    //cout << x << ' ' << n << endl;
    if(x == n) return true;
    //cout << idx[x] << "---"<<endl;
    bool flag = false;
    for(int i = 0; i < n; ++i) if(mp[idx[x]][i] == '1' && vis_C[i] == false) {
        flag = true;
        vis_C[i] = true;
        bool ret = dfs(x + 1);
        if(ret == false) return false;
        vis_C[i] = false;
    }
    if(!flag) return false;
    return true;
}
bool check() {
    //for(int i = 0; i < n; ++i) cout << mp[i] << endl;
    sort(idx, idx + n);
    do {
        //cout << "-----------" << endl;
        memset(vis_C, false, sizeof(vis_C));
        bool ret = dfs(0);
        if(ret == false) return false;

    }while(next_permutation(idx, idx + n));

    //cout << "----" << endl;
    return true;
}
int main() {
    freopen("in.txt", "r", stdin);
    freopen("D.txt", "w", stdout);
    int _, cas = 1;
    for(scanf("%d", &_); _--; ) {
        printf("Case #%d: ", cas++);
        scanf("%d", &n);

        for(int i = 0; i < n; ++i) idx[i] = i;

        for(int i = 0; i < n; ++i)
            scanf("%s", mp[i]);

        vector<pii> vec;
        for(int i = 0; i < n; ++i)
            for(int j = 0; j < n; ++j) {
                if(mp[i][j] == '0') vec.push_back(pii(i, j));
            }

        int mask = 1 << vec.size();

        int ans = 100;
        for(int i = 0; i < mask; ++i) {
            int cnt = 0;
            for(int j = 0; j < vec.size(); ++j) if(i >> j & 1) mp[vec[j].first][vec[j].second] = '1', cnt++;

            if(check()) ans = min(ans, cnt);
            for(int j = 0; j < vec.size(); ++j) if(i >> j & 1) mp[vec[j].first][vec[j].second] = '0';
        }

        cout << ans << endl;
    }
    return 0;
}
