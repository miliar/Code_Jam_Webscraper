#pragma  comment(linker, "/STACK:36777216")
#include <map>
#include <set>
#include <cmath>
#include <ctime>
#include <queue>
#include <stack>
#include <cstdio>
#include <string>
#include <vector>
#include <iomanip>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#define  lc(x) (x << 1)
#define  rc(x) (lc(x) + 1)
#define  lowbit(x) (x & (-x))
#define  PI    (acos(-1))
#define  lowbit(x) (x & (-x))
#define  EPS   1e-10
#define  MAXN  1005
#define  MAXM  2005
#define  LL    long long
#define  DB    double
#define  ULL   unsigned long long
#define  INF   0x7fffffff
#define  pb    push_back
#define  mp    make_pair
#define  MOD   1000000007

using namespace std;

struct tree{
    int son[27];
} tree[6][MAXN];

int sz[6];

void insert(int id, char *word){
     int p = 0;
     for(int i = 0, l = strlen(word); i < l; i ++){
        int tmp = word[i] - 'A' + 1;
        if(!tree[id][p].son[tmp])
            tree[id][p].son[tmp] = ++ sz[id];
        p = tree[id][p].son[tmp];
     }
}

int id[10], n, m, ans, mx, sum[10];

char ch[10][15];

void dfs(int pos){
    if(pos == m + 1){
        for(int i = 1; i <= n; i ++) if(sum[i] == 0) return;
        for(int i = 1; i <= m; i ++) insert(id[i], ch[i]);

        int res = 0;
        for(int i = 1; i <= n; i ++) res += sz[i] + 1;
        if(res > mx) mx = res, ans = 1;
        else if(res == mx) ans ++;

        for(int i = 1; i <= n; i ++){
            for(int j = 0; j <= sz[i]; j ++)
                for(int k = 0; k < 27; k ++) tree[i][j].son[k] = 0;
            sz[i] = 0;
        }
        return;
    }
    for(int i = 1; i <= n; i ++){
        id[pos] = i, sum[i] ++;
        dfs(pos + 1);
        sum[i] --;
    }
}

int t, cas;

int main(){
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D.out", "w", stdout);
    cin >> t;
    while(t --){
        cin >> m >> n;
        for(int i = 1; i <= m; i ++) scanf(" %s", &ch[i]);
        mx = 0, ans = 0;
        dfs(1);
        printf("Case #%d: %d %d\n", ++ cas, mx, ans);
    }
}
