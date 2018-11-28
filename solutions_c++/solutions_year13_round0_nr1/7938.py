#include <iostream>
#include<stdio.h>
#include<math.h>
#include<string.h>

using namespace std;

int main()
{
    freopen("A0.in","r",stdin);
    freopen("A00.in","w",stdout);
    int t,i,j,flag,d=1;
    char a[10][10],c;
    scanf("%d",&t);
    getchar();
    while(t--)
    {
        int pp=0;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                scanf("%c",&a[i][j]);
                if(a[i][j]=='.')
                    pp=1;
            }
            getchar();
        }
        getchar();
        printf("Case #%d: ",d++);
        for(i=1;i<=4;i++)
        {
            c=a[i][1];
            if(c=='T');
            c=a[i][2];
            flag=0;
            if(c=='.')
            flag=1;
            else
            for(j=1;j<=4;j++)
            {
                if(a[i][j]!=c&&a[i][j]!='T')
                {
                    //printf("++++%d %d\n",i,j);
                    flag=1;
                    break;
                }
            }
            if(flag==0)
            {
                printf("%c won\n",c);
                //printf("%d\n",i);
                //printf("11\n");
                break;
            }
        }
        if(flag==1)
        for(i=1;i<=4;i++)
        {
            c=a[1][i];
            if(c=='T')
                c=a[2][i];
            flag=0;
            if(c=='.')
            flag=1;
            else
            for(j=1;j<=4;j++)
            {
                if(a[j][i]!=c&&a[j][i]!='T')
                {
                    //printf("====%d %d\n",i,j);
                    flag=1;
                    break;
                }
            }
            if(flag==0)
            {
                printf("%c won\n",c);
                //printf("22\n");
                break;
            }
        }
        if(flag==1)
        {
            flag=0;
            for(i=2;i<=4;i++)
            {
                c=a[1][1];
                if(c=='T')
                    c=a[2][2];
                if(c=='.')
                flag=1;
                else
                    if(a[i][i]!=c&&a[i][i]!='T')
                    {
                        flag=1;
                    }

            }
            if(flag==0)
            {printf("%c won\n",c);
            //printf("33\n");
            }
        }
        if(flag==1)
        {
            flag=0;
                c=a[1][4];
                if(c=='T')
                    c=a[2][3];
                if(c=='.')
                flag=1;
                else
                {
                    if(a[2][3]!='T'&&a[2][3]!=c)
                    {
                        flag=1;
                    }
                    if(a[3][2]!='T'&&a[3][2]!=c)
                    {
                        flag=1;
                    }
                    if(a[4][1]!='T'&&a[4][1]!=c)
                    {
                        flag=1;
                    }
                }
            if(flag==0)
            {printf("%c won\n",c);
            //printf("44\n");
            }
        }
        //printf("+++++%d\n",flag);
        if(flag==1&&pp==0)
            printf("Draw\n");
        else if(flag==1&&pp==1)
            printf("Game has not completed\n");
    }
    return 0;
}
