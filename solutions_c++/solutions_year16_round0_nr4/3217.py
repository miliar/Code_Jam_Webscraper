#include<stdio.h>
#include<conio.h>
int main()
{
    int q;
    freopen("D-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&q);
    int k;
    for(k=1;k<=q;k++)
    {
        int x,c,s;
        scanf("%d%d%d",&x,&c,&s);
        printf("Case #%d: ",k);
        for(int j=1;j<=s;j++)
            printf("%d ",j);
        printf("\n");
    }
    return 0;
}
