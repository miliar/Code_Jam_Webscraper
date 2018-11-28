#include<stdio.h>
int main(){
    int sum,f,t,i,smax,shy_lvl,j;
    freopen("a2.in", "r", stdin);
    freopen("a2.out", "w", stdout);
    char c;
    scanf("%d",&t);
    for(i=1;i<=t;i++){
        sum=0;
        f=0;
        scanf("%d",&smax);
        scanf("%1d",&sum);  //no of people with 0 shy level
        if(smax==0)
            f=0;
        else{
            for(j=1;j<=smax;j++){
                scanf("%1d",&shy_lvl);
                if(shy_lvl!=0){
                if(sum<j){
                    f=f+j-sum;
                    sum+=f;
                }
                sum+=shy_lvl;
                }
            }
        }
        printf("Case #%d: %d\n",i,f);
        scanf("%c",&c);
    }
    return 0;
}
