#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
using namespace std;
#define  ll long long
#define endl '\n'
int a[11],mark;
ll flag[1000100];
void dig(ll x)
{
    while(x)
    {
        if(a[x%10]==0) mark++;
        a[x%10]=1;
        x/=10;
    }
}
int solve(int n)
{
    memset(a,0,sizeof(a));
    if(n==0) return -1;
    ll x=0;
    mark=0;
    while(1)
    {
        if(mark==10) return x;
        else x=x+n;
        dig(x);
    }
}
int main()
{
    //freopen("input.txt","r",stdin);
   // freopen("output.txt","w",stdout);
    int t,cas=1,n;
    for(int i=0;i<1000001;i++) flag[i]=solve(i);
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        cout<<"Case #"<<cas++<<": ";
        int ans=flag[n];
        if(ans==-1) cout<<"INSOMNIA"<<endl;
        else cout<<ans<<endl;
    }
    return 0;
}
