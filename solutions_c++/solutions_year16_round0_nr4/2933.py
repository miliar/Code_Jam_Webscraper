#include<iostream>
#include<cmath>
using namespace std;
long long pow(long long a,long long b){
	long long s=1;
	while(b){
		if(b%2==1) s=s*a;
		a=a*a;
		b/=2;
	}
	return s;
}
int main(){
	long long  t,i,k,c,s,j;
	cin>>t;
	
	for(i=1;i<=t;++i){
		cin>>k>>c>>s;
		cout<<"Case #"<<i<<": ";
		for(j=0;j<k;++j) cout<<(j*pow(k,c-1)+1)<<" ";
		cout<<"\n";
	}
	
	return 0;
}
