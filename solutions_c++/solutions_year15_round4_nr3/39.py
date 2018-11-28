#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cstring>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
#define SIZE(x) (int((x).size()))
#define rep(i,l,r) for (int i=(l); i<=(r); i++)
#define repd(i,r,l) for (int i=(r); i>=(l); i--)
#define rept(i,c) for (typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#ifndef ONLINE_JUDGE
#define debug(x) { cerr<<#x<<" = "<<(x)<<endl; }
#else
#define debug(x) {}
#endif
#define MAXN 4010
vector<int> edg[MAXN];
int l[MAXN][MAXN];
int vis[MAXN];
int n,m;
int S = 0, T = 1;
map<string, int> mp;
char inp[20];
int INF = MAXN;
void addE(int s, int t, int v) {
    edg[s].push_back(t);
    edg[t].push_back(s);
    l[s][t] = v;
}
int dfs(int u) {
    vis[u] = 1;
    if (u == T) return 1;
    rep(i,0,SIZE(edg[u])-1) {
        int v = edg[u][i];
        if (l[u][v] && !vis[v]) {
            if (dfs(v)) {
                l[u][v] --;
                l[v][u] ++;
                return 1;
            }
        }
    }
    return 0;
}
void printG() {
    puts("---");
    rep(i,0,n-1) {
        rep(j,0,n-1) {
            if (l[i][j] > 1) printf("%d %d I\n",i,j);
            else if (l[i][j] != 0)printf("%d %d %d\n", i,j,l[i][j]);
        }
    }
}
void lemon() {   
    int nn; 
    scanf("%d",&nn);
    n=2;
    m=0;
    mp.clear();
    memset(l,0,sizeof(l));
    rep(i,0,MAXN-1)edg[i].clear();
    while(1) {
        char wc;
        scanf("%s%c",inp,&wc);
        string st = string(inp);
        //puts(inp);
        if (mp.find(st) == mp.end()) {
            addE(n, n+1, 1);
            mp[st] = n++;
            n++;
        }
        addE(S, mp[st], INF);
        if (wc != ' ') break;
    }
    //puts("---");
    while(1) {
        char wc;
        scanf("%s%c",inp,&wc);
        //puts(inp);
        string st = string(inp);
        if (mp.find(st) == mp.end()) {
            addE(n, n+1, 1);
            mp[st] = n++;
            n++;
        }
        addE(mp[st]+1, T, INF);
        if (wc != ' ') break;
    }
    //puts("---");
    rep(i,2,nn-1) {
        vector<int> v;
        while(1) {
            char wc;
            scanf("%s%c",inp,&wc);
            //puts(inp);
            string st = string(inp);//puts(inp);
            if (mp.find(st) == mp.end()) {
                addE(n, n+1, 1);
                mp[st] = n++;
                n++;
            }
            v.push_back(mp[st]);
            if (wc != ' ') break;
        }
        rep(j,0,SIZE(v)-1) {
            rep(k,j+1,SIZE(v)-1) {
                addE(v[j]+1, v[k], INF);
                addE(v[k]+1, v[j], INF);
            }
        }
    }
    int ans = 0;
    while (1) {
        //printG();
        memset(vis, 0, sizeof(vis));
        if (dfs(S)) ans++;
        else break;
    }
    printf("%d\n", ans);
}
int main() {
    ios::sync_with_stdio(true);
    #ifndef ONLINE_JUDGE
    //    freopen("","r",stdin);
    #endif
    int cas;
    scanf("%d",&cas);
    rep(i,1,cas) {
    	printf("Case #%d: ",i);
    	lemon();
    }
    return 0;
}