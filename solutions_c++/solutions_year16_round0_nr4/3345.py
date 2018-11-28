#include<string.h>
#include<stdio.h>
int main()
{
    int T;
    int k,c,s;
    scanf("%d",&T);
    int cases=1;
    while(T--)
    {
        scanf("%d%d%d",&k,&c,&s);
        printf("Case #%d: ",cases++);
        for(int i=1;i<=k;i++)
        {
            if(i==1) printf("%d",i);
            else printf(" %d",i);
        }
        printf("\n");
    }
    return 0;
}
