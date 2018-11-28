#include <bits/stdc++.h>
#include <math.h>

using namespace std;

int main(int argc, char* argv[]) {
  int T;
  scanf("%d", &T);
  for (int qq = 1; qq <= T; qq++) {
    char stack[100];
    // input data starts
    scanf("%s", stack);
	// input data ends

    printf("Case #%d: ", qq);
	fflush(stdout);
	int length = strlen(stack); // <= 100
	//printf("Stack = %s\n", stack);	
	// 0 is top, lenght is bottom of pile
	// Corner case, already all the right way
	bool allHappy = true;
	for (int p = 0; p < length; p++) {
		allHappy = stack[p] == '+';
		if (!allHappy) 
			break;
	}
	if (allHappy) {
		printf("0\n");
	}
	else {
		int flips = 0;
		for (int p = length-1; p >= 0; p--) {
			if (stack[p] == '-') {
				flips++;
				for (int pF = p; pF >= 0; pF--) {
					if (stack[pF] == '-') {
						stack[pF] = '+';
					}
					else {
						stack[pF] = '-';
					}
				}
				//printf("Flipped %d Stack = %s\n", flips, stack);
			}
		}
		printf("%d\n", flips);
	}
	fflush(stdout);
  }
  
  return 0;
}
