#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define mag 100000 //10^8
#define inf 1e18
#define MOD 1000000007
#define rep(i,n) for(i=0;i<n;i++)
#define mset(x,v) memset(x, v, sizeof(x))
#define print_array(a,n) for(i=0;i<n;i++) cout<<a[i]<<" ";
#define var_val(x) cout<<#x<<" "<<x<<endl;
#define pb push_back
#define fi first
#define se second

int main(){
freopen("IP.txt","r",stdin);
freopen("OP.txt","w",stdout);
ll t;cin>>t;
ll k=1;
while(t--){
ll n;cin>>n;
set<ll>s;
ll i=2;
ll num=n,ans;
if(n==0){
cout<<"Case #"<<(k++)<<": ";
cout<<"INSOMNIA"<<endl;
}
else{
while(s.size()!=10){
  while(num){
    s.insert(num%10);
    num/=10;
  }
num=n*(i);
i++;
}
ans=num-n;
cout<<"Case #"<<(k++)<<": ";
cout<<ans<<endl;}
}
}
