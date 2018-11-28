#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
void print(vector<int> a)
{
    for(int i=0;i<a.size();i++) cout<<a[i];
}


ll fun(vector<ll> a,ll b)
{

    ll m=INT_MAX,sum=INT_MAX;
    for(ll i=1;i<=b;i++)
    {
        ll s=0;
        for(ll j=0;j<a.size();j++)
        {
            s+=(ceil((double)a[j]/i)-1);

        }
        if(s+i<=sum)
        {
            sum=s+i;
            m=s;
        }
    }
   // cout<<min(b,sum)<<endl;
    return min(b,sum);
}



int main()
{
    ll t;
    cin>>t;
    for(ll i=1;i<=t;i++)
    {
        ll n;
        cin>>n;
        vector<ll> a;
        for(ll j=0;j<n;j++)
        {
            ll temp;
            cin>>temp;
            a.push_back(temp);
        }
        cout<<"Case #"<<i<<": "<<fun(a,*max_element(a.begin(),a.end()))<<endl;
    }
    return 0;
}
