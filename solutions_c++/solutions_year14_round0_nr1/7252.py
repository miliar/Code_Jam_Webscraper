#include<stdio.h>
#include<string.h>
int main()
{
    long testcases,firstanswer,secondanswer,resultcount;
    long arrangeone[4][4],arrangetwo[4][4],result[4];
    scanf("%ld",&testcases);
    for(long t=0;t<testcases;t++)
    {
        scanf("%ld",&firstanswer);
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
                scanf("%ld",&arrangeone[j][k]);
        }
        scanf("%ld",&secondanswer);
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
                scanf("%ld",&arrangetwo[j][k]);
        }
        resultcount=0;
        memset(result,0,sizeof(result));
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                if(arrangeone[firstanswer-1][i]==arrangetwo[secondanswer-1][j])
                {
                    result[resultcount++]=arrangeone[firstanswer-1][i];
                    break;
                }
            }
        }
        if(resultcount==0)
            printf("Case #%ld: Volunteer cheated!\n",t+1);
        else if(resultcount>1)
            printf("Case #%ld: Bad magician!\n",t+1);
        else
            printf("Case #%ld: %ld\n",t+1,result[0]);
    }

    return 0;
}
