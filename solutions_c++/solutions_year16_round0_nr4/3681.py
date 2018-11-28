#include <iostream>
#include <stdio.h>
#include <cstring>
#include <sstream>
using namespace std;

typedef long long ll;
#define sc(x) scanf("%d",&(x))
#define scl(x) scanf("%lld",&(x))

ll exp(ll k,ll c){
	ll result=1;
	c-=1;
	while(c!=0){
		if(c%2==1){
			result*=k;
		}
		k*=k;
		c/=2;
	}
	return result;
}

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt","w",stdout);
	
	int t;
	sc(t);
	for(int z=1;z<=t;z++){
		ll k,c,s;
		scl(k);scl(c);scl(s);
		ll t1=exp(k,c);
		//cout<<t1<<endl;
		cout<<"Case #"<<z<<": ";
		ll sol=1;
		for(int i=1;i<=k;i++){
			cout<<sol<<" ";
			sol+=t1;
		}
		cout<<endl;

	}

		
	

}