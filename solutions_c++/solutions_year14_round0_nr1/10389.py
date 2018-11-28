#include<stdio.h>
int main()
{
    int tt,ans1,ans2, cards[4][4],i,j,p[4],c,ans,tc;
    scanf("%d",&tt);
    tc=tt;
    while(tt--)
    {
        c=0;
        scanf("%d",&ans1);
        ans1--;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                scanf("%d",&cards[i][j]);
            }
        }
        p[0]=cards[ans1][0];
        p[1]=cards[ans1][1];
        p[2]=cards[ans1][2];
        p[3]=cards[ans1][3];
        scanf("%d",&ans2);
        ans2--;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                scanf("%d",&cards[i][j]);
            }
        }

        for(int i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
            if(p[i]==cards[ans2][j])
            {
                c++;
                ans=p[i];
            }
            }
        }


        if(c==1)
            printf("Case #%d: %d\n",tc-tt,ans);
        else if(c>1)
            printf("Case #%d: Bad magician!\n",tc-tt);
        else printf("Case #%d: Volunteer cheated!\n",tc-tt);


    }
    return 0;
}
