#include <cstdio>
int T,k,c,s;
int main()
{
    scanf("%d",&T);
    for(int t=1;t<=T;++t)
    {
        scanf("%d%d%d",&k,&c,&s);
        printf("Case #%d:",t);
        for(int i=1;i<=s;++i)
            printf(" %d",i);
        putchar('\n');
    }
    return 0;
}
