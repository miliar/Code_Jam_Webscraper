#include<stdio.h>
int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int k,c,s,tt,i,test;
    scanf("%d",&tt);
    for(test=1;test<=tt;test++){
        scanf("%d %d %d",&k,&c,&s);
        printf("Case #%d: ",test);
        for(i=1;i<=k;i++)   printf("%d ",i);
        printf("\n");
    }
    return 0;
}
