#include<fstream>
#include<stdlib.h>
#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
using namespace std;
long long int p=0,A=0;
int main () {

    freopen("Google Code Jam Q-C.txt","r",stdin);
    freopen("Google Code Jam Q-C OUT.txt","w",stdout);
    scanf("%d",&A);
    for(p=1;p<=A;p++){
        bool FUCKED=0;
        int N=0,M=0,i=0,j=0,bC=0,bR=0;
        int map[104][104]={0};
        int maxC[104]={0};
        int maxR[104]={0};
        scanf("%d %d",&N,&M);
        for(i=1;i<=N;i++){
            for(j=1;j<=M;j++){
                scanf("%d",&map[i][j]);
            }
        }
        for(i=1;i<=N;i++){
            bR=0;
            for(j=1;j<=M;j++){
                if(map[i][j]>bR){bR=map[i][j];}
            }
            maxR[i]=bR;
        }

        for(j=1;j<=M;j++){
            bC=0;
            for(i=1;i<=N;i++){
                if(map[i][j]>bC){bC=map[i][j];}
            }
            maxC[j]=bC;
        }

        for(i=1;i<=N;i++){
            for(j=1;j<=M;j++){
                if(map[i][j]!=maxC[j]&&map[i][j]!=maxR[i]){
                    FUCKED=1;
                    break;
                }
            }
        }
        if(FUCKED==1){printf("Case #%d: NO\n",p);}
        else{printf("Case #%d: YES\n",p);}
    }
    return 0;
}
