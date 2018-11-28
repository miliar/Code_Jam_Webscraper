#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t;
    cin>>t;
    for(int T=1;T<=t;T++)
    {
        string s;
        cin>>s;
        s+="+";
        char prev=s[0];
        int ans=0;
        for(int i=1;i<s.size();i++)
        {
            if(s[i]==prev)
                continue;
            ans++;
            prev=s[i];
        }
        cout<<"Case #"<<T<<": "<<ans<<"\n";
    }
    return 0;
}
