#include<stdio.h>
#include<iostream>
using namespace std;
int N,M;
int rr[100][100];
int cc(int i,int j){
    int z;
    int element = rr[i][j];
    for(z=0;z<N;z++){

                     if(rr[z][j]>element){
                                      return 0;
                                      }
                     }
                     return 1;

    }
int main(){
int T,i,j,tt,s=1;
scanf("%d",&T);
for(tt=1;tt<=T;tt++){
scanf("%d%d",&N,&M);
for(i=0;i<N;i++){
                 for(j=0;j<M;j++)
                 scanf("%d",&rr[i][j]);
                 }
for(i=0;i<N;i++){

                 int maximum = rr[i][0];
                 for(j=0;j<M;j++){
                                  if(rr[i][j]>maximum)
                                  maximum = rr[i][j];
                                  }
                 for(j=0;j<M;j++){
                                  if(rr[i][j]<maximum)
                                  s = cc(i,j);
                                  if(s==0)
                                  break;

                                  }
                 if(s==0)
                 break;
                 }
                 if(s==1)
                 printf("Case #%d: YES\n",tt);
                 else
                 {printf("Case #%d: NO\n",tt);
                  s = 1;
                  }

}
return 0;
}
