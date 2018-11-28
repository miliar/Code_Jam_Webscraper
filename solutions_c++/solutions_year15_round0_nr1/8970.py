#include <bits/stdc++.h>
using namespace std;
int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("output.out","w",stdout);
    ios_base::sync_with_stdio(false);
    int t,n;
    string s;
    cin>>t;
    for(int j=1;j<=t;j++)
    {
        cin>>n;
        cin>>s;
        int ans = 0;
        int stand= 0;
        for(int i=0;i<s.size();i++)
        {
            if(stand>=i)stand = stand+s[i]-'0';
            else
            {
                ans = ans + i-stand;
                stand = i+s[i]-'0';
            }
        }
        cout<<"Case #"<<j<<":"<<' '<<ans<<endl;
    }
    return 0;
}
