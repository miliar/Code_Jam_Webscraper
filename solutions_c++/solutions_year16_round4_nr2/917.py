#include<iostream>
#include<algorithm>
#include<cstring>
#include<queue>
#include<cmath>
#include<cstdlib>
#include<vector>
using namespace std;
double a[20],o[21][21],ans=0.0;
void solve()
{
    ans=0.0;
    int n,i,br,u;
    cin>>n>>u;
    for(i=0;i<n;++i)
        cin>>a[i];
    int m,j,k;
    for(m=1;m<(1<<n);++m)
    {
        for(i=0;i<20;++i)
            for(j=0;j<20;++j)
                o[i][j]=0.0;
        o[0][0]=1.0;
        br=0;
        for(j=0;j<n;++j)
            if(m&(1<<j))
            {
                br++;
                for(i=0;i<20;++i)
                {
                    o[i+1][br-i-1]+=o[i][br-i-1]*a[j];
                    o[i][br-i]+=o[i][br-i-1]*(1.0-a[j]);
                }
            }
        if(br==u)ans=max(ans,o[br/2][br/2]);
    }
    cout<<ans<<'\n';
}
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int t,i;
    cin>>t;
    for(i=1;i<=t;++i)
    {
        cout<<"Case #"<<i<<": ";
        solve();
    }
}
