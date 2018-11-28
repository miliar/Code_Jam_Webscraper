// Syed Ghulam Akbar
// CodeJam 2016

#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

void main() {
	FILE *in = freopen( "Debug\\input.txt", "r", stdin );
	FILE *out = freopen( "Debug\\output.txt", "w", stdout );

	int testCount;
	scanf("%d",&testCount);

	for (int test=1;test<=testCount;test++) {
		
		string S;
		cin >> S;

		string output = "";

		for (int i=0; i<S.length(); i++) {
			char C = S[i];

			// Compare and put this character at correct position
			if (i==0)
				output += C;
			else if (C >= output[0])
				output = C + output;
			else
				output = output + C;
		}

		cout << "Case #" << test << ": " + output;
		cout << "\n";
	}
}
