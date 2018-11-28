#include<stdio.h>
#include<stdlib.h>
main()
{
    //int lol[5][5][5];
    //for(int i=0;i<5;i++)for(int j=0;j<5;j++)for(int k=0;k<5;k++)lol[i][j][k]=0;
    //lol[2][2][2]=1;
    int ttt;
    scanf("%d",&ttt);
    for(int tttt=0;tttt<ttt;tttt++)
    {
        printf("Case #%d: ",tttt+1);
        int a,s,d;
        scanf("%d %d %d",&a,&s,&d);
        bool chk=0;
        while(1)
        {
            if(a==1)
            {
                chk=1;
                break;
            }
            else if(a==2)
            {
                if(s%2==0||d%2==0)
                {
                    chk=1;
                    break;
                }
            }
            else if(a==3)
            {
                if(s==3)
                {
                    if(d>1)
                    {
                        chk=1;
                        break;
                    }
                }
                else if(d==3)
                {
                    if(s>1)
                    {
                        chk=1;
                        break;
                    }
                }
            }
            else if(a==4)
            {
                if((s>=3&&d>=3)&&(s==4||d==4))
                {
                    chk=1;
                    break;
                }
            }
            break;
        }
        if(chk)printf("GABRIEL");
        else printf("RICHARD");
        printf("\n");
    }
}
