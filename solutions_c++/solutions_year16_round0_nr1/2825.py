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
  		cin>>n;
  		if(n==0){
  			printf("Case #%lld: INSOMNIA\n",z);
  			//cout<<"INSOMNIA"<<endl;
  			continue;
  		}
  		ll ar[10];
  		memset(ar,0,sizeof ar);
  		ll p=10;
  		ll j=1;
  		while(p){
  			y=j*n;
  			ll tt=y;
  			while(y){
  				ll zz=y%10;
  				if(ar[zz]==0)
  				{
  					p--;
  					ar[zz]=1;
  				}
  				y=y/10;
  			}
  			
  			if(p==0){
  				printf("Case #%lld: %lld\n",z,tt);
  				//cout<<tt<<endl;
  			}
  			j++;
  		}

  	}
  	
	return 0;
		
		
}