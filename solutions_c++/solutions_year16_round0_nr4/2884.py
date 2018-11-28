#include<cstdio>
int main()
{
    int tn, k, c, s, i;
    freopen("gcds.in", "r", stdin);
    freopen("gcds.out", "w", stdout);
    scanf("%d",&tn);
    for(int tt=1;tt<=tn;tt++){
        scanf("%d %d %d",&k,&c,&s);
        printf("Case #%d:",tt);
        for(i=1;i<=k;i++)
            printf(" %d",i);
        printf("\n");
    }
    return 0;
}
