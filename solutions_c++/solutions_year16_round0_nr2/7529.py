#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T,cs,i,sz,ans;
    string s;
    cin>>T;
    for(cs=1; cs<=T; cs++)
    {
        cin>>s;
        sz=s.length();
        ans=i=0;
        if(s[i]=='-')
        {
            ans++;
            while(i<sz and s[i]=='-')
            {
                s[i]='+';
                i++;
            }
        }
        while(i<sz)
        {
            if(s[i]=='-')
            {
                ans+=2;
                while(i<sz and s[i]=='-')
                {
                    s[i]='+';
                    i++;
                }
            }
            else i++;
        }
        printf("Case #%d: %d\n",cs,ans);
    }
    return 0;
}
