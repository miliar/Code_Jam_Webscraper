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
string flip(string s,ll ss,ll e)
{
   for(;ss<e;ss++)
   {
    char temp=s[ss];
    s[ss]=s[e];
    s[e]=temp;
   }
   return s;
}
 
int main()  
{
  bool f=1,f2=1;
    ios_base::sync_with_stdio(false);cin.tie(NULL);
   int t;
    cin>>t;
    for(int i = 1; i<= t; i++)
    {
        string s;
        cin>>s;
        int countof=0;
        int ans;
        for(int j = 0; j<= s.length()-1; j++)
        {
           if(s[j]=='+')
                countof++;
        }
        
        if(countof==s.length())
            ans=0;
            
        else 
        {  int pos;
            for(int j = s.length()-1; j>= 0; j--)
            {
                if(s[j]=='-')
                {pos = j; break;}
            }
            
            
            int count = 1;
            for(int j =0; j<= pos-1; j++)
            {
                if(s[j]!=s[j+1])
                count++;
            }
            ans = count;
        }
        
        
    cout<<"Case "<<"#"<<i<<": "<<ans<<endl; 
    }
    
   
 
  return 0;
 
}    