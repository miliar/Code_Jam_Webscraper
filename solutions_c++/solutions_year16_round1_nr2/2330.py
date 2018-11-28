/*
 *
 * Tag: Implementation
 * Time: O(n)
 * Space: O(n)
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <climits>
#include <string>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <unordered_map>
#include <unordered_set>
using namespace std;
const int N = 10010000;
const int M = 110;
const long long MOD = 1000000007;
const double eps = 1e-10;
int n;
int a[M][M], sav[M][M], ans[M];
bool vis[M], isfind, miscol[M];

bool valichk(int idx, int tidx){
    for (int j = 0; j < n; ++ j) {
        if (sav[idx-1][j] >= a[tidx][j]) {
            return false;
        }
    }
    return true;
}

void print(){
    for (int i = 0; i < n; ++ i) {
        for (int j = 0; j < n; ++ j) {
            printf("%d ",sav[i][j]);
        }
        puts("");
    }
    puts("");
}

bool check(){
//    print();
    memset(miscol, 0, sizeof(miscol));
    for (int i = 0; i < 2*n - 1; ++ i) {
        if (!vis[i]) {
       //     printf(" i = %d\n",i);
            bool findcol = false;
           //
            for (int j = 0; j < n; ++ j) {
                if (miscol[j]) {
                    continue;
                }
                int k = 0;
                for (k = 0; k < n; ++ k) {
     //               printf("%d -- %d\n",sav[k][j],a[i][k]);
                    if(sav[k][j] != a[i][k]){
                        break;
                    }
                }
                if (k >= n) {
                    miscol[j] = 1;
                    findcol = true;
                    break;
                }
            }
            if (!findcol) {
                return false;
            }
      //      puts("");
     //       puts("");
            //
        }
    }
    for (int i = 0; i < n; ++ i) {
        if (!miscol[i]) {
            for (int j = 0; j < n; ++ j) {
                ans[j] = sav[j][i];
            }
        }
    }
    return true;
}

void dfs(int dep){
    if (dep == n) {
        if (check()) {
            isfind = true;
        }
        return ;
    }
    
    for (int i = 0; i < 2*n - 1; ++ i) {
        if (!vis[i] && valichk(dep, i)) {
            vis[i] = 1;
            for (int j = 0; j < n; ++ j) {
                sav[dep][j] = a[i][j];
            }
            dfs(dep + 1);
            if (isfind) {
                return;
            }
            vis[i] = 0;
        }
    }
}

int main() {
    freopen("/Users/ybc/Project/CCPP/ACM/B-small-attempt0.in", "r", stdin);
    freopen("/Users/ybc/Project/CCPP/ACM/out.txt", "w", stdout);
    int T;
    scanf("%d",&T);
    for (int cas = 1; cas <= T; ++ cas) {
        scanf("%d",&n);
        memset(vis, 0, sizeof(vis));
        isfind = false;
        for (int i = 0; i < 2*n-1; ++ i) {
            for (int j = 0; j < n; ++ j) {
                scanf("%d",&a[i][j]);
            }
        }
        for (int i = 0; i < 2*n - 1; ++ i) {
            vis[i] = 1;
            for (int j = 0; j < n; ++ j) {
                sav[0][j] = a[i][j];
            }
            dfs(1);
            if (isfind) {
                break;
            }
            vis[i] = 0;
        }
        printf("Case #%d:", cas);
        for (int i = 0; i < n; ++ i) {
            printf(" %d", ans[i]);
        }
        puts("");
    }
    return 0;
}