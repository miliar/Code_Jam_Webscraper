#include <iostream>
#include <sstream>
#include <string>
#include <iomanip>
#include <math.h>

using namespace std;

typedef unsigned long long int uint64;

bool is_palindrome(uint64 n) {
	stringstream ss;
	string input;
	ss << n;
	input = ss.str();
	
	if (input == string(input.rbegin(), input.rend()))
		return true;
	return false;
}

int main (int argc, char *argv[]) {
	
	size_t T, count = 1;
	string line;
	
	// get T
	getline(cin, line);
	stringstream(line) >> T;

	// get all cases and process it
	for(size_t count = 1; count <= T; count++) {
		uint64 result = 0;
		
		// get A, B
		uint64 A, B, max, min;
		getline(cin, line);
		stringstream(line) >> A >> B;
		// cout << "A: " << A << ", B: " << B << endl;
		
		// find the max
		min = ceil(sqrt(A));
		max = floor(sqrt(B));
		// cout << "Min: " << min << ", Max: " << max << endl;
		
		// find them
		for(uint64 i = min; i <= max; i++)
		{
			if (is_palindrome(i)) {
				uint64 n = i*i;
				if (is_palindrome(n)) {
					// cout << "i: " << i << ", n: " << n << endl;
					result++;
				}
			}
		}
		
		// print output
		cout << "Case #" << count << ": ";
		cout << result;
		cout << endl;
	}
	
	return 0;
}