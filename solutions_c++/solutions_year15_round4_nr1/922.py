#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

char s[105][105];
int N,M,ans;
int op[4][2]={{-1,0},{1,0},{0,-1},{0,1}};

bool ok(){
    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            if(s[i][j]=='.')    continue;
            int has = 0;
            for(int k=0;k<4 && has==0;k++){
                int x = i+op[k][0], y = j+op[k][1], yes = 0;
                while(x>=0 && x<N && y>=0 && y<M && yes==0){
                    if(s[x][y]!='.')    yes = 1;
                    x += op[k][0], y += op[k][1];
                }
                if(yes==1)  has = 1;
            }
            if(has==0)  return false;
            int kk;
            if(s[i][j]=='>')    kk = 3;
            else if(s[i][j]=='<')   kk = 2;
            else if(s[i][j]=='^')   kk = 0;
            else kk = 1;
            int x = i+op[kk][0], y = j+op[kk][1];
            has = 0;
            while(x>=0 && x<N && y>=0 && y<M && has==0){
                if(s[x][y]!='.')    has = 1;
                x += op[kk][0], y += op[kk][1];
            }
            if(has==0)  ans++;
        }
    }
    return true;
}

int main(){
    
    int T;
    scanf(" %d",&T);
    for(int t=0;t<T;t++){
        scanf(" %d %d",&N,&M);
        for(int i=0;i<N;i++)
            scanf(" %s",s[i]);
        ans = 0;
        if(!ok())   printf("Case #%d: IMPOSSIBLE\n",t+1);
        else{
            printf("Case #%d: %d\n",t+1,ans);
        }
    }

    return 0;
}
