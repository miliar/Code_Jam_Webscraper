/*
 * ID: sfiction
 * COMP: GCJ
 * ROUND: Qualification
 * PROB: B
 */
#include <cstdio>
#include <algorithm>

using namespace std;

const char *RI = "RICHARD", *GA = "GABRIEL";

int X, R, C;

int main(){
	int cas;
	scanf("%d", &cas);
	for (int casi=1;casi<=cas;++casi){
		printf("Case #%d: ", casi);
		scanf("%d%d%d", &X, &R, &C);
		if (R > C)
			swap(R, C);
		if (X >= 7 || X > C || R * C % X != 0)
			puts(RI);
		else if (X <= 2)
			puts(GA);
		else if (R == 1)
			puts(RI);
		else if (X == 3)
			puts(GA);
		else if (X == 4)
			puts(R >= 3 ? GA : RI);
		else if (R <= 2 || C <= 2)
			puts(RI);
	}
	return 0;
}
