#include<stdio.h>

int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,ti,k,c,s,i,j;
    scanf("%d",&t);
    for(ti=1; ti<=t; ++ti)
    {
        scanf("%d %d %d",&k, &c, &s);
        printf("Case #%d:",ti);
        for(i=1; i<=s; ++i)
            printf(" %d",i);
        puts("");
    }
    return 0;
}
