#include<bits/stdc++.h>
using namespace std;
#define ll long long

int main()
{
        freopen("inp.in","r",stdin);
    freopen("opt.out","w",stdout);

    ll t,j,ans,i,k;
    string s;
    cin>>t;
    j = 1;
    while(j <= t)
    {
        ans = 1;

        cin>>s;
        for(i=s.length();i >= 0 ;i--)
        {
            if(s[i] == '-')
            {
                break;
            }
        }
        if(i == -1)
        {
            cout<<"Case #"<<j<<": "<<0;
        }
        else
        {
            for(k = i; k > 0;k--)
            {
                if(s[k] != s[k-1])
                {
                    ans++;
                }
            }
            cout<<"Case #"<<j<<": "<<ans;
        }
        cout<<endl;
        j++;
    }
    return 0;
}
