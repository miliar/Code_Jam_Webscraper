#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
    //fflush(stdin);
    //freopen("problem1b.txt","r",stdin);
    //freopen("ans1b.txt","w",stdout);
    int i,j,k,m=0,x=0,y=0,t=0,dot=0,T,flag=-1;
    char game[4][4],c;

    scanf("%d",&T);
    scanf("%c",&c);
    //printf("%c\n",c);     //NEW LINE IS IN C
    for(i=1;i<=T;i++)
    {
        //start checking for a game
        //scanf("%c",&c);
        x=0; y=0; t=0; dot=0;
        for(j=0;j<4;j++)
        {
            for(k=0;k<4;k++)
                scanf("%c",&game[j][k]);
            scanf("%c",&c);     //very important for skipping new line read in game[j][k]
        }
        flag=-1;
        for(j=0;j<4;j++)
        {
            x=0; y=0;  t=0;
            //printf("row check\n");//row check
            for(k=0;k<4;k++)
            {
                //printf("%c\n",game[j][k]);
                if(game[j][k]=='X')
                    x++;
                else if(game[j][k]=='O')
                    y++;
                else if(game[j][k]=='.')
                    dot++;
                else if(game[j][k]=='T')
                    t++;
            }
            //printf("%d\n",game[j][k-1]);
            if(x==4 || (x==3 && t==1))
            {
                printf("Case #%d: X won\n",i);
                //fflush(stdin);
                flag=1; break;
            }

            else if(y==4 || (y==3 && t==1))
            {
                printf("Case #%d: O won\n",i);  flag=1;     break;
                //fflush(stdin);
            }

            else
            {
                //column check
                x=0; y=0;  t=0;
                for(k=0;k<4;k++)
                {
                    if(game[k][j]=='X')
                        x++;
                    else if(game[k][j]=='O')
                        y++;
                    else if(game[k][j]=='.')
                        dot++;
                    else if(game[k][j]=='T')
                        t++;
                }
                if(x==4 || (x==3 && t==1))
                {
                    printf("Case #%d: X won\n",i);  flag=1;     break;
                    //fflush(stdin);
                }

                else if(y==4 || (y==3 && t==1))
                {
                    printf("Case #%d: O won\n",i);  flag=1;     break;
                    //fflush(stdin);
                }

                else
                {
                    //diagonal check
                    x=0; y=0;  t=0;
                    for(m=0;m<4;m++)
                    {
                        if(game[m][m]=='X')
                            x++;
                        else if(game[m][m]=='T')
                            t++;
                        else if(game[m][m]=='O')
                            y++;
                    }
                    if((x==3 && t==1) || (x==4))
                    {
                        printf("Case #%d: X won\n",i);      flag=1;     break;
                        //fflush(stdin);
                    }
                    else if((y==3 && t==1) || (y==4))
                    {
                        printf("Case #%d: O won\n",i);      flag=1;     break;
                        //fflush(stdin);
                    }
                    else
                    {
                        //other diagonal check
                        x=0; y=0;  t=0;
                        for(m=3;m>=0;m--)
                        {
                            if(game[m][3-m]=='X')
                                x++;
                            else if(game[m][3-m]=='T')
                                t++;
                            else if(game[m][3-m]=='O')
                                y++;
                        }
                        if((x==3 && t==1) || (x==4))
                        {
                            printf("Case #%d: X won\n",i);      flag=1;     break;
                            //fflush(stdin);
                        }
                        else if((y==3 && t==1) || (y==4))
                        {
                            //printf("HERE\n");
                            printf("Case #%d: O won\n",i);      flag=1;     break;
                            //fflush(stdin);
                        }
                    }
                }
            }
            if(flag==1)
                break;
        }
        if(flag==-1 && dot>0)
        {
            printf("Case #%d: Game has not completed\n",i);
        }
        else if(flag==-1 && dot==0)
        {
            printf("Case #%d: Draw\n",i);
        }
        scanf("%c",&c);
    }
    return 0;
}
