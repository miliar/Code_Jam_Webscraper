#include<iostream>
#include<vector>
#include<stdio.h>
#include<math.h>
#include<algorithm>
#include <deque>
#include<map>
#include<string>
#include <sstream>
#include<set>
using namespace std;
#define f(i,a,b) for(ll i=a;i<b;i++)
#define fr(i,a,b) for(ll i=a;i>=b;i--)
#define ff(i,a,b,c) for(int i=a;i<b;i+=c)
#define w(n) while(n>0)
#define vi vector<int>
#define vll vector<long long int>
typedef pair<pair<int,int> ,int> PII;
typedef pair<long long int,long long int> PI;
typedef pair<long long int, pair<int,int> > Pli;
typedef pair<int,string> PS;
typedef long long int ll;
typedef int I;
typedef string S;
ll mod_pow(ll a,ll n,ll b){ll res = 1;while(n){if(n&1) {res = (res*a)%b;}a = (a*a)%b;n >>= 1;}return res%b;}
ll mod_div(ll a,ll b,ll md){ll ans = (a*mod_pow(b,md-2,md))%md; return ans;}
ll mul(ll a,ll b,ll md){ return (ll)(a*b)%md;}
ll gcd(ll n,ll m){if(m<=n && n%m==0)return m;if(n<m)return gcd(m,n);else return gcd(m,n%m);}
ll add(ll a,ll b,ll md){a=((a%md)+(b%md))%md;return a;}
ll sub(ll a,ll b,ll md){return add(a,md-b,md);}
ll bC(int n,int r){ll ans=1;if(r>n-r)r=n-r;f(i,1,r+1)ans=(ans*(n-i+1))/(i);return ans;}
I ti=1;
deque<char> temp;
I main()
{
    char path[100],outpath[100];
    cin>>path>>outpath;
    FILE *in=fopen(path,"r");
    FILE *ou=fopen(outpath,"a");
    I t;
    fscanf(in,"%d",&t);
    char r[1001];
    w(t)
    {
        t--;
        fscanf(in,"%s",r);
        cout<<r<<endl;
        temp.push_back(r[0]);
        for(int i=1;i<1000;i++)
        {
        if(r[i]<65 || r[i]>90)break;
        if(r[i]>=temp[0])
            temp.push_front(r[i]);
        else temp.push_back(r[i]);
        }
        fprintf(ou,"Case #%d: ",ti);
        for(int i=0;i<temp.size();i++)fprintf(ou,"%c",temp[i]);
        fprintf(ou,"\n");
        temp.clear();
        ti++;
    }
}

