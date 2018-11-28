#include<stdio.h>
#include<math.h>

using namespace std;

typedef unsigned long long ull;

char ispal(ull num) {	
	ull mun = 0, t = num;
	
	while(num > 0) {		
		mun = mun*10 + num % 10;
		num /= 10;
	}
	
	num = t;	
	return (mun == num);
}

int main() {
	int t, n; 
	ull a , b, aa, bb;
	
	scanf("%d\n", &t);
	// printf("(%d)\n", t);
	
	// iterate over number of cases
	for(int tt=1; tt<=t; ++tt) {
		scanf("%llu %llu\n", &a, &b);
		
		n = 0;
		aa = sqrt(a);
		bb = sqrt(b);
		
		if(aa*aa < a) aa++;
		if(bb*bb < b) bb++;
		
		//printf("[%llu, %llu] \n", a, b);
		//printf("[%llu, %llu] \n", aa, bb);
		
		for(ull ii = aa; ii<=bb; ++ii) {
			if(ispal(ii)) {
				ull i = ii * ii;
				
				if(i <= b && ispal(i)) {					
					n++;
					//printf("\n\tfair: %llu, square: %llu", ii, i);
				}
			}
		}
		//printf("\n");
		printf("Case #%d: %d\n", tt, n);
		//
	}
	
	return 0;
}