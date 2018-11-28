#include<bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define ll long long
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output2_large.txt","w",stdout);
    int t,q=0;
    cin>>t;
    while(t--)
    {
        q++;
        ll d,i,j,n,ans=0;
        cin>>d;
        vector< ll int > v,v1;
        vector< ll int >::iterator it,it1,low,up;
        for(i=0;i<d;i++)
        {
            cin>>j;
            v.pb(j);
        }
        v1=v;
        sort(v.begin(),v.end());
        it=v.end();it--;
        n=*it;
        ll mn=INT_MAX;
        for(i=1;i<=n;i++)
        {
            ans=i;
            for(j=0;j<v.size();j++)
            {
                ans+=(ceil(v[j]/(double)(i))-1);
            }
            if(ans<mn)
                mn=ans;
        }
        cout<<"Case #"<<q<<": "<<mn<<"\n";

    }
    return 0;
}
