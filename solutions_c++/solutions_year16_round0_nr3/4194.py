/*input

*/
#include <bits/stdc++.h>
#include<stdio.h>
#include<math.h>
using namespace std;
#define ff first
#define ss second
#define pb push_back
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
ll answer(ll   n) {
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
    vector<int> ans1;
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
                ll  d = answer(n);
        
                if(d == -1) 
                    break;
                else
                    ans1.push_back(d);
            }
            if(ans1.size() == 9 )
                break;
            else 
                ans1.clear();
        }
        cout<<s;
        for(ll k=0;k<ans1.size();++k) {
            cout<<" "<<ans1[k];
        }
        ans1.clear();
        cout<<endl;    
    }
    return 0;
}