#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <queue>

using namespace std;

const int N = 20;
const int mod = 1000000007;

int n, m;
char str[N][1000];
int id[N];
int max_sum, ans;

struct Trie{
    int cnt, root;
    int next[1000][26];
    int new_node(){
        memset(next[cnt], -1, sizeof(next[cnt]));
        return cnt++;
    }
    void clear(){
        cnt = 0;
        root = new_node();
    }
    void ins(char *s){
        int x = root;
        for(int i = 0; s[i]; ++i){
            int c = s[i] - 'A';
            if(next[x][c] == -1) next[x][c] = new_node();
            x = next[x][c];
        }
    }
}trie[10];

bool check(){
    bool flag[10] = {0};
    for(int i = 0; i < n; ++i) flag[id[i]] = 1;
    for(int i = 0; i < m; ++i){
        if(flag[i] == 0) return true;
    }
    return false;
}
void solve(){
    if(check()) return;
    for(int i = 0; i < m; ++i) trie[i].clear();
    for(int i = 0; i < n; ++i) trie[id[i]].ins(str[i]);
    int sum = 0;
    for(int i = 0; i < m; ++i) sum += trie[i].cnt;
    if(sum > max_sum){
        max_sum = sum;
        ans = 1;
    }
    else if(sum == max_sum){
        ans++;
    }
//    if(sum == 7){
//        for(int i = 0; i < n; ++i) cout << id[i] << ' '; cout << endl;
//    }
}
void dfs(int x){
    if(x == n){
        solve();
        return;
    }
    for(int i = 0; i < m; ++i){
        id[x] = i;
        dfs(x + 1);
    }
}
int main(){
//    freopen("D-small-attempt0.in", "r", stdin);
//    freopen("D-small-attempt0.out", "w", stdout);
    int _, cas = 1;
    for(scanf("%d", &_); _--; ){
        printf("Case #%d: ", cas++);
        scanf("%d %d", &n, &m);
        for(int i = 0; i < n; ++i) scanf("%s", str[i]);
        ans = 0;
        max_sum = 0;
        dfs(0);
        cout << max_sum << ' ' << ans % mod << endl;
    }
    return 0;
}
