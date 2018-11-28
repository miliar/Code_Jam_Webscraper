#include<stdio.h>
 char mat[4][4];
int checkrow(int i,int sym)
{
    int j,foundT=0;
    for(j=0;j<4;j++)
    {
        if(mat[i][j]==sym)
        {
            continue;
        }
        else if(mat[i][j]=='T' && !foundT)
        {
            foundT=1;
        }
        else
        {
            break;
        }
    }
    if(j==4)
        return 1;
    else
        return 0;
}
int checkcol(int j,int sym)
{
    int i,foundT=0;
    for(i=0;i<4;i++)
    {
        if(mat[i][j]==sym)
        {
            continue;
        }
        else if(mat[i][j]=='T' && !foundT)
        {
            foundT=1;
        }
        else
        {
            break;
        }
    }
    if(i==4)
        return 1;
    else
        return 0;
}
int checkdiag(int i,int j , int sym)
{
    int ic,foundT=0;
    if(i==j)
    {
        for(ic=0;ic<4;ic++)
        {
            if(mat[ic][ic]==sym)
            {
                continue;
            }
            else if(mat[ic][ic]=='T' && !foundT)
            {
                foundT=1;
            }
            else
            {
                break;
            }

        }
        if(ic==4)
        {
            return 1;
        }
        else
        {
            return 0;
        }
    }
    else
    {
        for(ic=0;ic<4;ic++)
        {
            if(mat[ic][3-ic]==sym)
            {
                continue;
            }
            else if(mat[ic][3-ic]=='T' && !foundT)
            {
                foundT=1;
            }
            else
            {
                break;
            }

        }
        if(ic==4)
        {
            return 1;
        }
        else
        {
            return 0;
        }

    }
}

int main()
{
    int t,flag,win,row,col,diag;
    int casecnt=0;
    int i,j,countempty;
    scanf("%d",&t);
    while(t--)
    {
        casecnt++;
        countempty=0;
        flag=0;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                scanf("%c",&mat[i][j]);
                if(mat[i][j]==10)
                    scanf("%c",&mat[i][j]);
            }
        }
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(mat[i][j]=='X')
                {
                    row=checkrow(i,'X');
                    col=checkcol(j,'X');
                    if(i+j==3 || i==j)
                    {
                        diag=checkdiag(i,j,'X');
                    }
                    if(row || col || diag)
                    {
                        flag=1;
                        win='X';
                        break;
                    }
                }
                else if(mat[i][j]=='O')
                {
                    row=checkrow(i,'O');
                    col=checkcol(j,'O');
                    if(i+j==3 || i==j)
                    {
                        diag=checkdiag(i,j,'O');
                    }
                    if(row || col || diag)
                    {
                        flag=1;
                        win='O';
                        break;
                    }
                }
                else if(mat[i][j]=='T')
                {
                    continue;
                }
                else
                {
                    countempty++;
                }


            }
            if(flag==1)
                break;
        }

        if(flag==1)
        {
            if(win=='X' || win=='O')
            {
                printf("Case #%d: %c won\n",casecnt,win);
            }
        }
        else
        {
            if(countempty>0)
            {
                printf("Case #%d: Game has not completed\n",casecnt);
            }
            else
            {
                printf("Case #%d: Draw\n",casecnt);
            }
        }
        getchar();
    }
    return 0;
}
