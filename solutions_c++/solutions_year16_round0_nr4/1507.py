#include<iostream>
#include<vector>
#include<cstdio>
#include<queue>
#include<cstring>
using namespace std;
vector<int>o;
void solve(int j)
{
    long long k,c,s,n,i;
    cin>>k>>c>>s;
    if(c==1)
    {
        if(k>s)cout<<"IMPOSSIBLE\n";
        else
        {
            for(i=1;i<k;++i)
                cout<<i<<' ';
            cout<<i<<'\n';
        }
        return;
    }
    if(k%2+k/2>s)
    {
        cout<<"IMPOSSIBLE\n";
        return;
    }
    int l=1;
    int r=k;
    while(l<=r)
    {
        o.push_back((l-1)*k+r);
        ++l;
        --r;
    }
    n=o.size();
    for(i=0;i<n-1;++i)
        cout<<o[i]<<' ';
    cout<<o[i]<<'\n';
    o.clear();
}
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int i,n;
    cin>>n;
    for(i=1;i<=n;++i)
    {
        cout<<"Case #"<<i<<": ";
        solve(i);
    }
}
