#include<stdio.h>
#include<string.h>
#include<math.h>
#include<functional>
#include<algorithm>
main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A.out","w",stdout);
    int T, n, i, j, k, b[150][150], len[150], cas=1, count;
    char input[150][150], a[150][150];
    scanf("%d", &T);

    while(T--)
    {
        scanf("%d", &n);
        for(i=1; i<=n; i++)
        {
            scanf("%s", input[i]);

        }
        memset(a, 0, sizeof(a));
        memset(b, 0, sizeof(b));
        for(i=1; i<=n; i++)
        {
            for(j=0, k=0; j<=strlen(input[i])-1; j++)
            {
                if(a[i][k]!=input[i][j])
                {
                    k++;
                    a[i][k]=input[i][j];
                }
                b[i][k]++;
            }
            len[i]=k;
        }
        /*for(i=1; i<=n; i++)
        {
            for(j=1; j<=len[i]; j++)
            {
                printf("%c ", a[i][j]);
            }
            printf("\n");
            for(j=1; j<=len[i]; j++)
            {
                printf("%d ", b[i][j]);
            }
            printf("\n");
        }*/
        int key=0;
        for(i=1; i<=n-1; i++)
        {
            if(len[i]!=len[i+1])
            {
                key=1;
            }
        }
        if(key==1)
        {
            printf("Case #%d: Fegla Won\n", cas++);
            continue;;
        }
        count=0;
        for(i=1; i<=len[1]; i++)
        {
            int sum=0;
            for(j=1; j<=n-1; j++)
            {
                if(a[j][i]!=a[j+1][i])
                {
                    key=1;
                }
            }
            if(key==1)
            {
                break;
            }
            for(j=1; j<=n; j++)
            {
                sum+=b[j][i];
            }
            sum/=n;
            for(j=1; j<=n; j++)
            {
                count=count+abs(sum-b[j][i]);
            }
        }
        if(key==1)
        {
            printf("Case #%d: Fegla Won\n", cas++);
            continue;
        }
        printf("Case #%d: %d\n", cas++, count);
    }

}
