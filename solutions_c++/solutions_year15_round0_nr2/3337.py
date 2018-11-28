#include<bits/stdc++.h>
using namespace std;
#define FOR(i,a)    for(int i = 0;i < a;i++)
#define REP(i,a,b)  for(int i = a;i < b;i++)

int main()
{
    ios_base::sync_with_stdio(false);
    freopen("B-large.in","r",stdin);
    freopen("output.out","w",stdout);
    int t;
    cin>>t;
    REP(a,1,t+1)
    {
        int n;
        vector<int>v;
        cin>>n;
        FOR(i,n)
        {
            int tmp;
            cin>>tmp;
            v.push_back(tmp);
        }
        sort(v.begin(),v.end());
        int ma=v[n-1];
        int ans=INT_MAX;
        for(int psz=ma;psz>=1;psz--)
        {
            int cou=0;
            for(int i=0;i<n;i++)
            {
                if(ceil(1.000*v[i]/psz)>=1)
                cou+=(ceil((1.000*v[i])/psz)-1);
            }
            ans=min(ans,cou+psz);
        }
        cout<<"Case #"<<a<<": "<<ans<<"\n";
    }
    return 0;
}
