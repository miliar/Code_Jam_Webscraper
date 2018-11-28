///magician

#include<iostream>
#include<stdio.h>
#include<stdlib.h>

using namespace std;

int main()
{
    int testcases,count,r;

    scanf("%d",&testcases);
    r=testcases;
    int testarray[testcases];

    while(testcases--)
    {
        count=0;

        int row1;
        scanf("%d",&row1);

        int cards1[4][4];

        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                scanf("%d",&cards1[i][j]);
            }
        }

        int row2;
        scanf("%d",&row2);

        int cards2[4][4];

        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                scanf("%d",&cards2[i][j]);
            }
        }

        testarray[r-testcases-1]=0;

        for(int i=0;i<4;i++)
        {

            for(int j=0;j<4;j++)
            {




            if(cards1[row1-1][i]==cards2[row2-1][j])
            {
                testarray[r-testcases-1]=cards1[row1-1][i];
                count++;
                if(count>1)
                {
                    testarray[r-testcases-1]=-1;
                    goto out;
                }
            }

            }

        }
        out: ;
    }

    for(int i=0;i<r;i++)
    {
        printf("Case #%d: ",i+1);
        if(testarray[i]==0)  printf("Volunteer cheated!\n");
        else if(testarray[i]==-1) printf("Bad magician!\n");
        else printf("%d\n",testarray[i]);
    }
    return 0;
}
