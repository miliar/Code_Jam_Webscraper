//
//  main.cpp
//  gcj
//
//  Created by Jinfu Leng on 4/11/14.
//  Copyright (c) 2014 jinfu. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;

int firstCards[4][4], secondCards[4][4];
int ans;
int Cnt(int first, int second){
    int cnt=0;
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
            //printf("%d %d\n",firstCards[first-1][i],secondCards[second-1][j]);
            if(firstCards[first-1][i]==secondCards[second-1][j]){
                ans=firstCards[first-1][i];
                cnt++;
            }
        }
    }
    //printf("%d\n",cnt);
    return cnt;
}
int main(int argc, const char * argv[])
{
    freopen("/Users/jinfu/Workspace/test/input.in","r",stdin);
    freopen("/Users/jinfu/Workspace/test/output","w",stdout);
    int T;
    scanf("%d",&T);
    for(int t=0;t<T;t++){
        printf("Case #%d: ",t+1);
        int first,second;
        scanf("%d",&first);
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                scanf("%d",&firstCards[i][j]);
            }
        }
        scanf("%d",&second);
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                scanf("%d",&secondCards[i][j]);
            }
        }
        int cnt=Cnt(first,second);
        if(cnt==0)
            printf("Volunteer cheated!\n");
        else if(cnt==1)
            printf("%d\n",ans);
        else
            printf("Bad magician!\n");
    }
    return 0;
}

