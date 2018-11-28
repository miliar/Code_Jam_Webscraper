#include "bits/stdc++.h"
#include "InfInt.h"
using namespace std;
InfInt mpow(InfInt x,InfInt n,InfInt mod){
	InfInt ans=1,t=x;
	while(n!=0){
		if(n%2!=0)
			ans*=t,ans%=mod;
		t*=t,t%=mod,n/=2;
	}
	return ans;
}
InfInt mul(InfInt a,InfInt b,InfInt mod){
	return ((a%mod)*(b%mod))%mod;
}
bool isprime(InfInt n){
	if(n==2)return true;
	if(n<2||n%2==0)return false;
	InfInt u=n-1,t=0;
	while(u%2==0){u/=2;t++;}
	InfInt sprp[3]={2,7,61};
	for(int k=0;k<3;k++){
		InfInt a=sprp[k]%n;
		if(a==0||a==1||a==n-1)continue;
		InfInt x=mpow(a,u,n);
		if(x==1||x==n-1)continue;
		for(InfInt i=0;i<t-1;i++){
			x=mul(x,x,n);
			if(x==1)return false;
			if(x==n-1)break;
		}
		if(x==n-1)continue;
		return false;
	}
	return true;
}
InfInt tran(bitset<16> a,InfInt b){
	InfInt sol=0;
	InfInt now=1;
	for(int i=0;i<16;i++){
		if(a[i])
			sol+=now;
		now*=b;
	}
	return sol;
}
bool iscoin(bitset<16> a){
	for(InfInt i=2;i<=10;i++){
		if(isprime(tran(a,i)))
			return false;
	}
	return true;
}
void coins(bitset<16> a){
	for(int i=2;i<=10;i++){
		InfInt now=tran(a,i);
		for(InfInt j=2;j<=now;j++)
			if(now%j==0){
				cout<<" "<<j;
				break; 
			}
	}
}
int main(){
	freopen("out.txt","w",stdout);
	InfInt n=16,j=50,t=1;
	cin>>t>>n>>j;
	InfInt cnt=0;
	cout<<"Case #1:"<<endl;
	for(int i=32769;i<=65535;i+=2){
		bitset<16> a(i);
		if(iscoin(a)){
			cnt++;
			cout<<a;
			coins(a);
			cout<<endl;
		}
		if(cnt==j)
			break;
	}
}
