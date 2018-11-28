#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>
#include <set>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <cmath>

using namespace std;

void solveProblem(unsigned long a, unsigned long b, unsigned long k) {
	unsigned long result = 0;
	unsigned long less = min(a, b);
	unsigned long bigger = max(a, b);

	// Obvious
	unsigned long border = min(k, less);
	result += (border) * (border);

	if(less - border > 0)
	{
		result += (less - border) * border;
	}

	if(bigger - border > 0)
	{
		result += (bigger - border) * border;
	}

	// Calculate
	for(unsigned long i = border; i < less; ++i)
	{
		for(unsigned long j = border; j < bigger; ++j)
		{
			if((i & j) < k)
			{
				++result;
			}
		}
	}

	cout << result;
}

int main() {
	int testCases = 0;
	cin >> testCases;

	for (int i = 1; i <= testCases; ++i) {
		unsigned long a, b, k;
		cin >> a >> b >> k;

		// Solve problem
		cout << "Case #" << i << ": ";
		solveProblem(a, b, k);
		cout << endl;
	}

	return 0;
}
