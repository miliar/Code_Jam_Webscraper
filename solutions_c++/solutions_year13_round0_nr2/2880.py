#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<list>
#include<utility>
#include<string.h>
using namespace std;
int target[105][105],lawn[105][105];
int rmins[104], cmins[104];
int rmaxs[104], cmaxs[104];
int main(){
    freopen("b-large.in","r",stdin);
    freopen("b-lage.out","w",stdout);
    int T,N,M, h;
    scanf("%d", &T);
    for(int c=0;c<T;c++){
        scanf("%d %d",&N,&M);
        fill(rmaxs,rmaxs + 104,-1); fill(cmaxs,cmaxs + 104,-1);
        for(int i=0;i<N;i++){
            for(int j=0;j<M;j++){
                scanf("%d",&h);
                lawn[i][j] = 100, target[i][j] = h;
                rmaxs[i] = max(rmaxs[i], h); cmaxs[j] = max(cmaxs[j], h);
            }
        }
        bool possible = true;
        for(int i=0;i<N && possible;i++){
            for(int j=0;j<M && possible;j++){
                if(lawn[i][j]!=target[i][j]){
                    if(target[i][j]<rmaxs[i]){
                        if(target[i][j]<cmaxs[j]){
                            possible = false;
                        }
                        else{
                            for(int k=0;k<N;k++) lawn[k][j] = target[i][j];
                        }
                    }
                    else{
                        for(int k=0;k<M;k++) lawn[i][k] = target[i][j];
                    }
                }
            }
        }
        if(possible) printf("Case #%d: YES\n",c+1);
        else printf("Case #%d: NO\n",c+1);
    }
    return 0;
}
