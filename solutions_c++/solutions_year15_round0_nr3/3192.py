#include "bits/stdc++.h"
using namespace std;

typedef long long ll;

struct node{
	char c;
	int sign;
};

typedef struct node node;

node Sum(node sum, char add){
	node result;
	result.sign = sum.sign;
	switch(sum.c){
		case '1': switch(add){
					case '1': result.c = '1'; break;
					case 'i': result.c = 'i'; break;
					case 'j': result.c = 'j'; break;
					case 'k': result.c = 'k'; break;
				}
				break;
		case 'i': switch(add){
					case '1': result.c = 'i'; break;
					case 'i': result.c = '1'; result.sign *= -1; break;
					case 'j': result.c = 'k'; break;
					case 'k': result.c = 'j'; result.sign *=(-1); break;
				}
				break;
		case 'j': switch(add){
					case '1': result.c = 'j'; break;
					case 'i': result.c = 'k';result.sign *=(-1); break;
					case 'j': result.c = '1';result.sign *=(-1); break;
					case 'k': result.c = 'i'; break;
				}
				break;
		case 'k': switch(add){
					case '1': result.c = 'k'; break;
					case 'i': result.c = 'j'; break;
					case 'j': result.c = 'i'; result.sign *=(-1); break;
					case 'k': result.c = '1'; result.sign *=(-1); break;
				}
				break;
	}
	return result;
}

int main(){
	int t;
	cin >> t;
	int T = 0;
	while(t--){
		T++;
		ll l,x;
		cin >> l >> x;
		string s;
		cin >> s;
		
		node sum;
		sum.c = '1';
		sum.sign = 1;

		int flag = 0;
		for(ll j=0; j<x; j++){
			for(ll i=0; i<l; i++){
				if(flag == 0){
					sum = Sum(sum, s[i]);
					if(sum.c == 'i' && sum.sign == 1) {
						flag = 1;
						sum.c = '1';
						sum.sign = 1;
					}
				}
				else if(flag == 1){
					sum = Sum(sum, s[i]);
					if(sum.c == 'j' && sum.sign == 1) {
						flag = 2;
						sum.c = '1';
						sum.sign = 1;
					}
				}
				else if(flag == 2){
					sum = Sum(sum, s[i]);
					if(sum.c == 'k' && sum.sign == 1) {
						flag = 3;
						sum.c = '1';
						sum.sign = 1;
					}
				}
				else{
					sum = Sum(sum, s[i]);
				}
				
			}
		}

		if(sum.c == '1' && sum.sign == 1 && flag >= 3){
			printf("Case #%d: YES\n", T);
		}
		else{
			printf("Case #%d: NO\n", T);
		}
	}
}


/*
if(l*x<3){
			printf("Case #%d: NO\n", T);
			continue;
		}
	
		node result = Evaluate(s);
		if(x%4 == 0){
			result.c = '1';
			result.sign = 1;
		}
		else if(x%4==2){
			result.sign *= result.sign;
			result.c = '1';
			result.sign *= -1;
		}
		else if(x%4 == 3){
			result.sign *= -1;
		}
		if(result.sign == -1 && result.c == '1'){
			printf("Case #%d: YES\n", T);
		}
		else{
			printf("Case #%d: NO\n", T);
		}*/