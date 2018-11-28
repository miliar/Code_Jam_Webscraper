// Syed Ghulam Akbar
// CodeJam 2016

#include <cstdio>
#include <iostream>
#include <algorithm>
#include <iomanip>      // std::setprecision
#include <string>

using namespace std;

void main() {
	FILE *in = freopen( "Debug\\input.txt", "r", stdin );
	FILE *out = freopen( "Debug\\output.txt", "w", stdout );

	int testCount;
	scanf("%d",&testCount);

	for (int test=1;test<=testCount;test++) {

		// Read the pankcakes order
		char S[201];
		cin >> S;

		// Start flipping from the bottom because we want our bottom pancake to be in the 
		// correct order first
		int len = strlen(S);
		long flips = 0;

		for (int i=len-1; i>=0; i--) {
			
			// Check if we need this pancake to be flipped
			if (S[i] == '-') {
				// Check how many of the top items are in the face up state. Since, during
				// slipping, these will be reversed, so we need to first slip all these 
				// first for the best stategy
				// e.g. if the state is +++---, we should flip the first three to make this +++--- to ------
				if (S[0] == '+') {
					flips++;

					int j=0;
					while (j<len-1 && S[j] == '+') {
						S[j] = '-';
						j++;
					}
				}

				// Now flip the entire stack. first of all we need to move the positions i.e. top one
				// becomes bottom one, second last beforst second last from bottom, and so on
				int j, k;
				for (j = 0, k = i; j < k; j++, k--) {
					char c = S[j];
					S[j] = S[k];
					S[k] = c;
				}

				// Now also swap the directions of the pancakes in the slipped stack
				for (j = 0; j < i; j++) {
					S[j] = (S[j] == '+' ? '-' : '+');
				}

				// Count this flip as well
				flips++;
			}
		}
		
		std::cout << "Case #" << test << ": " << flips << endl;
	}
}
