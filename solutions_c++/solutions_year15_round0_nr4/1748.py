#include <iostream>
using namespace std;

int T, X, a, b, R, C;
bool gwins;

int main() {
	scanf ("%d", &T);
	for (int t = 1 ; t <= T ; t++) {
		gwins = true;
		scanf ("%d%d%d", &X, &a, &b);
		R = max (a, b);
		C = min (a, b);
		
		if (X >= 7 || R*C % X != 0 || X >= R+1 || X >= 2*C+1)
			printf ("Case #%d: RICHARD\n", t);
		else if (X < 2*C-1)
			printf ("Case #%d: GABRIEL\n", t);
		else {
			// X = 2C -1 or 2C
			for (int c = 1 ; c <= (C-1)*(C-1) && gwins ; c++) {
				gwins = false;
				for (int r = 0 ; r <= R-C-(X-2*C+1) ; r++)
					if ((c+r*C) % X == 0) // G can find something that wins
						gwins = true;
				if (!gwins) // R wins, this val of c works
					printf ("Case #%d: RICHARD\n", t);
			}
			if (gwins)
				printf ("Case #%d: GABRIEL\n", t);
		}
	}
	return 0;
}