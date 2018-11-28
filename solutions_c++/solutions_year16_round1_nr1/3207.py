#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("solution.out","w",stdout);

    int t;
    string s,ans;

    cin>>t;

    for(int i=1; i<=t; i++)
    {
        ans="";

        cin>>s;

        for(int j=0; j<s.length(); j++)
        {
            if(s[j]>= ans[0])
                ans=s[j]+ans;
            else
                ans+=s[j];
        }

        cout<<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}
