#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define xx first
#define yy second
#define mod 1000000007
#define pb push_back
ll modpow ( ll a , ll b )
{
ll res =1;
while ( b )
{
if ( b &1) res =( res * a )  ;
a =( a * a ) ;
b >>=1;
}
return res ;
}
ll n,m,i,j,k,ans=0,sum=0,q,x,y,t,r,h,w,b,c,d,z;
ll prime(ll n){
	//ll ret=0;
   for(ll i=2;i*i<=n;i++){
   		if(n%i==0){
   			return i;
   		}
   }
   return 0;
}
void solve(ll ind , string s){
	if(ind==n){
		//cout<<s<<" ";
		ll ap[11];
		int p=1;
		for(ll i=2;i<=10;i++){
			ll val=0;
			for(ll j=0;j<n;j++){
				val*=i;
				val+=s[j]-'0';
			}
			//cout<<val<<" ";
			ll tt=prime(val);
			if(tt==0){
				p=0;
			}
			else{
				ap[i]=tt;
			}
		}
		if(p==1 && d<m){
			d++;
			cout<<s<<" ";
			for(ll i=2;i<=10;i++)
				cout<<ap[i]<<" ";
			cout<<"\n";

		}
		return;
	}

	if(ind==n-1 && d<m)
	solve(ind+1,s+"1");
    else{
    	if(d<m)
    	solve(ind+1,s+"1");
        if(d<m)
    	solve(ind+1,s+"0");
    }
	

}
int main(){
	
 
  	scanf("%lld",&t);
  	for(z=1;z<=t;z++){
  		d=0;
  		cin>>n>>m;
  		printf("Case #%lld:\n",z);
  		solve(1,"1");
  	}
  	
	return 0;
		
		
}