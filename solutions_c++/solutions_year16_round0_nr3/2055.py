#include<bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define f first
#define maxn 100100
#define s second
#define ll long long int
#define inf 1000000014
#define infl (ll)(1e16+1)
//#define mod 1000000007
#define sz(x) (int) x.size()
#define trace1(x)  cerr << #x << ": " << x << endl;
#define trace2(x, y)  cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
using namespace  std;
ll modexp(ll a, ll b,ll mod)
{
    if(b==0ll)
        return 1ll;
    else if(b==1ll)
        return a;
    else
        if(b%2!=0)
         return (modexp(a,b-1,mod)*a)%mod;
    else
        return modexp((a*a)%mod,b/2,mod);
}
vector< int > v[550];
ll base2[550];
ll poww[12][60];

ll bin(int a)
{
    if(a<=1)
            return a;
    else
        return bin(a/2)*10ll+(ll)(a%2);
}
ll trans(ll a, int b)
{
    int ctr=0;
    ll ans=0;
    while(a!=0)
    {
        int d = a%10;
        a/=10;
        ans = ans+d*poww[b][ctr];
        ctr++;
    }
    return ans;
}
ll interpret(int x,int y)
{   ll bin2 = bin(x);
    ll bin1;
    if(y==10)
        return bin2;
    else
        bin1 = trans(bin2,y);
    return bin1;
}
int getdiv(ll x,int j)
{
    int sq = sqrt(x);
    for(int i=2;i<=sq;i++)
    {
        if((x+modexp(j,31,i))%i==0)
            return i;
    }
    return -1;
}
void print(int x)
{
    ll binn = bin(x);
    //cout<<binn<<"\n";
    int arr[32];
    int ct=31;
    while(binn!=0)
    {   //cout<<ct<<" ";
        arr[ct] = binn%10;
        binn/=10;
        ct--;
    }
    arr[0]=1;
    for(int i=1;i<=ct;i++)
        arr[i]=0;
    for(int i=0;i<32;i++)
        printf("%d",arr[i]);
    printf(" ");
}
int main(int argc, char const *argv[])
{

        for(int i=2;i<=10;i++)
    {
        ll val = 1ll;
        int ctr=0;
        while(val<=infl)
        {
            poww[i][ctr++] = val;
            val*=i;
        }
    }
    int t;
    cin>>t;
    int n,val;
    cin>>n>>val;
    int done = 0;
    for(int i=1;i<=4000;i+=2)
    {    int flag=0;
         for(int j=2;j<=10;j++)
         {
            ll  out = interpret(i,j);
             int get = getdiv(out,j);
            if(get==-1)
                break;
            else
                v[done].pb(get);
         }
         if(v[done].size()==9)
            {
            base2[done] = i;
            done++;
            }
        else
            v[done].clear();
        if(done==val)
            break;
    }
    printf("Case #1:\n");
    for(int i=0;i<val;i++)
    {   //printf("%d ",i+1);
        print(base2[i]);
        for(int j=0;j<v[i].size();j++)
        {
            printf("%d ",v[i][j]);
        }
        printf("\n");
    }
    return 0;
}
