#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdint>
using namespace std;

void solve(uint64_t a, uint64_t b, uint64_t k)
{
	int wins = 0;
	for(uint64_t i=0; i < a; i++) {
		for(uint64_t j=0; j < b; j++) {
			if( (i & j) < k ) {
				wins++;
			}
		}
	}

	cout << wins;
}

int main()
{
	int numCases;
	cin >> numCases;
	for(int i=0; i < numCases; i++) {
		uint64_t a, b, k;
		cin >> a >> b >> k;


		cout << "Case #" << i+1 << ": ";
		solve(a, b, k);
		cout << endl;
	}

	return 0;
}
