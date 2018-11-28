#include <bits/stdc++.h>
using namespace std;
int main()
{
    int a,b,c,d,T,sweep,i,j,p,q;
    char s[110];
    scanf("%d",&T);
    for(i=1;i<=T;i++)
    {
        scanf("%s",&s);
        a=strlen(s);
        b=0;
 
          c=0;
           while(1)
           {   d=-1;
               for(j=a-1;j>=0;j--)
                {
                    if(s[j]=='-')
                      {
                          d=j;
                          c++;
 
                          break;
                      }
                }
                if(d==-1)
                {
 
                    break;
                }
                for(j=0;j<=d;j++)
                {
                    if(s[j]=='+')
                      s[j]='-';
                    else if(s[j]=='-')
                      s[j]='+';
                }
           }
           printf("Case #%d: %d\n",i,c);
 
        }
 
    return 0;
}