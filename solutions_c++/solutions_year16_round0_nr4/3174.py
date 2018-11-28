#include <stdio.h>
int k,c,s;
int main (void)
{
    int i,j,t;

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    scanf("%d",&t);
    for(i=0;i<t;i++){
        scanf("%d %d %d",&k,&c,&s);
        printf("Case #%d:",i+1);
        for(j=0;j<s;j++)
            printf(" %d",j+1);
        printf("\n");
    }

    return 0;
}
