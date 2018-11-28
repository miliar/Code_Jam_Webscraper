#include <stdio.h>
#include <string.h>
int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("small_output.txt","w",stdout);

    int cases;
    scanf("%d",&cases);
    for(int T = 1; T <= cases; T++)
    {
        int k,c,s;
        scanf("%d %d %d",&k,&c,&s);

        printf("Case #%d:",T);
        for(int i = 1; i <= k; i++)
            printf(" %d",i);
        puts("");
    }
}

