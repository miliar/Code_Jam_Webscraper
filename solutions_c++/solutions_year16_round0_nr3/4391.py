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


string s;
int t,r=1;
ll dp[105];
int main()
{
    freopen("input2.in","r",stdin);
    freopen("output2.txt","w",stdout);
    cin>>t;
    while(t--)
    {
        cin>>s;
        if(s[0]=='-')
            dp[0]=1;
        else dp[0]=0;
        for(int i=1;i<s.size();i++)
        {
            if(s[i]=='+')
                dp[i]=dp[i-1];
            else if(s[i] == '-' && s[i] == s[i-1])
                dp[i]=dp[i-1];
            else if(s[i] == '-' && s[i] != s[i-1])
                dp[i]=dp[i-1]+2;
            
        }
        
        cout<<"Case #"<<r<<": "<<dp[s.size()-1]<<endl;
        ++r;
    }
    return 0;
}