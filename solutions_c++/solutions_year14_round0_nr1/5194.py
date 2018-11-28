#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int v;
int t;
int ans;
int nums[17];
int thenum,ctr=0;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);

    int test;
    int i,j;

    scanf("%d",&t);

    for (test=1;test<=t;test++)
    {
        memset(nums,0,sizeof(nums));

        scanf("%d",&ans);

        for (i=1;i<=4;i++)
        {
            for (j=1;j<=4;j++)
            {
                scanf("%d",&v);

                if (i==ans)
                nums[v]++;
            }
        }

        scanf("%d",&ans);

        for (i=1;i<=4;i++)
        {
            for (j=1;j<=4;j++)
            {
                scanf("%d",&v);

                if (i==ans)
                nums[v]++;
            }
        }

        ctr=0;
        for (i=1;i<=16;i++)
        {
            if (nums[i]==2)
            {
                ctr++;
                thenum=i;
            }
        }

        printf("Case #%d: ",test);

        if (ctr==0)
        {
            printf("Volunteer cheated!\n");
        }
        else if (ctr==1)
        {
            printf("%d\n",thenum);
        }
        else
        {
            printf("Bad magician!\n");
        }
    }

    return 0;
}
