// Syed Ghulam Akbar
// CodeJam 2016

#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

void main() {
	FILE *in = freopen( "Debug\\input.txt", "r", stdin );
	FILE *out = freopen( "Debug\\output.txt", "w", stdout );

	int testCount;
	scanf("%d",&testCount);

	for (int test=1;test<=testCount;test++) {
		int N;
		cin >> N;

		int S[30], sum = 0;

		for (int i=0; i<N; i++) {
			cin >> S[i];
			sum += S[i];
		}

		// Get the first and second highest numbers
		bool done = false;
		cout << "Case #" << test << ": ";

		while (!done) {
			int first = -1, second = -1; 
			int firstIndex = -1, secondIndex = -1;
			for (int i=0; i<N; i++) { 

				if (S[i] >= first) {
					second = first;
					secondIndex = firstIndex;

					// Update the highest index
					first = S[i];
					firstIndex = i;
				}
			}

			// All rows are done
			if (firstIndex == -1 || first == 0)
				break;

			// Now check if we evacuate the highest index senater at the same time
			// or if there is only one difference
			char A=0, B=0;
			if (second == first && (sum - 2) != 1) {
				A = 'A'+firstIndex;
				B = 'A'+secondIndex;

				S[firstIndex]--;
				S[secondIndex]--;
				sum = sum - 2;
			}
			else {
				A = 'A'+firstIndex;
				S[firstIndex]--;

				sum--;
			}
			
			// Print the senate group
			if (B != 0)
				cout << B;
			cout << A;

			cout << " ";
		}

		cout << "\n";
	}
}
