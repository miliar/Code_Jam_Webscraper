#include <iostream>
#include <stdio.h>
using namespace std;

typedef unsigned long long ll;
ll binaryPow(ll b){
	ll p = 0;
	while(b >>= 1)
		p ++;
	return p;
}
ll oneStep(ll k){
	ll power = binaryPow(k);
	ll iter = (1 << (power + 1));
	ll count = 0;
	for(ll i = k + 1; i <= iter; i++)
		if((i & k) < k)
			count++;
	return (k + count);
}
ll solve(ll a,ll b, ll k){
//	ll p = binaryPow(b);
//	cout<<oneStep(k)<<'\n';
//	ll times = b / (1 << (binaryPow(k) + 1)), remainder = b % (1 << (binaryPow(k) + 1));
	ll sum = b * k; 

	for(ll j = k; j < a; j ++)
		for(ll l = 0; l < b; l++){
			if((j & l) < k){
				sum++;
				//	cout<<(j & l)<< " " << j<<" "<< l<<'\n';
			}
		}
	return sum;
}
void read(){
	int t;
	ll a,b,k;
	scanf("%d",&t);
	for(int i = 0; i < t; i++){
		scanf("%llu%llu%llu",&a,&b,&k);
		ll count = 0;
	//	printf("Case #%d: %llu\n",(i + 1),solve(a,b,k));
		for(ll j = 0; j < a; j ++)
			for(ll l = 0; l < b; l++){
				if((j & l) < k){
					count++;
				//	cout<<(j & l)<< " " << j<<" "<< l<<'\n';
				}
			}
		printf("Case #%d: %llu\n",(i + 1),count);
	}
}

int main(){
	freopen("f.in","r",stdin);
	freopen("f.out","w",stdout);
	read();
	return 0;

}