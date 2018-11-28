#include <cstdio>
#include <cstring>
int A[5][5],B[5][5];
int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T,n,m,k,ans,pos = 0;
    scanf("%d",&T);
    while(T --)
    {
        printf("Case #%d: ",++ pos);
        ans = 0;
        k = -1;
        scanf("%d",&n);
        for(int i = 1;i <= 4;i ++)
            for(int j = 1;j <= 4;j ++)
            scanf("%d",&A[i][j]);
        scanf("%d",&m);
        for(int i = 1;i <= 4;i ++)
            for(int j = 1;j <= 4;j ++)
            scanf("%d",&B[i][j]);
        for(int i = 1;i <= 4;i ++)
        {
            for(int j = 1;j <= 4;j ++)
            {
                if(A[n][i] == B[m][j])
                {
                    ans ++;
                    k = A[n][i];
                }
            }
        }
        if(ans == 1)
            printf("%d\n",k);
        else
            {
                if(k == -1)
                printf("Volunteer cheated!\n");
                else
                printf("Bad magician!\n");
            }
    }
    return 0;
}
