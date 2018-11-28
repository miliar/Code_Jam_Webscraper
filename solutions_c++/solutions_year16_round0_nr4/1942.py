#include<cstdio>
int main()
{
    freopen("QD.in","r",stdin);
    freopen("QD.out","w",stdout);
    int T,k,c,s;
    scanf("%d",&T);
    for(int I=1;I<=T;I++)
    {
        scanf("%d%d%d",&k,&c,&s);
        if(k==s)
        {
            printf("Case #%d: ",I);
            for(int i=1;i<=s;i++)
                printf("%d ",i);
            printf("\n");
        }
    }
}
