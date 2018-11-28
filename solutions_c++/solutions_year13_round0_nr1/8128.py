#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>



int main()
{
    int testcase,x,o;
    bool xw,ow,nc;
    char tictac[10][10];
    scanf("%i\n",&testcase);
    for(int i=1;i<=testcase;i++)
    {
        x=0,o=0;
        nc=false;
        for(int k=0;k<4;k++)
        {
            for(int l=0;l<4;l++)
            {
                scanf("%c",&tictac[k][l]);
                if(tictac[k][l]=='.')nc=true;
            }
            scanf("\n");
        }
        scanf("\n");
        /*for(int k=0;k<4;k++)
        {
            for(int l=0;l<4;l++)
            {
                printf("%c",tictac[k][l]);
                if(tictac[k][l]=='.')nc=true;
            }
            printf("\n");
        }*/
        for(int k=0;k<4;k++)
        {
            if(tictac[k][0]=='X'||tictac[k][0]=='T')
            {
                x++;
            }
            if(tictac[k][1]=='X'||tictac[k][1]=='T')
            {
                x++;
            }
            if(tictac[k][2]=='X'||tictac[k][2]=='T')
            {
                x++;
            }
            if(tictac[k][3]=='X'||tictac[k][3]=='T')
            {
                x++;
            }
            if(tictac[k][0]=='O'||tictac[k][0]=='T')
            {
                o++;
            }
            if(tictac[k][1]=='O'||tictac[k][1]=='T')
            {
                o++;
            }
            if(tictac[k][2]=='O'||tictac[k][2]=='T')
            {
                o++;
            }
            if(tictac[k][3]=='O'||tictac[k][4]=='T')
            {
                o++;
            }
            if(x==4)
            {
                xw=true;
                break;
            }
            else if(o==4)
            {
                ow=true;
                break;    
            }  
            x=0,o=0;          
        }
        if(!(xw||ow))
        {
            x=0,o=0; 
            for(int k=0;k<4;k++)
            {
                if(tictac[0][k]=='X'||tictac[0][k]=='T')
                {
                    x++;
                }
                if(tictac[1][k]=='X'||tictac[1][k]=='T')
                {
                    x++;
                }
                if(tictac[2][k]=='X'||tictac[2][k]=='T')
                {
                    x++;
                }
                if(tictac[3][k]=='X'||tictac[3][k]=='T')
                {
                    x++;
                }
                if(tictac[0][k]=='O'||tictac[0][k]=='T')
                {
                    o++;
                }
                if(tictac[1][k]=='O'||tictac[1][k]=='T')
                {
                    o++;
                }
                if(tictac[2][k]=='O'||tictac[2][k]=='T')
                {
                    o++;
                }
                if(tictac[3][k]=='O'||tictac[3][k]=='T')
                {
                    o++;
                }
                if(x==4)
                {
                    xw=true;
                    break;
                }
                else if(o==4)
                {
                    ow=true;
                    break;    
                }  
                x=0,o=0;          
            }
        }
        if(!(xw||ow))
        {
            x=0,o=0; 
            
            for(int jj=0;jj<4;jj++)
            {
                if(tictac[jj][jj]=='X'||tictac[jj][jj]=='T')
                {
                    x++;
                    //printf("%i",x);
                }
                if(tictac[jj][jj]=='O'||tictac[jj][jj]=='T')
                {
                    o++;
                }
                
                if(x==4)
                {
                    xw=true;
                    //printf("haho");
                    break;
                }
                else if(o==4)
                {
                    ow=true;
                    break;    
                }            
            }
        }
        if(!(xw||ow))
        {
            //printf("hoho");
            x=0,o=0; 
            int j=0;
            for(int k=3;k>=0;k--)
            {
                if(tictac[j][k]=='X'||tictac[j][k]=='T')
                {
                    x++;
                }
                if(tictac[j][k]=='O'||tictac[j][k]=='T')
                {
                    o++;
                }
                j++;
                if(x==4)
                {
                    xw=true;
                    break;
                }
                else if(o==4)
                {
                    ow=true;
                    break;    
                }          
            }
        }
        if(xw)printf("Case #%i: X won\n",i);
        else if(ow) printf("Case #%i: O won\n",i);
        else if(nc) printf("Case #%i: Game has not completed\n",i);
        else printf("Case #%i: Draw\n",i);
        xw=false,ow=false,nc=false;
        x=0,o=0;
    }
}
