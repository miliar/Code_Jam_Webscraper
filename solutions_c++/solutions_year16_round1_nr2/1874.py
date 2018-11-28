#include<bits/stdc++.h>
using namespace std;
#define ll long long
set <ll> s,ans;
set <ll> :: iterator it;
ll a[200][200],cnt[3000];

int main()
{
freopen("input.in","r",stdin);
freopen("output.txt","w",stdout);
ll n,t,k,i,j;
cin>>t;

for(k=1;k<=t;k++)
{
    memset(cnt,0,sizeof(cnt));
    s.clear();
    ans.clear();
    cin>>n;
    for(i=1;i<=2*n-1;i++)
    {
        for(j=1;j<=n;j++)
            {
                cin>>a[i][j];
                cnt[a[i][j]]++;
                s.insert(a[i][j]);
            }
    }

    for(it=s.begin();it!=s.end();it++)
        if(cnt[*it]%2!=0)
        ans.insert(*it);
 cout<<"Case #"<<k<<": ";
    for(it=ans.begin();it!=ans.end();it++)
        cout<<*it<<" ";
    cout<<"\n";

    }



return 0;
}
