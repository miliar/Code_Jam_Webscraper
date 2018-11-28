#include <iostream>
#include <stdio.h>

using namespace std;

char change(char ch)
{
    if(ch=='+')
    {
        return '-';
    }
    return '+';
}

void flip(string& s,int i)
{
    int j;
    char temp;
    for(j=0;j<=i/2;j++)
    {
        temp=s[j];
        s[j]=change(s[i-j]);
        s[i-j]=change(temp);
    }
}

int main()
{
    int t,q;
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for(q=1;q<=t;q++)
    {
        int n,i,j=0,r=0;
        string s;
        cin>>s;
        n=s.length();
        i=n-1;
        while(i>=0)
        {
           if(s[i]=='-')
           {
               r++;
               j=0;
               if(s[j]=='+')
               {
                   r++;
               }
               while(s[j]=='+')
               {
                   s[j]='-';
                   j++;
               }
               flip(s,i);
               i-=j;
           }
           else
           {
               i--;
           }
        }
        printf("Case #%d: %d\n",q,r);
    }
    return 0;
}
