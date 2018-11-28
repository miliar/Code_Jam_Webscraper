#include <algorithm>
#include <iostream>
#include <unordered_map>
#include <unordered_set>

using namespace std;

void solveProblem(long double c, long double f, long double x) {
	long double coockiesPerSecond = 2.0;
	long double bestTime = x / coockiesPerSecond;
	long double totalTime = 0.0;

	while(true)
	{
		long double farmTime = c / coockiesPerSecond;
		totalTime += farmTime;
		coockiesPerSecond += f;

		long double noFarmTime = totalTime + (x / coockiesPerSecond);
		if(noFarmTime >= bestTime)
		{
			break;
		}

		bestTime = noFarmTime;
	}

	cout.precision(7);
	cout << fixed <<  bestTime;
}

int main() {
	int testCases = 0;

	cin >> testCases;

	for (int i = 1; i <= testCases; ++i) {
		long double c, f, x;
		cin >> c >> f >> x;

		// Solve problem
		cout << "Case #" << i << ": ";
		solveProblem(c, f, x);
		cout << endl;
	}

	return 0;
}
