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
  		string aa="";
  		aa+=s[0];
  		for(i=1;s[i];i++){
  			if(s[i]>=aa[0]){
  				aa=s[i]+aa;
  			}
  			else
  				aa=aa+s[i];
  		}
  		printf("Case #%lld: ",z);
  		cout<<aa<<endl;
  		//cout<<aa<<endl;


   	}
  	
	return 0;
		
		
}