#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
typedef long long ll;
bool isPal(ll x);
ll A,B;
#define maxN 10000001
int fairyPal[maxN];
int cont;
int get(ll);
int main(){
		cont=0;

		for(int i=0;i<maxN;i++){
			ll j=i;
			if(isPal(j) and isPal(j*j)) {fairyPal[cont++]=j*j; 
			//cout<<j*j<<endl;
			}
		}
	int t; scanf("%d\n",&t);
	for(int caso=1;caso<=t;caso++){
		scanf("%lld %lld\n",&A,&B);
		int ans=get(B)-get(A-1);
		printf("Case #%d: %d\n",caso,ans);		
	}
return 0;}
bool isPal(ll x){
	ll y=0LL;
	ll tmp=x;
	while( tmp ){
		y=y*10LL+tmp%10;
		tmp/=10LL;
	}
	return x==y;
}
int get(ll A){
	int left=0;
	int right=cont;
	while(right-left>1){
		int med=(left+right)>>1;
		if(fairyPal[med]>A) right=med;
		else left=med;
	}
	//cout<<A<<" :"<<left<<endl;
	return left;
}
