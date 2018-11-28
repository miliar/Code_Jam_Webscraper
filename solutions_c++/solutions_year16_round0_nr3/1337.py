#include<iostream>
#include<vector>
#include<cstdio>
#include<queue>
#include<cstring>
using namespace std;
long long d[11];
const int N=32,J=500;
void rec(long long m)
{
    if(m==1)
    {
        cout<<1;
        return;
    }
    rec(m/2);
    cout<<m%2;
}
int del( __int128 a)
{
    int i;
    for(i=2;i<1000006 && i<a;++i)
        if(a%i==0)return i;
    return 0;
}
__int128 fi(long long m,long long s)
{
    __int128 st=1,o=0;
    while(m)
    {
        o+=st*(m%2);
        m/=2;
        st*=s;
    }
    return o;
}
void solve()
{
    int n,j;
    cin>>n>>j;
     long long m,br=0,i;
     for(m=(1ll<<(N-1))+1;br<J;m+=2)
     {
         d[2]=del(m);
         for(i=3;i<11;++i)
            d[i]=del(fi(m,i));
         for(i=2;i<11;++i)
            if(d[i]==0)break;
         if(i==11)
         {
             rec(m);
             for(i=2;i<11;++i)
                cout<<' '<<d[i];
             ++br;
             cout<<'\n';
         }
     }
}
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int i,n;
    cin>>n;
    for(i=1;i<=n;++i)
    {
        cout<<"Case #"<<i<<":\n";
        solve();
    }
}
