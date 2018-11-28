// Syed Ghulam Akbar
// CodeJam 2015

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
		long n = 0, standing = 0, needed = 0;
		string shyness = "";

		// Get the input
		cin >> n >> shyness;

		// Process all the input and caclulated needed audience count
		for (int i=0; i<n+1; i++)
		{
			int Si = shyness[i] - '0';

			if (Si > 0 && i > standing)
			{
				needed += (i - standing);
				standing += (i - standing);
			}

			standing += Si;
		}

		cout << "Case #" << test << ": " << needed << endl;
	}
}
