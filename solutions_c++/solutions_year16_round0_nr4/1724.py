#include<bits/stdc++.h>
using namespace std;
int main(){
    int T;
    freopen("D-small-attempt0.in","r",stdin);
    freopen("y.txt","w",stdout);
    scanf("%d",&T);
    for(int t=1;t<=T;++t){
        int K,C,S;
        scanf("%d %d %d",&K,&C,&S);
        printf("Case #%d:",t);
        for(int i=1;i<=S;++i)
            printf(" %d",i);
        printf("\n");
    }
    return 0;
}
