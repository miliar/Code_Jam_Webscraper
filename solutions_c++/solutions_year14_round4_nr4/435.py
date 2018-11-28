#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <queue>
using namespace std;
const int sigma_sz = 26;
const int maxnode = 10000+10;
struct Trie{
    int ch[maxnode][sigma_sz];
    int val[maxnode],sz;
    int idx(char c) {
        return c - 'A';
    }
    void init(){
        sz = 1;
        memset(ch[0],0,sizeof(ch[0]));
        memset(val,0,sizeof(val));
    }
    void insert(char *s) {
        int  n = strlen(s), u = 0;
        for (int i = 0; i < n; i++) {
            int c = idx(s[i]);
            if (ch[u][c] == 0) {
                memset(ch[sz],0,sizeof(ch[sz]));
                ch[u][c] = sz++;
            }
            u = ch[u][c];
        }
        val[u]++;
    }
}Rabbit[5];
char s[10][11];
int n, m;
int a[10];
int ans, num;
int fg[10];
void work() {
    memset(fg, 0, sizeof(fg));
    for (int i = 0; i < n; i++) fg[a[i]] = 1;
    for (int i = 0; i < m; i++) if (fg[i] == 0) return;

    for (int i = 0; i < m; i++) Rabbit[i].init();
    for (int i = 0; i < n; i++) {
        Rabbit[a[i]].insert(s[i]);
    }
    int sum = 0;
    for (int i = 0; i < m; i++) {
        sum += Rabbit[i].sz;
    }
    if (sum > ans) {
        ans = sum;
        num = 1;
    }else if (sum == ans) {
        num++;
    }
}
void dfs(int d) {
    if (d == n) {
        work();
        return;
    }
    for (int i = 0; i < m; i++) {
        a[d] = i;
        dfs(d+1);
    }
}
void solve() {
    ans = 0;
    num = 0;
    dfs(0);
    printf("%d %d\n",ans, num);
}
int main() {
  //  cout << ('Z' - 'A') << endl;
    freopen("D-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T, cas = 0; scanf("%d",&T);
    while (T--) {
        scanf("%d%d",&n,&m);
        for (int i = 0; i < n; i++) scanf("%s",s[i]);
        printf("Case #%d: ",++cas);
        solve();
    }
    return 0;
}
