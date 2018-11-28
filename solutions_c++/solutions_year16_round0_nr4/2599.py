#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define inf 1e18
#define MOD 1000000007
#define rep(i,n) for(i=0;i<n;i++)
#define mset(x,v) memset(x, v, sizeof(x))
#define print_array(a,n) for(i=0;i<n;i++) cout<<a[i]<<" ";
#define var_val(x) cout<<#x<<" "<<x<<endl;
#define pb push_back
#define fe first
#define se second

ll func(ll a,ll n)
{ll res=1;
ll temp=a;
while(n!=0){
    if(n%2==1)
    {
        res=res*(temp);

    }
n=n/2;
temp=temp*temp;
}
return res;
}



int main(){
ll t;cin>>t;
while(t--){
    ll k,c,s;cin>>k>>c>>s;
    ll ans=func(k,c-1);
    for(i=1;i<=k;i++)
        cout<<i*ans;

}
}


