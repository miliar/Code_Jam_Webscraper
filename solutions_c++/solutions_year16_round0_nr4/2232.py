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
ll n,m,i,j,s,k,ans=0,sum=0,q,x,y,t,r,h,w,b,c,d,z;

int main(){
	
 
  	scanf("%lld",&t);
  	for(z=1;z<=t;z++){
 		cin>>k>>c>>s;
 		ll tt=modpow(k,c-1);
 		printf("Case #%lld: ",z);
 		for(i=1;i<=k;i++){
 			cout<<1+(i-1)*tt<<" ";
 		}		
 		cout<<endl;
  	}
  	
	return 0;
		
		
}