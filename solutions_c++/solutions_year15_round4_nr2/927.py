#include<stdio.h>

int q,k,n,i,j,hup,hlow;
double rup,rlow,mid,rcup,c,r,rclow,t,mn,x,y;

int main(){
    scanf("%d",&q);
    for(k=1;k<=q;k++){
        scanf("%d %lf %lf",&n,&x,&y);
        rlow=0;
        rclow=0;
        rup=0;
        rcup=0;
        mid=0;
        for(i=0;i<n;i++){
            scanf("%lf %lf",&r,&c);
            if(c<y){
                rlow+=r;
                rclow+=r*(c-y);
            }
            else if(c>y){
                rup+=r;
                rcup+=r*(c-y);
            }
            else{
                mid+=r;
            }
        }
        if(rup==0||rlow==0){
            if(mid==0){
                printf("Case #%d: IMPOSSIBLE\n",k);
                continue;
            }
            else{
                printf("Case #%d: %lf\n",k,x/mid);
                continue;
            }
        }
        if(rcup+rclow>0){
            rlow+=mid;
            t=(x*(rcup/rup)/(rcup/rup-rclow/rlow))/rlow;
        }
        else{
            rup+=mid;
            t=(x*(rclow/rlow)/(rclow/rlow-rcup/rup))/rup;
        }
        printf("Case #%d: %lf\n",k,t);
    }
}
