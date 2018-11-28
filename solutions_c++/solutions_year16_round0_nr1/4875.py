#include <cstdio>
int t,n,v[1000023];
int main()
{
    freopen ("out.out","r",stdin);
    for(int i=1;i<=1000000;i++) scanf("%d",&v[i]);
    freopen ("in.in","r",stdin);
    freopen ("output.out","w",stdout);
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        printf("Case #%d: ",i);
        scanf("%d",&n);
        if(n==0) printf("INSOMNIA\n");
        else printf("%d\n",v[n]);
    }
}
