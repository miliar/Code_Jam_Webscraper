#include<iostream>
#include<algorithm>
#include<cstring>
#include<queue>
#include<cmath>
#include<cstdlib>
#include<vector>
using namespace std;
int used[4];
bool check(int n,int i,int p,int m)
{
    if(i==p)return check(n,i+1,p,m);
    if(i==n)
    {
        for(int j=0;j<n;++j)
            if(((m&(1<<(p*n+j)))!=0) && used[j]==0)return 1;
        return 0;
    }
    int j;
    bool l=0;
    for(j=0;j<n;j++)
        if(used[j]==0 && (m&(1<<(i*n+j)))!=0)
        {
            used[j]=1;
            l=check(n,i+1,p,m);
            used[j]=0;
            if(l==0)return 0;
        }
    return l;
}
int bit(int x)
{
    int br=0;
    while(x)
    {
        x&=x-1;
        br++;
    }
    return br;
}
void solve()
{
    int n,m=0,i,nm,o=0;
    char c;
    cin>>n;
    for(i=0;i<n*n;i++)
    {
        cin>>c;
        if(c=='0')++o;
        m=(m<<1)+c-'0';
    }
    for(nm=0;nm<(1<<(n*n));++nm)
    {
        if((nm&m)!=m)continue;
        for(i=0;i<n;++i)
            if(check(n,0,i,nm)==0)break;
        if(i==n)o=min(o,bit(nm^m));
    }
    cout<<o<<'\n';
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
