#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("input.txt","r",stdin);//redirects standard input
   freopen("output.txt","w",stdout);//redirects standard output
    int t;
    cin>>t;
    for(int j=0; j<t; j++)
    {
        string s;
        cin>>s;
        int ans=0;
        for(int i=1; i<s.size(); i++)
        {
            if(s[i]==s[i-1])
            {
                s.erase(i,1);
                i--;
            }
        }
        if(s.size()==1)
        {
            if(s[0]=='-')printf("Case #%d: 1\n",j+1);
            else printf("Case #%d: 0\n",j+1);
        }
        else
        {
            for(int i=1; i<s.size(); i++)
            {
                if(s[i]=='+'&&s[i-1]=='-'){
                s[i-1]='-';
                ans+=1;}
                if(s[i]=='-'&&s[i-1]=='+'){
            s[i]='+';
                ans+=2;
            }
            }

            printf("Case #%d: %d\n",j+1,ans);
        }
    }
    return 0;
}
