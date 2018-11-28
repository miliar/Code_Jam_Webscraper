#include<bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{
    freopen("Ainput.txt","r",stdin);
    freopen("Aoutput.txt","w",stdout);
    ll t,n,i,x=0;
    string s;
    cin>>t;
    while(t--)
    {
        ll d=0,ans=0;
        cin>>n>>s;
        for(i=0;i<=n;i++)
        {
            if(d<i&&s[i]!='0')
            {
                ans+=(i-d);
                d=i;
                d+=(s[i]-'0');
            }
            else
            d+=(s[i]-'0');
        }
        cout<<"Case #"<<++x<<": "<<ans<<endl;
    }
}
