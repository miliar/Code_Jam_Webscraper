#include <cstdio>

using namespace std;

int A[5][5],B[5][5];

int main()
{
    int T,F,S,tc=1,cnt,ans;
    scanf("%d",&T);
    while(T--)
    {
        cnt=0;
        scanf("%d",&F);
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
                scanf("%d",&A[i][j]);

        scanf("%d",&S);
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
                scanf("%d",&B[i][j]);

        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                if(B[S][j] == A[F][i])
                {
                    cnt++;
                    ans = A[F][i];
                }
            }
        }

        printf("Case #%d: ",tc++);
        if(cnt>1)
            printf("Bad magician!\n");
        else if(cnt == 0)
            printf("Volunteer cheated!\n");
        else
            printf("%d\n",ans);
    }
    return 0;
}
