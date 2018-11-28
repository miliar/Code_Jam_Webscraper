#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int main() {
	int t, r, c, x;
	scanf("%d", &t);

	for(int tc = 1; tc <= t; tc++) {
		scanf("%d %d %d", &x, &r, &c);

		printf("Case #%d: ", tc);

		if(x == 1) printf("GABRIEL\n");
		else if(x == 2) {
			if((r * c) % 2 == 0) printf("GABRIEL\n");
			else printf("RICHARD\n");

		} else if(x == 3) {
			if(r == 1 || c == 1 || (r * c) % 3 != 0) printf("RICHARD\n");
			else printf("GABRIEL\n");
		
		} else {
			if((r * c) % 4 != 0) printf("RICHARD\n");
			else {
				if(r == 2 && c == 2) printf("RICHARD\n");
				else if(r == 1 || c == 1) printf("RICHARD\n");
				else if((r == 2 && c == 4) || (r == 4 && c == 2)) printf("RICHARD\n");
				else if((r == 3 && c == 4) || (r == 4 && c == 3)) printf("GABRIEL\n");
				else if(r == 4 && c == 4) printf("GABRIEL\n");
			}
		}
	}

	return 0;
}