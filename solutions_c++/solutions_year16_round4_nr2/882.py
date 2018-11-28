#include<cstdio>
int bae[18];
double prob[18];
double calc,sum;
double mx=0;
int main(){
    int t,n,kk,cnt,cnt2;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for(int turn=1;turn<=t;turn++){
        mx=0;
        scanf("%d %d",&n,&kk);
        for(int i=0;i<n;i++){
            scanf("%lf",&prob[i]);
            //printf("%f\n",prob[i]);
        }
        for(int j=0;j<(1 << n);j++){
            cnt=0;
            for(int k=0;k<n;k++){
                if(j & (1 << k)){
                    bae[cnt++]=k;
                }
            }
            if(cnt==kk){
                /*
                for(int j2=0;j2<kk;j2++){
                    printf("%d%f ",bae[j2],prob[bae[j2]]);
                }
                printf("\n");
                */
                sum=0;
                for(int j2=0;j2<(1 << kk);j2++){
                    calc=1.0;
                    cnt2=0;
                    for(int k2=0;k2<kk;k2++){
                        if(j2 & (1 << k2)){
                            calc*=prob[bae[k2]];
                            cnt2++;
                        }else{
                            calc*=(1-prob[bae[k2]]);
                        }
                    }
                    //printf("%f",calc);
                    if(cnt2==kk/2) sum+=calc;
                }
                if(mx<sum) mx=sum;
            }
        }
        printf("Case #%d: %f\n",turn,mx);
    }
}
