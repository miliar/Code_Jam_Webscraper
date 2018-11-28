#include <iostream>
#include<bits/stdc++.h>
using namespace std;

string s,c;


int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int t,i,ans,j;
    scanf("%d",&t);
    for(int k=1;k<=t;k++)
    {
        ans=0;

        cin>>s;
        c.clear();
        for(i=0;i<s.size();)
        {
            c+=s[i];
            for(j=i+1;j<s.size();j++)
             if(s[j]!=s[i])
                break;
            i=j;

        }
        for(i=0;i<c.size();i++)
        {
            if(c[i]=='-')
                {
                    if(i>0)
                  ans+=2;
                else
                    ans++;
                }
        }
        printf("Case #%d: ",k);
        printf("%d\n",ans);
    }
    return 0;
}
