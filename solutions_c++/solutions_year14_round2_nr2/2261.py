#include "def.h"

I main() {
	I k, A, B, K;

	S(k);
	Fe(t,1,k) {
		I c=0;
		S(A);S(B);S(K);
		R(i,A) {
			R(j,B) {
				if((j&i)<K) c++;
			}
		}
		printf("Case #%d: %d\n", t,c);
	}
}
