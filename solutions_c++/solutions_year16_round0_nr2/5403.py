#include <iostream>
#include <string>
#include <climits>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>
#include <utility>
#include <queue>
#include <stack>
#include <map>
#include<unordered_map>
#include <set>
#include <cstring>
#include <iomanip>
#include <list>
#include <bitset>
//#include<bits/stdc++.h>
#define itn int
#define mp make_pair
#define endl "\n"
using namespace std;
typedef long long ll;
int mod = 1e9 + 7 ;
ll powmod(ll a,ll b) {ll res=1;if(a>=mod)a%=mod;for(;b;b>>=1){if(b&1)res=res*a;if(res>=mod)res%=mod;a=a*a;if(a>=mod)a%=mod;}return res;}
ll gcd(ll a , ll b){return b==0?a:gcd(b,a%b); }

int main()
{
    freopen("/Users/shamitlal/Desktop/prac/prac4/input2.in","r",stdin);
    freopen("/Users/shamitlal/Desktop/prac/prac4/output.txt","w",stdout);
    
    string str;
    int t,r=1;
    ll dp[1000];
    cin>>t;
    for(ll ii=1;ii<=t;ii++)
    {
        cin>>str;
        dp[0]=0;
        if(str[0]=='-')
            dp[0]=1;
        
        for(int i=1;i<str.size();i++)
        {
            
            if(str[i] == '-' && str[i] == str[i-1])
                dp[i]=dp[i-1];
            else if(str[i] == '-' && str[i] != str[i-1])
                dp[i]=dp[i-1]+2;
            else if(str[i]=='+')
                dp[i]=dp[i-1];
            
        }
        
        cout<<"Case #"<<ii<<": "<<dp[str.size()-1]<<endl;
        
    }
    return 0;
}




