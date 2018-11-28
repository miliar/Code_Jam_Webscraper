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

void binary(ll n){
stack<int>s;
while(n){
s.push(n&1);
n=n>>1;
}
while(!s.empty()){
cout<<s.top();
s.pop();}
}


void go1(){
set<ll>s;
ll x;
x=0;
x=x|(1<<15);
x=x|(1<<0);
x=x|(1<<8);
x=x|(1<<7);
ll sum=0;
for(ll i=1;i<=6;i++){
        for(ll j=i+1;j<=6;j++)
            for(ll k=j+1;k<=6;k++){
            ll num=x;
            num|=(1<<i);num|=(1<<j);num|=(1<<k);
            num|=(1<<(8+i));num|=(1<<(8+j));num|=(1<<(8+k));
            binary(num);
            cout<<" ";//binary
            s.insert(num);
            sum++;
                for(ll idx=2;idx<=10;idx++)
                    cout<<func(idx,0)+func(idx,i)+func(idx,j)+func(idx,7)+func(idx,k)<<" ";
            cout<<endl;
            }
}

for(ll i=1;i<=6;i++){
        for(ll j=i+1;j<=6;j++)
           {
            ll num=x;
            num|=(1<<i);num|=(1<<j);
            num|=(1<<(8+i));num|=(1<<(8+j));
           binary(num);
            cout<<" ";//binary
            s.insert(num);
            sum++;
                 for(ll idx=2;idx<=10;idx++)
                    cout<<func(idx,0)+func(idx,i)+func(idx,j)+func(idx,7)<<" ";
            cout<<endl;
            }
}

x=0;
x=x|(1<<15);
x=x|(1<<0);
for(ll i=1;i<=6;i++){
        for(ll j=i+1;j<=6;j++)
            {
            ll num=x;
            num|=(1<<i);num|=(1<<j);
            num|=(1<<(15-j+i));num|=(1<<(15-j));
            binary(num);
            cout<<" ";//binary
            s.insert(num);
            sum++;
                for(ll idx=2;idx<=10;idx++)
                    cout<<func(idx,0)+func(idx,i)+func(idx,j)<<" ";
            cout<<endl;
            }
}


}

int main(){
freopen("IP.txt","r",stdin);
freopen("OP.txt","w",stdout);
ll t,n,j;
cin>>t>>n>>j;
cout<<"Case #1:"<<endl;
go1();
}


