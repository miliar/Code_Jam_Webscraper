/*input

*/
#include <bits/stdc++.h>
#include<stdio.h>
#include<math.h>
using namespace std;
#define pii pair<long long,long long>
#define PI 3.14159265
#define ff first
#define ss second
#define pb push_back
#define INF 1000000009
#define mod 1000000007
typedef long long ll  ;
typedef unsigned long long ull  ;
ll power(ll a , ll n)
{
    ll ans = 1, d = a;
    while (n)   
    {
        if(n&1)
          ans = (ans * d);
        d = (d*d);
        n = n>>1;
    }
    return ans;
}
ll getansw(ll   n) {
    ll   rt = sqrt(n);
    for(ll  i = 2;i<=rt;i++) 
        if(n%i==0) 
            return i;
    return -1;
}

ll tob(string s,ll b) {
    ll   n = 0;
    for(ll i = s.size()-1,j = 0;i>=0;i--,j++) 
        n+=(s[i]-48)*power(b,j);
    return n;
}

int main() 
{    
    vector<int> answ;
    ll j = 0,a1,a2,t;
    cin>>t;
    cin>>a1>>a2;
    string s;
    cout<<"Case #1:\n";
    for(ll i=0;i<50;i++) 
    {
        while(true) 
        {
            s = "1"+bitset<14>(j++).to_string()+"1";
          
            for(ll k= 2;k<=10;k++) 
            {
                ll  n = tob(s,k);
                ll  d = getansw(n);
        
                if(d == -1) 
                    break;
                else
                    answ.push_back(d);
            }
            if(answ.size() == 9 )
                break;
            else 
                answ.clear();
        }
        cout<<s;
        for(ll k=0;k<answ.size();++k) {
            cout<<" "<<answ[k];
        }
        answ.clear();
        cout<<endl;    
    }
    return 0;
}