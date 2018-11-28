#include<stdio.h>
#include<string>
#include<iostream>
using namespace std;
string s[10];

int main()
{
    freopen ("input.txt","r",stdin);
    freopen ("output.txt","w",stdout);
    int tcase ;
    scanf("%d",&tcase);
    int t,i;
    for(t=0 ; t<tcase ; t++)
    {
        int j,k,flag1,flag2,chk=0;
        for(i=0 ; i<4 ; i++)
            cin >> s[i];

            int dX1=0,dO1=0,dX2=0,dO2=0,flag=0;

            for(j=0,k=0 ; j<4 ; j++,k++)
            {
                if(s[j][k]=='X')
                    dX1++;
                if(s[j][k]=='O')
                    dO1++;
                if(s[j][k]=='T')
                {
                    dX1++;
                    dO1++;
                }
                if(s[j][k]=='.')
                    flag=1;
            }
            for(j=0,k=3 ; j<4 ;j++,k--)
            {
                if(s[j][k]=='X')
                    dX2++;
                if(s[j][k]=='O')
                    dO2++;
                if(s[j][k]=='T')
                {
                    dX2++;
                    dO2++;
                }
                if(s[j][k]=='.')
                    flag=1;
            }
        //printf("%d \n",dO2);
            if(dX1==4 || dX2==4)
            {
                printf("Case #%d: X won\n",t+1);
                chk=1;
            }

            else if(dO1==4 || dO2==4)
            {
                printf("Case #%d: O won\n",t+1);
                chk=1;
            }

            else
            {
                for(j=0 ; j<4 ; j++)
                {
                    int x1=0,x2=0,o1=0,o2=0;
                    for(k=0 ; k<4 ; k++)
                    {
                        if(s[j][k]=='X')
                            x1++;
                        if(s[j][k]=='O')
                            o1++;
                        if(s[j][k]=='T')
                        {
                            x1++;
                            o1++;
                        }
                        if(s[k][j]=='X')
                            x2++;
                        if(s[k][j]=='O')
                            o2++;
                        if(s[k][j]=='T')
                        {
                            x2++;
                            o2++;
                        }
                        if(s[j][k]=='.')
                            flag=1;
                    }

                    if(x1==4 || x2==4)
                    {
                        printf("Case #%d: X won\n",t+1);
                        chk=1;
                        break;
                    }

                    else if(o1==4 || o2==4)
                    {
                        printf("Case #%d: O won\n",t+1);
                        chk=1;
                        break;
                    }
                }
            }
            if(chk==0)
            {
                flag2=1;
                for(j=0 ; j<4 ; j++)
                {
                    flag1=0;
                    for(k=0 ; k<4 ; k++)
                    {
                        if(s[j][k]!='.')
                            flag1=1;
                        if(s[j][k]=='.')
                            flag2=0;
                    }
                    if(flag1==0)
                    {
                        printf("Case #%d: Game has not completed\n",t+1);
                        break;
                    }
                }
                if(flag2==1)
                    printf("Case #%d: Draw\n",t+1);
            }

    }
    return 0;
}
