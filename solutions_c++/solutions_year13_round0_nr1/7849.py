#include <iostream>
#include<cstdio>

using namespace std;
char a[5][5];
int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("output.in","w",stdout);
    int test,i,j,f,fl,k;
    scanf("%d",&test);
    char ans;
    for(k=1;k<=test;k++)
    {
        f=0;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                cin>>a[i][j];
                if(a[i][j]=='.')
                f=1;
            }
        }
        char ch;
        fl=0;
        for(i=0;i<4;i++)
        {
            fl=1;
            for(j=0;j<3;j++)
            {
                if(a[i][j]!='.'&&a[i][j]!='T')
                ch=a[i][j];
                if(a[i][j]=='.')
                {
                fl=0;
                break;
                }
                else if(a[i][j]=='T')
                {
                continue;
                }
                else if(a[i][j]!=a[i][j+1]&&a[i][j+1]!='T')
                {
                    fl=0;
                    break;
                }
            }
            if(fl==1)
            {
                ans=ch;
                break;
            }
        }
        if(fl==0)
        {
            for(j=0;j<4;j++)
            {
                fl=1;
                for(i=0;i<3;i++)
                {
                    if(a[i][j]!='.'&&a[i][j]!='T')
                    ch=a[i][j];
                    if(a[i][j]=='.')
                {
                fl=0;
                break;
                }
                else if(a[i][j]=='T')
                {
                continue;
                }
                else if(a[i][j]!=a[i+1][j]&&a[i+1][j]!='T')
                {
                    fl=0;
                    break;
                }
                }
                if(fl==1)
            {
                ans=ch;
                break;
            }
            }
        }
        if(fl==0)
        {
            fl=1;
            for(i=0;i<3;i++)
            {
                if(a[i][i]!='.'&&a[i][i]!='T')
                ch=a[i][i];
                if(a[i][i]=='.')
                {
                    fl=0;
                    break;
                }
                else if(a[i][i]=='T')
                {
                    continue;
                }
                else if(a[i][i]!=a[i+1][i+1]&&a[i+1][i+1]!='T')
                {
                    fl=0;
                    break;
                }
            }
            if(fl==1)
            {
                ans=ch;
            }
        }
        if(fl==0)
        {
            fl=1;
            for(i=0;i<3;i++)
            {
                if(a[i][3-i]!='.'&&a[i][3-i]!='T')
                ch=a[i][3-i];
                if(a[i][3-i]=='.')
                {
                    fl=0;
                    break;
                }
                else if(a[i][3-i]=='T')
                continue;
                else if(a[i][3-i]!=a[i+1][3-i-1]&&a[i+1][3-i-1]!='T')
                {
                    fl=0;
                    break;
                }
            }
            if(fl==1)
            ans=ch;
        }
        printf("Case #%d: ",k);
        if(fl==1)
        printf("%c won\n",ans);
        else
        {
            if(f==1)
            printf("Game has not completed\n");
            else
            printf("Draw\n");
        }
    }
}
