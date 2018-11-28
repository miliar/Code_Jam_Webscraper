#include<stdio.h>
int T,N,M[10000];
int main(){
    int maxx=0,interval,res1,res2;
    scanf("%d",&T);
    for(int tc=1;tc<=T;tc++){
        scanf("%d",&N);
        res1=0; res2=0;
        interval=0;
        for(int i=0;i<N;i++) scanf("%d",&M[i]);
        maxx=M[0];
        for(int i=1;i<N;i++){
            if(M[i]>M[i-1]){
                res1+=maxx-M[i-1];
                maxx=M[i];
            }
            else if(i==N-1){
                res1+=maxx-M[i];
            }
        }
        for(int i=0;i<N-1;i++){
            if(M[i]-M[i+1]>interval) interval=M[i]-M[i+1];
        }
        for(int i=0;i<N-1;i++){
            if(M[i]<interval) res2+=M[i];
            else res2+=interval;
        }
        printf("Case #%d: %d %d\n",tc,res1,res2);
    }
}
