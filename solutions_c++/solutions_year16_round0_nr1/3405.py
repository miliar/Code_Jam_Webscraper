#include<cstdio>
using namespace std;
long long Q,test,x,cate,aux,ras,i,v[15];
int main()
{
    freopen("input","r",stdin);
    freopen("output","w",stdout);
    scanf("%lld",&Q);
    for(test=1;test<=Q;test++)
    {
        scanf("%lld",&x);
        if(x==0)
        {
            printf("Case #%lld: INSOMNIA\n",test);
            continue;
        }
        for(i=0;i<10;i++)
            v[i]=0;
        cate=0;
        ras=0;
        while(cate<10)
        {
            ras=ras+x;
            aux=ras;
            while(aux>0)
            {
                v[aux%10]++;
                if(v[aux%10]==1)cate++;
                aux/=10;
            }
        }
        printf("Case #%lld: %lld\n",test,ras);
    }
    return 0;
}
