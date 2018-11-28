#include<stdio.h>
#include<string.h>
#define N 501

int n,chk[10];
int kk[1000],sum[1000][1000];
char arr[1000];

int is_fs(int x,int b,int a){
    int i,p=0,cut=0;

    for(i=0;i<x;i++){
        sum[a][i]=kk[i]*b+cut;
        cut=sum[a][i]/10;
        sum[a][i]%=10;
        chk[sum[a][i]]=1;
        if(i==x-1 && cut>0)x++;
    }
    for(i=0;i<10;i++){
        if(chk[i]==0)return 0;
    }
    return x;
}
int g(){
    for(int i=0;i<10;i++)chk[i]=0;
}
int main(void){
    int i,j,k,T,tot,p;

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    scanf("%d",&T);
    for(i=1;i<=T;i++){
        scanf("%s",arr);
        g();
        n=strlen(arr);
        for(j=0,p=n-1;j<n;j++,p--){
            kk[p]=arr[j]-48;
        }
        for(j=n;j<N;j++){
            kk[j]=0;
        }
        printf("Case #%d: ",i);
        for(j=1;j<=N;j++){
            tot=is_fs(n,j,i);
            if(tot>0){
                for(k=tot-1;k>=0;k--){
                    printf("%d",sum[i][k]);
                }
                break;
            }
            if(j==N){
                printf("INSOMNIA");
                break;
            }
        }
        printf("\n");
    }
}
