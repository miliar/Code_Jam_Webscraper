#include <iostream>
#include <cstdio>
#define ll long long

using namespace std;

bool all10(int n[10]){

	for(int i=0; i<10; i++){
		if(!n[i])
			return false;
	}
	return true;
}

int main(){

	int t,digits[10],cont;
	ll in,last,ever;
	scanf("%d",&t);
	for(int i=0; i<t;i++){
		cont = 1;
		scanf("%lld",&in);
		if(in == 0){
			printf("Case #%d: INSOMNIA\n",i+1);
			continue;
		}
		for(int i=0; i<10; i++){
			digits[i]=0;
		}
		ever = in;
		while(1){
			cont++;
			last = in;
			while(in!=0){
				digits[in%10] = 1;
				in/=10;
			}
			if(all10(digits))
				break;
			in = ever*cont;
		}
		printf("Case #%d: %lld\n",i+1,last);
	}

return 0;
}
