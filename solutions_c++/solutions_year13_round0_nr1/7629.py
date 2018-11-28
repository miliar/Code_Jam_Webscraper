#include<stdio.h>
int main()
{
    int i,j,g,k,t,caset=0,x,o,countrx=0,countro=0,countrt=0,countcx=0,countco=0,countct=0,countdx=0,countdo=0,countdt=0,countdrx=0,countdro=0,countdrt=0;
    char a[4][5];
    scanf("%d",&t);
    while(t--)
    {   caset++;
        x=0;
        o=0;
        g=0;
        countdx=0;
        countdo=0;
        countdt=0;
        countdrx=0;
        countdro=0;
        countdrt=0;
        for(i=0;i<4;i++)
        {   
            //for(j=0;j<5;j++)
            //{
                scanf("%s",a[i]);
            //}
        }
        /*for(i=0;i<4;i++)
        {
            for(j=0;j<5;j++)
                printf("%c",a[i][j]);
            printf("\n");
        }*/
        for(i=0;i<4;i++)
        {   countrx=0,countro=0,countrt=0,countcx=0,countco=0,countct=0;
            for(j=0;j<4;j++)
            {   if(countrx>=1 && countro>=1)
                    break;
                if(a[i][j]=='X')
                    countrx++;
                if(a[i][j]=='O')
                    countro++;
                if(a[i][j]=='T')
                    countrt++;
            }
            
            for(k=0;k<4;k++)
            {
                if(countcx>=1 && countco>=1)
                    break;
                if(a[k][i]=='X')
                    countcx++;
                if(a[k][i]=='O')
                    countco++;
                if(a[k][i]=='T')
                    countct++;
            }
            if(countrx==4 || (countrx==3 && countrt==1))
            {    x=1;
                break;
            }
            else if(countro==4 || (countro==3 && countrt==1))
            {   o=1;
                    break;
            }
           
            //if(k==0)
            //{
            else if(countcx==4 || (countcx==3 && countct==1))
                {   x=1;
                    break;
                }
            else if(countco==4 || (countco==3 && countct==1))
                {   o=1;
                    break;
                }
            //}
        }
        for(i=0;i<4;i++)
        {
            if(a[i][i]=='X')
                countdx++;
            if(a[i][i]=='O')
                countdo++;
            if(a[i][i]=='T')
                countdt++;
        }
        for(i=3,j=0;i>=0;j++,i--)
        {   
            if(a[j][i]=='X')
                countdrx++;
            if(a[j][i]=='O')
                countdro++;
            if(a[j][i]=='T')
                countdrt++;
        }
        if(countdx==4 || (countdx==3 && countdt==1))
            x=1;
        if(countdo==4 || (countdo==3 && countdt==1))
            o=1;   
        if(countdrx==4 || (countdrx==3 && countdrt==1))
            x=1;
        if(countdro==4 || (countdro==3 && countdrt==1))
            o=1;
        if(x==1)
                printf("Case #%d: X won\n",caset);
        else if(o==1)
                 printf("Case #%d: O won\n",caset);
        else if(x!=1 && o!=1)
         {
            for(i=0;i<4;i++)
            {
                for(j=0;j<4;j++)
                {
                    if(a[i][j]=='.')
                        g=1;
                }
                if(g==1)
                 break;
            }
            if(g==0)
                 printf("Case #%d: Draw\n",caset);
            else
                printf("Case #%d: Game has not completed\n",caset);
         }      
        
    }
    return 0;
}