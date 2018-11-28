#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
int main()
{
    ll t,i,k,m,n,v,x,st,ans;
    cin>>t;string s;
    for(k=1;k<=t;k++)
    {
        cin>>n>>s;
        st=s[0]-'0';ans=0;
        for(i=1;i<=n;i++)
        {
            v=i;x=s[i]-'0';
            if(st>=v) st+=x;
            else
            {
                m=v-st;
                st+=m+x;
                ans+=m;
            }
        }
        cout<<"Case #"<<k<<": "<<ans<<endl;
    }
    return 0;
}
