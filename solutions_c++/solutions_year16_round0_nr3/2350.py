#include <stdio.h>
#include <string.h>
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("small_output.txt","w",stdout);

    int cases;
    scanf("%d",&cases);
    for(int T = 1; T <= cases; T++)
    {
        int n,k;
        scanf("%d %d",&n,&k);

        char mid[8];

        printf("Case #%d:\n",T);
        for(int i = 0; i < k; i++)
        {
            for(int j = 0; j < strlen(mid)-1; j++)
                mid[j] = (i&(1<<j)) == 0 ? '0' : '1';

            printf("1");
            for(int j = 0; j < n-2; j++)
                printf("%d",mid[j/2]-'0');
            printf("1 ");

            for(int j = 3; j <= 10; j++)
                printf("%d ",j);
            printf("11\n");
        }

    }
}

