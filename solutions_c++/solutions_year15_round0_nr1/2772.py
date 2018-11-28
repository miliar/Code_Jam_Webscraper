#include<bits/stdc++.h>
using namespace std;
typedef long long ll;


int main()
{
        ll t;
        cin>>t;
        for(ll i=1;i<=t;i++)
        {
            ll n;
            cin>>n;
            string s;
            cin>>s;
            ll res=0,c=0;
            c+=(s[0]-'0');
            for(ll j=1;j<s.size();j++)
            {
                if(s[j]=='0')   continue;
                else
                {
                    if(j>c)
                    {
                        res+=(j-c);
                        c+=res+s[j]-'0';
                    }
                    else
                        c+=(s[j]-'0');
                }
            }
            cout<<"Case #"<<i<<": "<<res<<endl;
        }
        return 0;
}
