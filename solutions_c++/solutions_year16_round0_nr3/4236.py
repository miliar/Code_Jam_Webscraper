#include <iostream>
#include <cstdio>
#include <string>
#include <sstream>
#include <cstdlib>
#include <cmath>
using namespace std;
#define ll long long int

ll i,j,k,t,n,J,q,r,ans;	
ll use[14];
ll x;
int num[100];

ll calc(ll p){
	ans=0;
	for(q=0;q<n;q++){
		if(num[q])	ans+= (ll)pow(p,n-1-q);
	}
	return ans;
}

ll isPrime(ll y){
	ll limit = sqrt(y)+1;
	ll o,u;
	if(y==2 || y==1) return 1;
	for(o=2;o<=limit;o++){
		if(y%o==0) return o;
	}
	return 1;
}

void rec(ll idx){
	if(J==0) return;
	if(idx== n-1){
		for(j=2;j<=10;j++){
			use[j] = calc(j);
			x = isPrime(use[j]);
			if(x==1) return;
			use[j]=x;
		}
		for(j=0;j<n;j++) printf("%d",num[j]);
		printf(" ");
		for(j=2;j<=10;j++) printf("%lld ",use[j]);
		printf("\n");
		J--;
		return;	
	}
	num[idx]=0;
	rec(idx+1);

	num[idx]=1;
	rec(idx+1);
}

int main(){
	//sieve();
	scanf("%lld",&t);
	for(k=1;k<=t;k++){
		scanf("%lld%lld",&n,&J);
		num[0]=num[n-1]=1;
		printf("Case #%lld:\n",k);
		rec(1);
	}
}