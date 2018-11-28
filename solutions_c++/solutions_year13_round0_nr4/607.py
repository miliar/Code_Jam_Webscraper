#include<cstdio>
#include<cstring>
#include<iostream>
#include<cmath>
#include<algorithm>
#include<string>
#include<map>
#include<set>
using namespace std;
const int MAXN = 20 + 2;
multiset<int> key[1000], have[100];
set<int>::iterator iter;
bool g[4000000], f[4000000];
int n, k;
int cf[MAXN], a[MAXN];


void cal(int c, int v, int t)
{
     for (iter = key[v].begin(); iter != key[v].end(); iter++)
         if (t > 0)
            have[c].insert(*iter);
         else have[c].erase(have[c].find(*iter));
} 

void dfs(int x, int c)
{
     g[x] = true;
     int i, y;
     have[c].clear();
     cal(c, n, 1);
     for (i = 0; i < n; i++)
         if (x & cf[i]){
            cal(c, i, 1);
         }
     for (i = 0; i < n; i++)
         if (x & cf[i])
            have[c].erase(have[c].find(a[i]));
     for (i = 0; i < n; i++)
         if ((x & cf[i]) == 0)
            if (have[c].find(a[i]) != have[c].end()){
            y = x + cf[i];
            if (g[y] == false)
               dfs(y, c + 1);
            if (f[y] == true){
               f[x] = true; return;
            } 
         }
}

int main()
{
    int ts, ks, x, i, v, j;
    
    freopen("D.in", "r", stdin);
    freopen("D.out", "w", stdout);
    cf[0] = 1;
    for (i = 1; i < MAXN; i++) cf[i] = cf[i - 1] * 2;
    scanf("%d", &ts);
    for (ks = 0; ks < ts; ks++){
        scanf("%d %d", &k, &n);
        key[n].clear();
        for (i = 0; i < k; i++){
            scanf("%d", &x);
            key[n].insert(x);
        }
        for (i = 0; i < n; i++){
            key[i].clear();
            scanf("%d %d", &a[i], &v);
            for (j = 0; j < v; j++){
                scanf("%d", &x);
                key[i].insert(x);
            }
        }
        memset(f, false, sizeof(f));
        memset(g, false, sizeof(g));
        g[cf[n] - 1] = true; f[cf[n] - 1] = true;
        dfs(0, 0);
        
        if (f[0]){
           printf("Case #%d:", ks + 1);
           x = 0;
           while (x < cf[n] - 1){
                 for (i = 0; i < n; i++)
                     if ((cf[i] & x) == 0) 
                        if (f[cf[i] | x]){
                           x = cf[i] | x;
                           printf(" %d", i + 1);
                        }
           }
           printf("\n");
        }
        else printf("Case #%d: IMPOSSIBLE\n", ks + 1);
    }
    return 0;
}
