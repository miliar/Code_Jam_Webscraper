#include <bits/stdc++.h>

using namespace std;

long long casos, ctos, nivel, puede;

int main(){
    scanf("%lld", &casos);
    for(long long v=1; v<=casos; v++){
        scanf("%lld%lld%lld", &ctos, &nivel, &puede);
        printf("Case #%lld: ", v);
        
        if((ctos-1)/nivel+1>puede){
            printf("IMPOSSIBLE\n"); continue;
        }
        long long next=0, place, lvl = nivel;
        for(long long i=1; i<=ctos; i++){
            if(lvl == nivel){
                next = i; lvl=1;
            }
            else{
                ++lvl;
                next=(next-1)*ctos+i;
            }
            if(lvl==nivel){
                printf("%lld ",next);
            }
        }
        if(lvl!=nivel){
            while(lvl!=nivel){
                next=(next-1)*ctos+ctos;
                ++lvl;
            }
            printf("%lld ", next);
        }
        
        printf("\n"); 
    }
    return 0;
}
