#include <iostream>

using namespace std;

long solve(long N)
{
	if (N == 0)
	{
		return -1;
	}

	bool digitChecks[10] = { false };

	int i = 1;
	while (true) {
		int currentCount = N * i;
		string currentCountStr = to_string(currentCount);
		for(const char& c : currentCountStr) {
			digitChecks[c - '0'] = true;
		}

		bool isFallAsleep = true;
		for (bool check: digitChecks) {
			if (check == false) {
				isFallAsleep = false;
			}
		}

		if (isFallAsleep) {
			return currentCount;
		}

		i++;
	}
	return -1;
}

int main()
{
	int testCaseCount = 0;
	cin >> testCaseCount;
	for (int i = 1; i <= testCaseCount; ++i)
	{
		long N;
		cin >> N;
		long result = solve(N);
		cout << "Case #" << i << ": ";
		if (result == -1) {
			cout << "INSOMNIA";
		} else {
			cout << result;
		}
		cout << endl;
	}
}
