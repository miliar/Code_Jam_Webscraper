#include <bits/stdc++.h>
using namespace std;
char z[30];
vector<int>v;
int main()
{

    freopen("dw.txt","r",stdin);
    freopen("out1.txt","w",stdout);
    int a1,a,b,c,d,e,f,i,j,k,p,q;
    char s[4],x1[4];
    int x[1001][3];
    for(i=0;i<=999;i++)
        {   b=i;
            x[i][2]=(b%10);
            b=b/10;
            x[i][1]=b%10;
            b=b/10;
            x[i][0]=b%10;
            b=b/10;
        }

    cin>>a1;
    for(i=1;i<=a1;i++)
    {
        cin>>s>>x1;
        a=strlen(s);
        if(a==2)
        {
            s[2]=s[1];
            x1[2]=x1[1];
            s[1]=s[0];
            x1[1]=x1[0];
            s[0]='0';
            x1[0]='0';
        }
        if(a==1)

            {   s[2]=s[0];
                x1[2]=x1[0];
                s[1]='0';
                x1[1]=s[1];
                x1[0]=s[1];
                s[0]=s[1];
            }

            s[3]='\0';
            x1[3]='\0';



        p=100000000;
        c=1000000;
        d=1000000;
      if(a==3){
        for(j=0;j<=999;j++)
        {
            if((x[j][0]==s[0]-48 || s[0]=='?') && (x[j][1]==s[1]-48 || s[1]=='?') && (x[j][2]==s[2]-48 || s[2]=='?'))
            {
                for(k=0;k<=999;k++)
                {
                    if((x[k][0]==x1[0]-48 || x1[0]=='?') && (x[k][1]==x1[1]-48 || x1[1]=='?') && (x[k][2]==x1[2]-48 || x1[2]=='?'))
            {
                      if(abs(j-k)<p)
                      {
                          p=abs(j-k);
                          c=j;
                          d=k;
                      }
                      else if(abs(j-k)==p)
                      {
                          if(j<c)
                          {
                              c=j;
                              d=k;
                          }
                          if(j==c)
                          {
                              if(k<d)
                                d=k;
                          }
                      }

                }
            }
        }

    }
      }
      else if(a==2)
      {
          for(j=0;j<=99;j++)
        {
            if((x[j][0]==s[0]-48 || s[0]=='?') && (x[j][1]==s[1]-48 || s[1]=='?') && (x[j][2]==s[2]-48 || s[2]=='?'))
            {
                for(k=0;k<=99;k++)
                {
                    if((x[k][0]==x1[0]-48 || x1[0]=='?') && (x[k][1]==x1[1]-48 || x1[1]=='?') && (x[k][2]==x1[2]-48 || x1[2]=='?'))
            {
                      if(abs(j-k)<p)
                      {
                          p=abs(j-k);
                          c=j;
                          d=k;
                      }
                      else if(abs(j-k)==p)
                      {
                          if(j<c)
                          {
                              c=j;
                              d=k;
                          }
                          if(j==c)
                          {
                              if(k<d)
                                d=k;
                          }
                      }

                }
            }
        }

    }
      }
      else if(a==1)
      {
          for(j=0;j<=9;j++)
        {
            if((x[j][0]==s[0]-48 || s[0]=='?') && (x[j][1]==s[1]-48 || s[1]=='?') && (x[j][2]==s[2]-48 || s[2]=='?'))
            {
                for(k=0;k<=9;k++)
                {
                    if((x[k][0]==x1[0]-48 || x1[0]=='?') && (x[k][1]==x1[1]-48 || x1[1]=='?') && (x[k][2]==x1[2]-48 || x1[2]=='?'))
            {
                      if(abs(j-k)<p)
                      {
                          p=abs(j-k);
                          c=j;
                          d=k;
                      }
                      else if(abs(j-k)==p)
                      {
                          if(j<c)
                          {
                              c=j;
                              d=k;
                          }
                          if(j==c)
                          {
                              if(k<d)
                                d=k;
                          }
                      }

                }
            }
        }

    }
      }
     if(a==3)
      {
          printf("Case #%d: ",i);
          printf("%d%d%d ",x[c][0],x[c][1],x[c][2]);
          printf("%d%d%d\n",x[d][0],x[d][1],x[d][2]);



    }
    else if(a==2)
    {
        printf("Case #%d: ",i);
          printf("%d%d ",x[c][1],x[c][2]);
          printf("%d%d\n",x[d][1],x[d][2]);
    }
    else if(a==1)
    {printf("Case #%d: ",i);
          printf("%d ",x[c][2]);
     printf("%d\n",x[d][2]);
    }
    }
    return 0;
}
