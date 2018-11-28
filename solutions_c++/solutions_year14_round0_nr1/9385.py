#include<stdio.h>
#include<stdlib.h>
main()
{
    int tt;
    scanf("%d",&tt);
    for(int ttt=0;ttt<tt;ttt++)
    {
        printf("Case #%d: ",ttt+1);
        int cnting[17]={0};
        int r1;
        scanf("%d",&r1);
        for(int i=1;i<=4;i++)
        {
            for(int j=0;j<4;j++)
            {
                int tmp;
                scanf("%d",&tmp);
                if(i==r1)cnting[tmp]++;
            }
        }
        int r2;
        scanf("%d",&r2);
        for(int i=1;i<=4;i++)
        {
            for(int j=0;j<4;j++)
            {
                int tmp;
                scanf("%d",&tmp);
                if(i==r2)cnting[tmp]++;
            }
        }
        bool chk=0;
        bool chk2=0;
        int tmpp;
        for(int i=1;i<17;i++)
        {
            if(cnting[i]==2)
            {
                if(chk==0)
                {
                    chk=1;
                    tmpp=i;
                }
                else
                {
                    chk2=1;
                    break;
                }
            }
        }
        if(chk2)
        {
            printf("Bad magician!\n");
        }
        else if(chk==0)
        {
            printf("Volunteer cheated!\n");
        }
        else printf("%d\n",tmpp);
    }
}
