#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int n,t,i,j,k,d,m,x,o;
    char a[4][4];
    cin>>n;
    for(k=1;k<=n;k++)
    {
       d=0;m=0;
       for(i=0;i<4;i++)
       {
           for(j=0;j<4;j++)
           {
               cin>>a[i][j];
               if(a[i][j]=='.')
               d++;
           }
       }
       for(i=0;i<4;i++)
       {
           x=0;t=0;o=0;
           for(j=0;j<4;j++)
           {
               if(a[i][j]=='X'||a[i][j]=='T')
               {
                   if(a[i][j]=='X')
                   x++;
                   else
                   t++;
               }
               if(a[i][j]=='O'||a[i][j]=='T')
               {
                   if(a[i][j]=='O')
                   o++;
                   else
                   t++;
               }
           }
           if((x==4&&t==0)||(x==3&&t>=1))
           {
               cout<<"Case #"<<k<<": X won"<<endl;
               m=1;
               break;
           }
           else if((o==4&&t==0)||(o==3&&t>=1))
           {
               cout<<"Case #"<<k<<": O won"<<endl;
               m=1;
               break;
           }
       }
       if(m==0){
       for(j=0;j<4;j++)
       {
           x=0;t=0;o=0;
           for(i=0;i<4;i++)
           {
               if(a[i][j]=='X'||a[i][j]=='T')
               {
                   if(a[i][j]=='X')
                   x++;
                   else
                   t++;
               }
               if(a[i][j]=='O'||a[i][j]=='T')
               {
                    if(a[i][j]=='O')
                    o++;
                    else
                    t++;
               }
           }
           if((x==4&&t==0)||(x==3&&t>=1))
           {
               cout<<"Case #"<<k<<": X won"<<endl;
               m=1;
               break;
           }
           else if((o==4&&t==0)||(o==3&&t>=1))
           {
               cout<<"Case #"<<k<<": O won"<<endl;
               m=1;
               break;
           }
       }
    }
    if(m==0)
    {
        x=0;t=0;o=0;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(i==j)
                {
                    if(a[i][j]=='X'||a[i][j]=='T')
                    {
                        if(a[i][j]=='X')
                        x++;
                        else
                        t++;
                    }
                    if(a[i][j]=='O'||a[i][j]=='T')
                    {
                        if(a[i][j]=='O')
                        o++;
                        else
                        t++;
                    }
                }
            }
        }
        if((x==4&&t==0)||(x==3&&t>=1))
            {
                cout<<"Case #"<<k<<": X won"<<endl;
                m=1;
            }
            else if((o==4&&t==0)||(o==3&&t>=1))
            {
                cout<<"Case #"<<k<<": O won"<<endl;
                m=1;
            }
    }
    if(m==0)
    {
        x=0;t=0;o=0;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(i+j==3)
                {
                    if(a[i][j]=='X'||a[i][j]=='T')
                    {
                        if(a[i][j]=='X')
                        x++;
                        else
                        t++;
                    }
                    if(a[i][j]=='O'||a[i][j]=='T')
                    {
                        if(a[i][j]=='O')
                        o++;
                        else
                        t++;
                    }
                }
            }

        }
        if((x==4&&t==0)||(x==3&&t>=1))
            {
                cout<<"Case #"<<k<<": X won"<<endl;
                m=1;
            }
            else if((o==4&&t==0)||(o==3&&t>=1))
            {
                cout<<"Case #"<<k<<": O won"<<endl;
                m=1;
            }
    }
    if(m==0&&d==0)
    cout<<"Case #"<<k<<": Draw"<<endl;
    else if(m==0&&d>0)
    cout<<"Case #"<<k<<": Game has not completed"<<endl;
    }
    return 0;
}
