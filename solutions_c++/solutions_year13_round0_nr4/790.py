#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

int k, n;
int keys[300], open[300], in[300], c[300][300];
bool searched[1<<20];

void init()
{
     int x;
     scanf("%d%d", &k, &n);
     memset(keys, 0, sizeof(keys));
     for (int i  = 0; i < k; ++i){
         scanf("%d", &x);
         keys[x]++;
     }
     for (int i = 1; i <= n; ++i){
         scanf("%d", &open[i]);
         scanf("%d", &in[i]);
         for (int j = 0; j < in[i]; ++j)
             scanf("%d", &c[i][j]);
     }         
}

int way[300];
bool mark[300];
bool search(int v, int st)
{
     if (v > n){
        return true;         
     }     
     if (searched[st]) return false;
     searched[st] = true;
     for (int i = 1; i <= n; ++i)
         if (!mark[i] && keys[open[i]] > 0){
            way[v] = i;
            mark[i] = true;
            keys[open[i]]--;
            for (int j = 0; j < in[i]; ++j) keys[c[i][j]]++;
            if (search(v+1, (st | (1<<(i-1))))) return true;
            for (int j = 0; j < in[i]; ++j) keys[c[i][j]]--;
            keys[open[i]]++;
            mark[i] = false;                   
         }
     return false;
}
     
void work()
{
     memset(mark, 0, sizeof(mark));
     memset(way, 0, sizeof(way));
     memset(searched, 0, sizeof(searched));
     if (search(1, 0)){
        for (int i = 1; i <= n; ++i)
            printf(" %d", way[i]);
        printf("\n");              
     }     
     else
         printf(" IMPOSSIBLE\n");
}
          
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int cases = 0;
    int i = 0;
    scanf("%d", &cases);
    while (cases--){
          ++i;
          printf("Case #%d:", i);
          init();
          work();      
    }
    return 0;
}
