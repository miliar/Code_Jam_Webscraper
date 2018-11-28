#include <bits/stdc++.h>
using namespace std;


int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int T;
    string s,ans;
    int i,j,it;
    cin>>T;
    for (it=1;it<=T;it++)
    {
        cin>>s;
        ans = "";
        for (i=s.length()-1;i>=0;i--)
        {
            if (s[i]=='+') continue;
            ans = s[0];
            for (j=1;j<=i;j++)
            {
                if (s[j]!=ans[ans.length()-1]) ans+=s[j];
            }
            break;
        }
        cout<<"Case #"<<it<<": "<<ans.length()<<endl;
    }
    return 0;
}
