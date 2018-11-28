#include<stdio.h>
#include<iostream>
#include<vector>
#include<cstring>
using namespace std;

int ans = 2147483647;
int weight[10010];
int disk;
int state[10010];
int n;
void dfs(int i, int w){

    if(i == n){
        ans = min(ans, w);
        return;
    }
    if(state[i] == 0){

        state[i] = 1;
        dfs(i+1,w+1);
        for(int x = i+1;x <n;x++)
        if(state[x]==0 && weight[i] + weight[x] <=disk){
            state[x] = 1;
            dfs(i+1,w+1);
            state[x] = 0;
        }
        state[i] = 0;
    }else dfs(i+1,w);
}
int main(){
    int T;scanf("%d",&T);
    for(int _ = 1; _<=T;_++){
        scanf("%d%d",&n,&disk);
        for(int i = 0; i < n ;i++) scanf("%d",&weight[i]);
        printf("Case #%d: ",_);
        memset(state,0,sizeof(state));
        ans = 0;
        for(int i = 0 ;i <n;i++){
            if(state[i] == 0){
                int value = -1, id =-1;
                for(int j = i+1;j<n;j++)
                    if(weight[j] + weight[i] <= disk && state[j] == 0){
                        if(value < weight[j]){value = weight[j]; id = j;}
                    }
                state[i] = 1;
                if(id !=-1){
                    state[id] = 1;
                }
                ans++;
            }
        }
        //dfs(0,0);
        printf("%d\n",ans);
    }
    return 0;
}
