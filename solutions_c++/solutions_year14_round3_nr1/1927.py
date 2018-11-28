#include <stdio.h>
#include <math.h>

long gcd(long x, long y){
	if(y == 0){
		return x;
	}
	else{
		return gcd(y, x%y);
	}
}

double logXX(long a, long b){
	return log((double)a)/log((double)b);
}

int main(void){
	int T;
	int case_count=1;
	scanf("%d", &T);
	while(T--){
		long p, q;
		scanf("%ld/%ld",&p, &q);
		long gcd_value = gcd(p, q);
		//printf("%ld\n", gcd_value);
		p /= gcd_value;
		q /= gcd_value;
		double half_check = (1.0*p)/(1.0*q);

		double lg_value = logXX((double)q, 2.0);
		int lg_value_int = (long)lg_value;
		//printf("%d %f\n", lg_value_int, lg_value);

		if(lg_value_int != lg_value){
			printf("Case #%d: impossible\n", case_count++);
			continue;
		}

		int loop_count=1;
		if(half_check >= 0.5){
			printf("Case #%d: %d\n", case_count++, loop_count);
			continue;
		}
		while(true){
			loop_count++;
			q /= 2;
			half_check = (1.0*p)/(1.0*q);
			if(half_check >= 0.5){
				printf("Case #%d: %d\n", case_count++, loop_count);
				break;
			}
		}
	}
	return 0;
}