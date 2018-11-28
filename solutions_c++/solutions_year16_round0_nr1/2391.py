#include<bits/stdc++.h>
using namespace std;

#define pb push_back
#define ff first
#define ss second
#define mpr make_pair
#define all(a) a.begin(),a.end()
#define Sz(a) a.size()
#define ii pair<int,int>


#define ll long long
#define inf 1000000009
#define mod 1000000007

#define rep(i,n)    for(i=0;i<(n);i++)
#define foro(i,n)   for(i=1;i<=(n);i++)
#define repe(i,a,b) for(i=(a);i<=(b);i++)
#define repr(i,a,b) for(i=(a);i>=(b);i--)
int cs;ll n,k,j;

int main()
{
    int i,T,u,v;
    //freopen("A-small-attempt0.in","r",stdin);
    freopen("A-large.in","r",stdin);
    freopen("16qAout.txt","w",stdout);
    scanf("%d",&T);
    bool f;int vis[12];
    while(T--)
    {
        cin>>n;
        rep(i,10)vis[i]=0;f=0;
        if(n)f=1;j=1;
        while(f)
        {
            k=n*j;
            while(k)
            {
                vis[k%10]=1;
                k/=10;
            }
            j++;;f=0;
            for(i=0;i<10;i++)
                if(!vis[i])f=1;
        }
        printf("Case #%d: ",++cs);
        if(n)printf("%lld\n",n*j-n);
        else puts("INSOMNIA");
    }
    return 0;

}