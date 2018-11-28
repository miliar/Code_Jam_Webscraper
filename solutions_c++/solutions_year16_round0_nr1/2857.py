#include<bits/stdc++.h>
using namespace std;
#define ll long long

map<ll,int>mp;
int vis[11];
bool deal(ll x){ 
    if(!x) return 0;
    while(x){
        vis[x%10]=1;
        x/=10;
    }
    for(int i=0;i<10;i++) if(!vis[i]) return 1;
    return 0;
}   
int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("out.txt","w",stdout);
    int T,Case=1;
    ll n;
    scanf("%d",&T);
    while(T--)
    {
        printf("Case #%d: ",Case++);
        cin>>n;
        memset(vis,0,sizeof vis);
        /*for(int i=1;i<=100;i++)
        {
            cout<<n*i<<endl;
        }*/
        ll tem=n;
        while(deal(tem)){
            tem+=n;
        }
        if(!n) cout<<"INSOMNIA\n";
        else cout<<tem<<endl;
    } 
    return 0;
}
