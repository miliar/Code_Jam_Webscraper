#include <cstdio>
using namespace std;

int a1[4][4];
int a2[4][4];
int row1, row2;


int main()
{
    int kase;
    scanf("%d", &kase);
    for (int k = 1; k<=kase; k++)
    {
        int count = 0;
        int ans = 0 ;
        scanf("%d",&row1);
        for (int i = 0; i<4; i++)
            scanf("%d %d %d %d", &a1[i][0], &a1[i][1], &a1[i][2], &a1[i][3]);
        scanf("%d",&row2);
        for (int i = 0; i<4; i++)
            scanf("%d %d %d %d", &a2[i][0], &a2[i][1], &a2[i][2], &a2[i][3]);
        for (int i =0; i<4; i++)
        {
            for (int j =0; j<4; j++)
            {
                //fprintf(stderr,"%d %d\n",a1[row1-1][i], a2[row2-1][j]);
                if (a1[row1-1][i]==a2[row2-1][j])
                {
                    ans = a1[row1-1][i];
                    count++;
                    continue;
                }
             }
         }

         printf("Case #%d: ",k);
         if (count>1)
            printf("Bad magician!\n");
         else if (ans>0)
            printf("%d\n",ans);
         else
            printf("Volunteer cheated!\n");
      }
      return 0;
}


