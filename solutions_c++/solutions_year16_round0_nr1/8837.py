// Monjurul Huda Munna
// Daffodil International University

#include <bits/stdc++.h>

using namespace std;

typedef long long int lld;

#define Max 1000009

lld result[Max];

void preCal(){
	lld i, j, k, num;
	lld n, digit[10], bit;
    for( i=1 ; i<=1000000ll ; i++){
    	memset (digit, 0, sizeof digit);
		bit = 0;
		j = 1;
		while(bit<10){
			num = i * j; j++;
			n = num;
			while(num>0){
				k = num % 10;
				num /= 10;
				if(digit[k]==0){
					bit++; digit[k] = 1;
				}
			}
		}
		result[i] = n;
	}
	return;
}


int main(){


   // freopen("input_CountingSheep.txt", "r", stdin);
//	freopen("result_CountingSheep.txt", "w", stdout);
	
	preCal();
	
    lld i, j, k, num, test, kase = 0;
    scanf ("%lld", &test);
    while(test--){
    	scanf ("%lld", &num);
    	
    	if(num != 0) printf ("Case #%lld: %lld\n", ++kase, result[num]);
    	else printf ("Case #%lld: INSOMNIA\n", ++kase);
	}


    return 0;
}

