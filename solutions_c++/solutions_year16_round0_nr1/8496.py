//#include <bits/stdc++.h>
#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<math.h>
#include<stack>
#include<stdio.h>
 
 
 
using namespace std;
 
typedef long long ll;
#define F first
#define S second
#define rep(i,n) for(i=0;i<n;i++)
#define srt(i) sort(i.begin(),i.end())
#define vct(i,n) vector<int> i(n)
#define vctp(i,n) vector < pair<int,int> > i(n);
#define arrp(i,n) pair<int,int> i[n];
#define modu(i) ((i<0)?(-1*i):(i)) //or use abs
#define endl '\n'
#define pi 3.14
 
ll MOD=1e9+7;
ll p=1e9+7;
ll fact(ll n)
{
  if(n==0)
    return 1;
  else
    return(n*fact(n-1));
}
ll power(ll x, ll y)
{
    ll res = 1;
 
    x = x % p;  
 
    while (y > 0)
    {
        if (y & 1)
            res = (res*x) % p;
 
        y = y/2;
        x = (x*x) % p;  
    }
    
    return res;
}
 template <typename T>
T modpow(T base, T exp, T modulus) {
  base %= modulus;
  T result = 1;
  while (exp > 0) {
    if (exp & 1) result = (result * base) % modulus;
    base = (base * base) % modulus;
    exp >>= 1;
  }
  return result;
}
 
int main()  
{
  bool f=1,f2=1;
    ios_base::sync_with_stdio(false);cin.tie(NULL);
   int t;
   cin>>t;
   for(int k=1;k<=t;k++)
            {
              ll n,m;
              cin>>n;
              //n==0
              int ar[10]={0};
              int i;
              bool f=0;
              for(i=1;i<1000000;i++)
              {
                f=1;
                ll nn=n*i;
                string s = to_string(nn);
                int j;
                rep(j,s.length())
                {
                ar[s[j]-'0']=1;
                //cout<<s[j]<<"\n";
                }
                rep(j,10)
                {
                  if(ar[j]==0)
                    f=0;
                 // cout<<"j"<<ar[j]<<" ";
                }
                if(f)
                  break;
              }
              if(f)
              cout<<"Case #"<<k<<": "<<n*i<<"\n";
              else
              cout<<"Case #"<<k<<": "<<"INSOMNIA"<<"\n";
 
             
            }
 
  return 0;
 
}    