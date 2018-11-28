#include<cstdio>

int bae[21][1000];
int cnt,n;
int mn=9;
int offset[10]={0,1,2,3,3,4,4,5,5,5};

void rec(int tm){
    bool fin=true;
    int i,j,k,mx=0;
    //printf("%d\n",tm);
    for(i=0;i<n;i++){
       // printf("%d ",bae[tm][i]);
        if(bae[tm][i]>mx) mx=bae[tm][i];
    }
    //printf("\n");
    if(tm+offset[mx]>mn) return;
    if(mx==0){
        if(mn>tm){
            mn=tm;
        }
        return;
    }else{
        for(i=0;i<n;i++){
            if(bae[tm][i]==0) bae[tm+1][i]=0;
            else bae[tm+1][i]=bae[tm][i]-1;
        }
        rec(tm+1);
        for(i=0;i<n;i++){
            n++;
            for(j=0;j<n;j++){
                bae[tm+1][j]=bae[tm][j];
            }
            for(k=1;k<bae[tm][i];k++){
                bae[tm+1][n-1]=k;
                bae[tm+1][i]=bae[tm][i]-k;
                rec(tm+1);
            }
            n--;
        }
    }
}

int main(){
    int t,turn,i;
    scanf("%d",&turn);
    //freopen("dap3.txt","w",stdout);
    for(t=1;t<=turn;t++){
        scanf("%d",&n);
        cnt=n;
        mn=10;
        for(i=0;i<n;i++) scanf("%d",&bae[0][i]);
        rec(0);
        printf("Case #%d: %d\n",t,mn);
    }
}
