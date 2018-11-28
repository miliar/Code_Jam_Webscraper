#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<cstring>

using namespace std;





int main(){

    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w+",stdout);

    long long K,C,S;
    int n;

    while(scanf("%d",&n)==1){

        for(long long i=1;i<=n;i++){
            scanf("%lld%lld%lld",&K,&C,&S);
            printf("Case #%d: ",i);
            //if(K==1)printf("IMPOSSIBLE");
            //else{
                for(long long k=1;k<=S;k++){
                    printf("%d ",k);
                }
            //}
            printf("\n");
        }
    }


    return 0;
}
