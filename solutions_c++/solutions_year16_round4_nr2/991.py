#include<stdio.h>
#include<string.h>
#include<memory.h>
FILE *fo = fopen("/Users/JungRockJoon/Desktop/Rock/Algorithm/Codejam2016/Round2/2/input.txt","r");
FILE *fp = fopen("/Users/JungRockJoon/Desktop/Rock/Algorithm/Codejam2016/Round2/2/output.txt","w");
int t,T,N,K,mid = 20,len[20];
double l[20];
double Max;
void search(int now,int cnt){
    if(cnt == K){
        int i,j;
        double D[40],D2[40];
        for(j=0;j<40;j++)
            D2[j] = D[j] = 0;
        D[mid] = 1.0;
        for(i=0;i<now;i++){
            if(len[i] == 1){
                for(j=0;j<40;j++)
                    D2[j] = 0;
                for(j=1;j<39;j++){
                    D2[j+1] += D[j] * l[i];
                    D2[j-1] += D[j] * (1.0 - l[i]);
                }
                for(j=0;j<40;j++) {
                    D[j] = D2[j];
                }
            }
        }
        if(Max < D[mid]) Max = D[mid];
        return;
    }
    if(now != N){
        len[now] = 1;
        search(now+1,cnt+1);
        len[now] = 0;
        search(now+1,cnt);
        len[now] = 0;
    }
}
int main(){
    fscanf(fo,"%d",&T);
    for(t=1;t<=T;t++){
        memset(l,0,sizeof(l));
        memset(len,0,sizeof(len));
        int i,j;
        fscanf(fo,"%d %d",&N,&K);
        for(i=0;i<N;i++){
            fscanf(fo,"%lf",&l[i]);
        }
        Max = 0.0;
        search(0,0);
        fprintf(fp,"Case #%d: %.8lf\n",t,Max);
    }
    return 0;
}