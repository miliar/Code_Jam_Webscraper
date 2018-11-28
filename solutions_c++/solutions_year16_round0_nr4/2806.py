#include<cstdio>
#include<cstring>
using namespace std;
long long p,ras;
int k,c,s;
int main()
{
    freopen("input","r",stdin);
    freopen("output","w",stdout);
    int Q;
    scanf("%d\n",&Q);
    for(int test=1;test<=Q;test++)
    {
        printf("Case #%d: ",test);

        scanf("%d %d %d",&k,&c,&s);
        p=1LL;
        for(int i=1;i<c;i++)
            p=p*k;
        ras=p;
        for(int i=1;i<=k;i++)
        {
            printf("%lld ",ras);
            ras+=p;
        }
        printf("\n");
    }
    return 0;
}
