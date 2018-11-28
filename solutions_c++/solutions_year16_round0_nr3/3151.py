#include<stdio.h>
#include<stdlib.h>
#include<stdint.h>
#include <inttypes.h>
#include<math.h>

int len;

int64_t isPrime(int64_t val) {
	if(val%2==0) return 2;
	
	int64_t lim=(int64_t)(sqrt(val)+1);
	int64_t c=3;
	while(c<=lim) {
		if(val%c==0) return c;
		c+=2;
	}
	return 0;
}

bool check(uint32_t val, int base, bool print) {
	int64_t dec=0;
	int64_t mul=1;
	while(val!=0) {
		if(val&1) dec+=mul;
		mul*=base;
		val>>=1;
	}
//	if(print) printf("%d %"PRId64" ",base, dec);
	int64_t res=isPrime(dec);
	if(res==0) return false;
	if(print) printf("%"PRId64, res);
	return true;
}

bool check(uint32_t val, bool print) {
	if(print) {
		for(int i=len;i>=0;--i) {
			printf("%d", (val>>i)&1);
		}
	}
	for(int i=2;i<=10;++i) {
		if(print) printf(" ");
		if(!check(val, i, print)) return false;
	}
	if(print) printf("\n");
	return true;
}

int main(int argc, char** argv) {
	int tsts, n, j;
	
	scanf("%d %d %d",&tsts, &n, &j);
	--n;
	len=n;
	uint32_t min=(((uint32_t)1)<<n)+1;	// pierwszy i ostatni bit = 1
	uint32_t max=(((int64_t)1)<<(n+1))-1;	// wszystkie bity 1
	int res=0;

	printf("Case #1:\n");
	int64_t val=max;
	for(;;) {
//		printf("Checking %"PRId64"\n",val);
		
		if(check(val, false)) {
			check(val, true);
			if(++res==j) break;	// wszystkie wyniki
		}
		if(val==min) break;	// koniec obliczeń, choć to nie powinno nigdy nastąpić
		val-=2;
	}
	
	return 0;
}