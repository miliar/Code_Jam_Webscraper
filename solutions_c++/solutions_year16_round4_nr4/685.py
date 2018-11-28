#include<cstdio>
int bd[4][4];
int rec[4][4];
int cnt;
int mcnt[5]={0,1,4,36,576};
int n;
int chk[4];
int chk2[4];
int seq[4];
int ccnt=0;
void dotest2(int x){
    bool chosen=false;
    if(x==n){
        return;
    }
    for(int i=0;i<n;i++){
        if(rec[seq[x]][i]){
            if(chk2[i]) continue;
            chk2[i]=1;
            chosen=true;
            dotest2(x+1);
            chk2[i]=0;
        }
    }
    if(!chosen) ccnt=1;
}

void dotest(int x){
    if(x==n){
        dotest2(0);
        return;
    }
    for(int i=0;i<n;i++){
        if(chk[i]) continue;
        chk[i]=1;
        seq[x]=i;
        dotest(x+1);
        chk[i]=0;
    }
}

int main(){
    int t;
    int mn;
    bool valid=0;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for(int turn=1;turn<=t;turn++){
        scanf("%d",&n);
        mn=(n*n)+1;
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                scanf("%1d",&bd[i][j]);
            }
        }
        //printf("!");
        for(int i=0;i<(1 << (n*n));i++){
            valid=true;
            for(int j=0;j<(n*n);j++){
                if((!((1 << j) & i))&&bd[j/n][j%n]){
                    valid=false;
                    break;
                }
            }
            if(valid){
                //printf("@\n");
                cnt=0;
                for(int j=0;j<(n*n);j++){
                    if((1 << j)&i) rec[j/n][j%n]=1;
                    else rec[j/n][j%n]=0;
                    cnt+=(rec[j/n][j%n]-bd[j/n][j%n]);
                }
                ccnt=0;
                dotest(0);
                if(ccnt==0){
                    //printf("OK\n");
                    cnt=0;
                    for(int j=0;j<(n*n);j++){
                        cnt+=(rec[j/n][j%n]-bd[j/n][j%n]);
                    }
                    /*
                    for(int j=0;j<n;j++){
                        for(int k=0;k<n;k++){
                            printf("%d",rec[j][k]);
                        }
                        printf("\n");
                    }
                    */
                    //printf("%d\n",cnt);
                    if(mn>cnt) mn=cnt;
                }
            }
        }
        printf("Case #%d: %d\n",turn,mn);
    }
}
