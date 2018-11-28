#include <cstdio>

using namespace std;

int T,k,c,s,i,nr;

int main()
{
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%d",&T);
    nr=0;
    while(T > 0)
    {
        --T;++nr;
        scanf("%d%d%d",&k,&c,&s);
        printf("Case #%d: ",nr);
        for(i=1;i<=s;++i) printf("%d ",i);
        printf("\n");
    }
    return 0;
}
