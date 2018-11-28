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
ll t,i;cin>>t;
ll K=1;
while(t--){
unordered_map<char,ll>mp;
//for(i=0;i<=25;i++){
//    mp['A'+i]=0;
//}
unordered_map<ll,ll>sum;
string s;cin>>s;
ll n=s.size();
rep(i,n){
mp[s[i]]++;
}
//
sum[0]=mp['Z'];
sum[8]=mp['G'];
sum[6]=mp['X'];
sum[4]=mp['U'];
sum[2]=mp['W'];

rep(i,sum[0])
{
mp['Z']--;mp['E']--;mp['R']--;mp['O']--;
}

rep(i,sum[8]){
mp['E']--;mp['I']--;mp['G']--;mp['H']--;mp['T']--;
}
rep(i,sum[6]){
mp['S']--;mp['I']--;mp['X']--;
}

rep(i,sum[4])
{
mp['F']--;mp['O']--;mp['R']--;mp['U']--;
}

rep(i,sum[2])
{
mp['T']--;mp['O']--;mp['W']--;
}

sum[1]=mp['O'];
sum[3]=mp['T'];
sum[7]=mp['S'];
sum[5]=mp['F'];
sum[9]=mp['I']-sum[5];
cout<<"Case #"<<K++<<": ";
for(i=0;i<=9;i++)
    for(ll j=0;j<sum[i];j++)
    cout<<i;
    cout<<endl;

}//

}

