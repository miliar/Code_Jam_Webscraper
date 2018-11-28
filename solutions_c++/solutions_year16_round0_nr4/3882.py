#include<cstdio>
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int tc;
    scanf("%d",&tc);
    for(int mindol=1;mindol<=tc;mindol++)
    {
        int k,c,s;
        scanf("%d %d %d",&k,&c,&s);
        printf("Case #%d: ",mindol);
        for(int i=1;i<=k;i++)
            printf("%d ",i);
        puts("");
    }
    return 0;
}
