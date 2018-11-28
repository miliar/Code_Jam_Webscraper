#include <bits/stdc++.h>

using namespace std;

string s;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
int t,ans,i,j;
scanf("%d",&t);
for(j=1;j<=t;j++)
{
    cin>>s;
    i=0;
    ans=0;
if(s[i]=='-')
{
    while(s[i]=='-')
    {
        i++;
    }
    ans++;
}

    while(i<s.size())
    {
        while(s[i]=='+' && i<s.size())
        {
            i++;
        }
        if(i==s.size())
        {
            break;
        }
        else
            if(s[i]=='-')
        {
            ans=ans+2;
         while(s[i]=='-' && i<s.size())
         {
             i++;
         }
         if(i==s.size())
            break;
        }
    }
printf("Case #%d: %d\n",j,ans);
}
    return 0;
}
