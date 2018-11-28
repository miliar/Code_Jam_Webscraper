// Syed Ghulam Akbar
// CodeJam 2014

#include <cstdio>
#include <iostream>
#include <string>
#include <math.h>
#include <algorithm>

using namespace std;

void main() {
	FILE *in = freopen( "Debug\\input.txt", "r", stdin );
	FILE *out = freopen( "Debug\\output.txt", "w", stdout );

	int testCount;
	scanf("%d",&testCount);

	for (int test=1;test<=testCount;test++) {
		int K, C, S;

		cin >> K >> C >> S;

		long result[101];
		long fractileLen = pow((double)K, (double)C);

		// Check for the starting number to look for
		int startIndex = K-1;
		if (startIndex <= 1 || C == 1) 
			startIndex = 1;

		for (int i=1; i<=S; i++) {
			if (C == 1)
				result[i] = i;
			else
				result[i] = i * K - 1;

			if (result[i] == 0)
				result[i] = 1;
		}

		std::cout << "Case #" << test << ": ";
		
		// Print the result 
		for (int i=1; i<=S; i++)
			cout << result[i] << " ";

		cout << endl;
	}
}
