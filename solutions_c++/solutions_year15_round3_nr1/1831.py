#include <cstdio>
int t;
int main()
{
    freopen ("input.in","r",stdin);
    freopen ("output.out","w",stdout);
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        int r,c,w;
        scanf("%d%d%d",&r,&c,&w);
        int s=(c/w+w-1);
        if(c%w!=0) s++;
        s*=r;
        printf("Case #%d: %d\n",i,s);
    }
}
