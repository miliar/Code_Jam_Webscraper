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
    freopen("/Users/shamitlal/Desktop/prac/prac4/input.in","r",stdin);
    freopen("/Users/shamitlal/Desktop/prac/prac4/output.txt","w",stdout);
    ll n,i,a;
    int t,k,m;
    set<ll>s;

    cin>>t;
    for(int ii=1;ii<=t;ii++)
    {
        i=1;
        cin>>n;
        ll temp=n;
        if(n==0)
            cout<<"Case #"<<ii<<": INSOMNIA\n";
        
        
        else{
            
            
            while(1)
            {
                a=n;
                while(a>0)
                {
                    s.insert(a%10);
                    a=a/10;
                }
                
                if(s.size() == 10)
                {
                    cout<<"Case #"<<ii<<": "<<n<<"\n";
                    break;
                } 
                
                else
                {
                    i=i+1;
                    n=i*temp;
                }
                
                
            }
        }
        s.clear();
    }
    return 0;
}
