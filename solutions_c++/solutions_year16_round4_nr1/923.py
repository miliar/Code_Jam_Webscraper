#include <bits/stdc++.h>

using namespace std;

int T,n,p,r,s,cas;

string dfs(int p,int r,int s,string sp,string sr,string ss)
{
    if(p+r+s==1) return p?sp:(r?sr:ss);
    if(p+r<s || r+s<p || s+p<r) return "IMPOSSIBLE";
    int pr=(p+r-s)/2;
    int rs=(r+s-p)/2;
    int ps=(p+s-r)/2;
    return dfs(pr,rs,ps,min(sp,sr)+max(sp,sr),min(sr,ss)+max(sr,ss),min(sp,ss)+max(sp,ss));
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    for(cin>>T;T--;)
    {
        cin>>n>>r>>p>>s;
        cout<<"Case #"<<++cas<<": "<<dfs(p,r,s,"P","R","S")<<endl;
    }
    return 0;
}
