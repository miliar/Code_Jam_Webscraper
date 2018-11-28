#define _USE_MATH_DEFINES
#include <stdio.h>

#include <iostream>
#include <math.h>

using namespace std;

int main(){

int N;
scanf("%d\n", &N);

for(int i=1; i<=N; i++){

	unsigned long long int r, t;
	unsigned long long int cont = 0;
	scanf("%lld %lld\n", &r, &t);
	unsigned long long int areactotal;
	unsigned long long int areacparcial;	

	unsigned long long int gasto=0;
	unsigned long long int nr = r+1;

	while(1){
		areactotal = r*r;		
		areacparcial = 	nr * nr;
		//cout << " A " << (areacparcial - areactotal) << " " << gasto << " " << t;
		gasto +=  (areacparcial - areactotal);	
		if(gasto>t)
			break;
		else{
			cont++;
			r=r+2;
			nr = r+1;
		}
	
	}

	printf("Case #%d: %lld\n", i, cont);
}

return 0;
}
