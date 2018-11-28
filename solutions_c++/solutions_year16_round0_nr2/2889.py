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

int main(){
	
 
  	scanf("%lld",&t);
  	for(z=1;z<=t;z++){
  		string s;
  		cin>>s;
  		ll prev=0;
  		i=0;
  		ans=0;
  		while(i<s.length()){
  			while(s[i]=='+' && i<s.length()){
  				prev++;
  				i++;
  			}
  			while(s[i]=='-' && i<s.length()){
  				if(i+1==s.length() || (i<s.length() && s[i+1]=='+')){
  					ans+=((prev==0)?0:1)+1;
  				}
  				i++;
  			}
  		}
  		printf("Case #%lld: %lld\n",z,ans);
  		//cout<<ans<<endl;
  	}
  	
	return 0;
		
		
}