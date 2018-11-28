#include <cstdio>
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T,n,p,f;
    char x;
    scanf("%d",&T);
    for(int k=0;k<T;k++)
    {
        p=f=0;
        scanf("%d",&n);
        scanf("%c",&x);
        for(int i=0;i<n+1;i++)
        {
            scanf("%c",&x);
            x-='0';
            if(p<i){f+=i-p;p+=i-p;}
            p+=x;
        }
        printf("Case #%d: %d\n",k+1,f);
    }
    return 0;
}
