#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

int getMaxInRange(const vector<int>& lol, int start, int end)
{
	int max = -3000;
	for (int i = start; i < end; i++)
		if (lol[i] > max)
			max = lol[i];
	return max;
}
int getWaitingCost(const vector<int>& lol)
{
	return getMaxInRange(lol, 0, (int)lol.size());
}
int bruteforce(vector<int>& lol, int youpi = 0)
{
	if (youpi >= (int)lol.size())
		return getWaitingCost(lol);
	
	int minVal = bruteforce(lol, youpi + 1);
	int initialVal = lol[youpi];
	int startVal = 1;
	if (youpi > 0)
		startVal = getMaxInRange(lol, 0, youpi);
	for (int i = startVal; i < initialVal; i++)
	{
		int res = 3000;
		if (i > 0)
		{
			lol[youpi] = i;
			lol.push_back(initialVal - i);

			res = bruteforce(lol, youpi + 1) + 1;

			lol.pop_back();
			lol[youpi] = initialVal;
		}
		else
			res = bruteforce(lol, youpi + 1);

		if (res < minVal)
			minVal = res;
	}
	return minVal;
}

int main()
{
	int nbTests;
	cin >> nbTests;
	for (int testId = 0; testId < nbTests; testId++)
	{
		vector<int> lol;
		lol.reserve(1000);
		int D;
		cin >> D;
		lol.resize(D);
		for (int i = 0; i < D; i++)
			cin >> lol[i];

		// Trie la liste des lol
		sort(lol.begin(), lol.end(), greater<int>());

		cout << "Case #" << testId + 1 << ": " << bruteforce(lol) << endl;
	}

	return EXIT_SUCCESS;
}
