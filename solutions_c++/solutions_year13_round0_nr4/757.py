#include <iostream>
#include <vector>
#include <string>
#include <stdio.h>
#include <cmath>
#include <algorithm>
#include <utility>
#include <cstring>
#include <queue>

using namespace std;

#define INF 1<<30

int chests[210];
vector<int> ck[210];
int keys[210];
int placed[210];
int N,K,a,b;
int t,k;
int placement[210];
int dp[1<<21];
int recurse(int depth, int mask){
    if(dp[mask] != 0) return false;
    if(depth == N){
        return true;
    }
    for(int i = 1; i <= N; i++){
        // go to next case and open keys
        if(keys[chests[i]] > 0 && !placed[i]){
            keys[chests[i]]--;
            for(int j = 0; j < ck[i].size(); j++){
                keys[ck[i][j]]++;   
            }
            placed[i] = true;
            placement[depth] = i;
            if(recurse(depth+1, mask|1<<i)) return true;
            keys[chests[i]]++;
            for(int j = 0; j < ck[i].size(); j++){
                keys[ck[i][j]]--;   
            }
            placed[i] = false;
            
        }
    }
    dp[mask] = 1;
    return false;
    
}

int main()
{
    int casenum = 1;
    int TC;
    
    scanf("%d\n",&TC);
    while(TC--){
        scanf("%d %d",&K,&N);
        memset(keys,0,sizeof(keys));
        memset(dp,0,sizeof(dp));
        for(int i = 0; i < K; i++){
            scanf("%d",&a);
            keys[a]++;
        }
        for(int i = 1; i <= N; i++){
            scanf("%d %d",&t,&k);
            chests[i] = t;
            ck[i].clear();
            for(int j = 0; j < k; j++){
                scanf("%d",&a);
                ck[i].push_back(a);
                
            }
            sort(ck[i].begin(),ck[i].end());
        }
        
        memset(placed,0,sizeof(placed));
        bool found = recurse(0,0);
        if(found){
           
            printf("Case #%d:",casenum++);  
            for(int i = 0; i < N; i++) printf(" %d",placement[i]);
            printf("\n");
        }else{
            printf("Case #%d: IMPOSSIBLE\n",casenum++);   
        }
    }
    return 0;
}
