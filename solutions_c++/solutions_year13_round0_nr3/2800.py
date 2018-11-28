#include<stdio.h>
#include<string.h>
int is[12000];
int main(){
    freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
    int t,k,i,j,l,r,all;
    memset(is,0,sizeof(is));
    for(i=1;i<102;i++){
        is[i*i]=i;
    }
    while(scanf("%d",&t)!=EOF){
        for(k=1;k<=t;k++){
            all=0;
            printf("Case #%d: ",k);
            scanf("%d%d",&l,&r);
            for(i=l;i<=r;i++){
                if(is[i]==0) continue;
                if(i<10){
                    all+=1;
                    continue;
                }
                if(i<100){
                    if(i/10==i%10){
                        all+=1;
                    }
                    continue;
                }
                if(i<1000){
                    if(i/100==i%10){
                        if(is[i]/10==is[i]%10)
                        all+=1;
                    }
                    continue;
                }
                if(i<10000){
                    if(i/1000==i%10 && i/100%10==i/10%10){
                        if(is[i]/10==is[i]%10)
                        all+=1;
                    }
                    continue;
                }
                if(i<100000){
                    if(i/10000==i%10 && i/1000%10==i/10%10){
                        all+=1;
                    }
                    continue;
                }
            }
            printf("%d\n",all);
        }
    }
}
