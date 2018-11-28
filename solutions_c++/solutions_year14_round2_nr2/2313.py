// Syed Ghulam Akbar
// CodeJam 2014 - Round 1B

#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <math.h> 

using namespace std;

void main() {
	FILE *in = freopen( "Debug\\input.txt", "r", stdin );
	FILE *out = freopen( "Debug\\output.txt", "w", stdout );

	int testCount;
	scanf("%d",&testCount);

	for (int test=1;test<=testCount;test++) {
		long A, B, K;

		cin >> A >> B >> K;
		long result = 0;

		for (int i=0; i<A; i++)
			for (int j=0; j<B; j++)
			{
				if ( (i & j) < K)
					result++;
			}

		cout << "Case #" << test << ": " << result << endl;
	}
}
