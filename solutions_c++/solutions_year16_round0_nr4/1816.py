#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iterator>
#include <fstream>
#include <sstream>
#include <istream>
#include <unordered_map>

using namespace std;

int main()
{
	int numCases;
	cin >> numCases;

	for (int i = 0; i<numCases; i++)
	{
		int S, C, K;
		cin >> S >> C >> K;

		cout << "Case #" << i + 1 << ": ";
		if (S>K)
			cout << "IMPOSSIBLE" << endl;
		else
		{
			for (int j = 0; j < K - 1; j++)
				cout << j + 1 << " ";
			cout << K << endl;
		}
	}

	return 0;
}