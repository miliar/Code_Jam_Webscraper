#include <cstdio>
#include <cstring>

int main(){
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout);
    int tc,T,k,c,s;
    scanf("%d",&T);
    for(tc=1;tc<=T;++tc){
        scanf("%d%d%d",&k,&c,&s);
        printf("Case #%d:",tc);
        for(int i=1;i<=s;++i) printf(" %d",i);
        printf("\n");
    }
    return 0;
}
