#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
const int MAXM = 1000+5, MAXN = 100+5, MAXK = 100000+5;
int T, M, N;
char S[MAXM][100+5];
int nv, chd[MAXK][26];
int ans[2];
vector<int> vec[MAXN];
bool check() {
    for (int i = 0; i < N; i++) {
        if (!vec[i].size())
            return 0;
    }
    return 1;
}
int addNode() {
    memset(chd[nv], -1, sizeof(chd[nv]));
    return nv++;
}
int count(int n) {
    nv = 0;
    addNode();
    for (int j = 0; j < (int)vec[n].size(); j++) {
        int len = strlen(S[vec[n][j]]), cur = 0;
        for (int i = 0; i < len; i++) {
            int ch = S[vec[n][j]][i]-'A';
            if (chd[cur][ch] == -1) {
                int u = addNode();
                chd[cur][ch] = u;
                cur = u;
            } else {
                cur = chd[cur][ch];
            }
        }
    }
    return nv;
}
void dfs(int x) {
    if (x == M) {
        if (!check())
            return;
        int sum = 0;
        for (int i = 0; i < N; i++) {
            sum += count(i);
        }
        if (sum > ans[0]) {
            ans[0] = sum;
            ans[1] = 1;
        } else if (sum == ans[0]) {
            ans[1]++;
        }
        return;
    }
    for (int i = 0; i < N; i++) {
        vec[i].push_back(x);
        dfs(x+1);
        vec[i].pop_back();
    }
}
int main() {
    freopen("D-small-attempt1.in", "r", stdin);
    freopen("b.txt", "w", stdout);
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        scanf("%d%d", &M, &N);
        for (int i = 0; i < M; i++) {
            scanf("%s", S[i]);
        }
        ans[0] = 0;
        dfs(0);
        printf("Case #%d: %d %d\n", cas, ans[0], ans[1]);
    }
    return 0;
}
