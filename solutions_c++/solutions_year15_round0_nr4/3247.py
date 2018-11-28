#include "def.h"

I main() {
	I k;

	S(k);
	Fe(t,1,k) {
		I X; S(X);
		I R; S(R);
		I C; S(C);

		if (X >= 7) {
			printf("Case #%d: RICHARD\n",t);
			continue;
		}

		if (R*C % X != 0) {
			printf("Case #%d: RICHARD\n",t);
			continue;
		}

		if (max(R,C) < X) {
			printf("Case #%d: RICHARD\n",t);
			continue;
		}

		if ((X==1) || (X==2)) {
			printf("Case #%d: GABRIEL\n",t);
			continue;
		}

		if (min(R,C) < (X+1)/2) {
			printf("Case #%d: RICHARD\n",t);
			continue;
		}

		if ((min(R,C)==(X+1)/2) && ((max(R,C) <= (X/2 + 1)) || ((R*C/X <= 2) && (X>3)))){
			printf("Case #%d: RICHARD\n",t);
			continue;
		}

		printf("Case #%d: GABRIEL\n",t);

	}
}