//User: Shahbaz23 || Shahbaz_23

//Header Files
#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

//Macros for fast typing
#define sd(n)   scanf("%lld",&n)
//#define sld(n)  scanf("%llf",&n)//Will work only on GNU GCC and not MinGW
#define pf(n)   printf("%lld\n",n)
#define pfs(n)  printf("%lld ",n)
#define pfd(n)  printf("%llf\n",n);
#define pfds(n) printf("%llf ",n);
#define nln     printf("\n")
#define all(v)  v.begin(),v.end()
#define pb      push_back
#define mp      make_pair
#define mt      make_tuple
#define eb      emplace_back
#define xx      first
#define yy      second
#define vll     vector<ll>
#define vpll    vector<pair<ll,ll>>
#define vppll   vector<pair<ll,pair<ll,ll>>>
#define vpllb   vector<pair<ll,bool>>
#define vpsll   vector<pair<string,ll>>
#define vplls   vector<pair<ll,string>>

//Macros for debugging
#define dbugarr(a)      nln;for(auto i:a){cout<<i<<" ";}nln;
#define dbugarrp(a)     nln;for(auto i:a){cout<<i.first<<" "<<i.second;nln;}
#define dbugvec(a)      nln;for(auto i:a){cout<<i<<" ";}nln;
#define dbugvecp(a)     nln;for(auto i:a){cout<<i.first<<" "<<i.second;nln;}
#define dbugmap(a)      nln;for(auto i:a){cout<<i.first<<" "<<i.second;nln;}
#define dbugmat(a,n,m)  nln;for(ll i=0;i<n;i++){for(ll j=0;j<m;j++){cout<<a[i][j]<<" ";}nln;}

//Macros for GCC Hardware Commands
#define clz(n)      __builtin_clzll(n)
#define ctz(n)      __builtin_ctzll(n)
#define pcnt(n)     __builtin_popcountll(n)

//Namespaces
using namespace std;
using namespace __gnu_pbds;

//Redefining data types
typedef long long   ll;
typedef long double ld;
typedef tree<ll,null_type,less<ll>,rb_tree_tag,tree_order_statistics_node_update> ordered_set;

//Constants
const ll INF=LLONG_MAX;
const ll NINF=LLONG_MIN;
const ll MAX=2e6+5;
const ll MOD=1e9+7;

//GCD(a,b)
inline ll gcd(ll a,ll b)
{
    ll t;
    if(a<b)
    {
        t=a;
        a=b;
        b=t;
    }
    while(b!=0)
    {
        t=a;
        a=b;
        b=t%b;
    }
    return a;
}

//Sieve for Prime No. Generator
/*
vector<bool> ipr(100000005);
//ll prim[6*MAX];
void sieve(ll n)
{
    ll i,j;
    ipr[0]=ipr[1]=false;
    ipr[2]=true;
    for(i=4;i<n;i+=2)
    {
        ipr[i]=false;
    }
    for(i=3;i<n;i+=2)
    {
        ipr[i]=true;
    }
    for(i=3;i*i<n;i++)
    {
        if(ipr[i])
        {
            for(j=i*i;j<n;j+=2*i)
            {
                ipr[j]=false;
            }
        }
    }
    /*
    ll c=0;
    for(i=0;i<n;i++)
    {
        if(ipr[i])
        {
            prim[c++]=i;
        }
    }*//*
}
*/

//Pow(a,b)
inline ll mpow(ll a,ll b)//ll c for Pow(a,b)%c
{
    //ll c=MOD;
    ll ans=1;
    while(b!=0)
    {
        if(b&1)
        {
            ans=ans*a;
            //ans%=c;
        }
        a=a*a;
        //a%=c;
        b>>=1;
    }
    return ans;
}

//ceil(Log2(n))
inline ll mlog2(ll n)
{
    ll c=0;
    c+=64-clz(n);
    if(pcnt(n)==1)//for floor(Log2(n)) comment only this if statement
    {
        c--;
    }
    return c;
}

//Just for Troll
void troll()
{
    ll qwe[100000];
    for(ll i=0;i<1;i++);
}

//Main program starts here

ll arr[MAX],val[MAX];

bool prime(ll n)
{
    ll i;
    for(i=2;i*i<=n;i++)
    {
        if(n%i==0)
        {
            return false;
        }
    }
    return true;
}

int main()
{
    ifstream cinn("in.in");
    ofstream coutt("out.out");
    ll t,tt,i,j,k,l,n,n1,jj,flg;
    cinn>>t;
    for(tt=1;tt<=t;tt++)
    {
        cinn>>n>>jj;
        coutt<<"Case #"<<tt<<":\n";
        for(i=0;i<n-2;i++)
        {
            arr[i]=0;
        }
        k=0;
        while(k<jj)
        {
            for(i=n-3;i>=0;i--)
            {
                if(arr[i]==1)
                {
                    arr[i]=0;
                }
                else
                {
                    arr[i]=1;
                    break;
                }
            }
            flg=0;
            for(i=2;i<=10;i++)
            {
                j=1;
                n1=j*1;
                j*=i;
                for(l=n-3;l>=0;l--)
                {
                    if(arr[l]==1)
                    {
                        n1+=j;
                    }
                    j*=i;
                }
                n1+=j;
                if(prime(n1))
                {
                    flg=1;
                    break;
                }
                val[i]=n1;
            }
            if(flg==0)
            {
                coutt<<1;
                for(i=0;i<n-2;i++)
                {
                    coutt<<arr[i];
                }
                coutt<<1<<" ";
                k++;
                for(i=2;i<=10;i++)
                {
                    n1=val[i];
                    for(l=2;l*l<=n1;l++)
                    {
                        if(n1%l==0)
                        {
                            coutt<<l<<" ";
                            break;
                        }
                    }
                }
                coutt<<"\n";
            }
        }
    }
    return 0;
}
