#include <cstdio>
using namespace std;

int main()
{
    freopen("i.in","r",stdin);
    freopen("o.out","w",stdout);
    int i,T,r,t,nr;
    scanf("%d",&T);
    for(i=0;i<T;++i)
    {
        scanf("%d%d",&r,&t);
        nr=0;
        while(t>-1)
        {
            t-=((r+1)*(r+1)-r*r);
            if(t>-1) ++nr;
            r+=2;
        }
        printf("Case #%d: %d\n",i+1,nr);
    }
    return 0;
}
