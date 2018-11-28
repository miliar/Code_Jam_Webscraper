
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
#define mag 123456

int main(){
freopen("IP.txt","r",stdin);
freopen("OP.txt","w",stdout);
ll t;cin>>t;ll K=1;
while(t--){
   string s;cin>>s;
   string s1;
   ll n=s.size();
   s1+=s[0];
   for(ll i=1;i<n;i++){
   string a,b;
   a=s1+s[i];
   b=s[i]+s1;
   if(a>b)
    s1=a;
   else
    s1=b;
   }
cout<<"Case #"<<(K++)<<": ";
cout<<s1<<endl;
}
}
