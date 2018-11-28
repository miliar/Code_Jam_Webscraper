#include<cstdio>
#include<cstdlib>
#include<cstring>

typedef long long int lint;

using namespace std;

int main(void)
{
    freopen("Ds.in","r",stdin);
    freopen("Dsout.txt","w",stdout);
    int T;
    int tt;
    lint K,C,S;
    int i;
    scanf("%d",&T);

    for(tt=1;tt<=T;tt++)
    {
        scanf("%lld %lld %lld",&K,&C,&S);
        lint K1 = K;

        for(i=0;i<C-1;i++)
            K = K*K1;

        printf("Case #%d:",tt);
        for(i=0;i<S;i++)
        {
            printf(" %lld",i*(K/S)+1);

        }
        printf("\n");
    }

    return 0;
}
