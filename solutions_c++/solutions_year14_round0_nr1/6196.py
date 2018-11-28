#include <stdio.h>
#include <string.h>
int map[5][5];
int c[17];
int main()
{
    int T;
    scanf("%d",&T);
    int C=1;
    while(T--)
    {
        memset(c,0,sizeof(c));
        for(int t=1;t<=2;t++)
        {
            int r;scanf("%d",&r);
            
            for(int i=1;i<=4;i++)
            {
                for(int j=1;j<=4;j++)
                {
                    scanf("%d",&map[i][j]);
                }
            }
            
            for(int i=1;i<=4;i++)
                c[map[r][i]]++;
        }
        int sum1=0,sum2=0;
        int who2=0;
        for(int i=1;i<=16;i++)
            if(c[i]==1)sum1++;
            else if(c[i]==2){sum2++;who2=i;}
        
        printf("Case #%d: ",C++);
        
        if(sum2==0)printf("Volunteer cheated!\n");
        else if(sum2==1)printf("%d\n",who2);
        else printf("Bad magician!\n");
    }
    return 0;
}