#include <cstdio>
using namespace std;
int main() {
    freopen("D-small-attempt0.in","r",stdin);
    freopen("D-small-attempt0.out","w",stdout);
    int t,k,c,s;
    scanf("%d",&t);
    for(int cas=1; cas<=t; ++cas) {
        scanf("%d%d%d",&k,&c,&s);
        printf("Case #%d:",cas);
        for(int i=1; i<=k; ++i)
            printf(" %d",i);
        putchar('\n');
    }
    return 0;
}
