#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int pan[101];

int CheckPan(int n)
{
    for(int i=0;i<n;i++)
    {
        if(pan[i]==0)
            return 0;
    }
    return 1;
}

void flip(int n)
{
    for(int i=n-1;i>=0;i--)
    {
        if(pan[i]==0)
        {
            for(int j=0;j<=i;j++)
            {
                pan[j]^=1;
            }
        break;
        }
    }
}
int main()
{
    freopen("bl.in","r",stdin);
    freopen("bl.out","w",stdout);
char s[1002];
    int n,CASE;
    scanf("%d",&CASE);
   for(int C=1;C<=CASE;C++)
   {
       scanf("%s",s);
       n = strlen(s);
       for(int i=0;i<n;i++)
       {
           if(s[i]=='-')
            pan[i]=0;
           else pan[i]=1;
       }
       int res=0;
        while(CheckPan(n)==0)
        {
            flip(n);
            res++;
        }
        printf("Case #%d: %d\n",C,res);

   }
    return 0;
}
