#include<iostream>
#include<stdio.h>
main()
{
    int t;
    scanf("%d",&t);
    for(int i=0;i<t;i++)
    {
        int ans1,ans2,j,k;
        scanf("%d",&ans1);
        int per1[4][4];
        int per2[4][4];
        for(j=0;j<=3;j++)
        {
            for(int k=0;k<=3;k++)
                scanf("%d",&per1[j][k]);
        }
        scanf("%d",&ans2);
        for(j=0;j<=3;j++)
        {
            for(k=0;k<=3;k++)
                scanf("%d",&per2[j][k]);
        }
        int count=0,temp=0;
        for(j=0;j<4;j++)
        {
            for(k=0;k<4;k++)
            {   // printf("%d\\\\%d\n",per1[ans1-1][j],per2[ans2-1][k]);
                if(per1[ans1-1][j]==per2[ans2-1][k])
                {
                    temp=per1[ans1-1][j];

                    count++;
                }

            }
        }
        if(count==1)
            printf("Case #%d: %d\n",i+1,temp);
        else if(count>1)
            printf("Case #%d: Bad Magician!\n",i+1);
        else if(count==0)
            printf("Case #%d: Volunteer cheated!\n",i+1);
    }
}
