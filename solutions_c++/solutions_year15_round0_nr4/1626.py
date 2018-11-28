#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;

int main()
{
	int T;
	scanf("%d", &T);
	int X, R, C;

	for (int i = 1; i <= T ; i ++){
	
		scanf("%d", &X);
		scanf("%d", &R);
		scanf("%d", &C);
		
		if (X == 1) {
			printf("Case #%d: GABRIEL\n", i);
			continue;
		}
		if ((X == 2) && (R*C % 2 == 0)) {
			printf("Case #%d: GABRIEL\n", i);
			continue;
		}
		if ((X == 3) && (R*C % 3 == 0)) {
			if (min(R,C) > 1) printf("Case #%d: GABRIEL\n", i);
			else printf("Case #%d: RICHARD\n", i);
			continue;
		}
		if ((X == 4) && (R*C % 4 == 0)) {
			if ((min(R,C) >= 3) && (max(R,C) >= 4))
				printf("Case #%d: GABRIEL\n", i);
			else printf("Case #%d: RICHARD\n", i);
			continue;
		}
		printf("Case #%d: RICHARD\n", i);
	}
	
}
