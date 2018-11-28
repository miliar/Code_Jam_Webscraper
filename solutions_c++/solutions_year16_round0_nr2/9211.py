#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("solution.out","w",stdout);

    int t,ans;
    string s;

    cin>>t;

    for(int i=1; i<=t; i++)
    {
        ans=0;
        cin>>s;

        for (int j=0; j<=s.length()-1; j++)
        {
            if(s[j]=='-' && j==0)
                ans++;
            else if(s[j]=='+' && s[j+1]=='-')
                ans+=2;
        }

        cout<<"Case #"<<i<<": "<<ans<<endl;

    }

    return 0;
}
