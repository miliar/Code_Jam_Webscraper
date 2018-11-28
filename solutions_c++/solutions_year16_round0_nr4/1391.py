#include<bits/stdc++.h>
#define ll long long int
#define inf 1000000000
#define mod 1073741824
using namespace std;

ll t,tt,k,c,s,diff,ans,i;
ll expo(ll base,ll rise)
{
    ll ret;
    ret = 1;
    while(rise)
    {
        if(rise%2)
        {
            ret *= base;
        }
        base*=base;
        rise/=2;
    }
    return ret;

}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>t;
    tt=t;
    while(t)
    {
        cin>>k>>c>>s;
        diff = expo(k,c-1);
        ans=1;
        cout<<"Case #"<<tt-t+1<<": ";
        for(i=0;i<s;i++)
        {
            cout<<ans<<" ";
            ans+=diff;
        }
        cout<<endl;

        t--;
    }

    return 0;
}
