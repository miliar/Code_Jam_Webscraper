#include<bits/stdc++.h>
#define ll long long int
using namespace std;
int main()
{
    ll t,T,n,i,j,a,b,c,d,ans,l;
    vector<ll>v,v1;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>T;
    for(t=1; t<=T; t++)
    {
        cin>>n;
        v.clear();
        for(i=0; i<n; i++)
        {
            cin>>a;
            v.push_back(a);
        }
        //v=v1;
        sort(v.begin(),v.begin()+v.size());
        ans=1005;
        for(i=1; i<=1005; i++)
        {
            a=0;
            for(j=0;j<v.size();j++)
            {
                a+=(ceil((1.0*v[j])/(1.0*i))-1);
            }
            ans=min(ans,a+i);
        }
        printf("Case #%lld: %lld\n",t,ans);
    }
    return 0;
}
