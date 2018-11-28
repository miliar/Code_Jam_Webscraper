#include <algorithm>
#include <climits>
#include <fstream>
#include <iostream>
using namespace std;

int arr[1005], plates[1005];
bool solve(int D, int special, int mid)
{
	int count = 0;
	for (int i = 0; i < D; i++)
	{
		// Check if i'th pancake cannot be finished in mid minutes
		if (arr[i] > mid)
		{
			int diff = arr[i] - mid;
			plates[++count] = diff;
		}
	}

	int index = 1;
	while (index <= count)
	{
		if (plates[index] > 0 && special == 0)
			return false;

		if (mid >= plates[index])
			index++;
		else
			plates[index] -= mid;

		special--;
	}

	return true;
}

int main()
{
	freopen("B-input.txt", "r", stdin);
	freopen("B-output.txt", "w", stdout);

	int T;
	cin >> T;

	for (int testCase = 1; testCase <= T; testCase++)
	{
		int D;
		cin >> D;

		for (int i = 0; i < D; i++)
			cin >> arr[i];

		int result = INT_MAX;
		for (int special = 0; special <= 1000; special++)
		{
			int low = 1, high = 1000;

			while (low < high)
			{
				int mid = low + (high - low) / 2;

				// Check if we can have at most mid non-special minutes
				if (solve(D, special, mid))
					high = mid;
				else
					low = mid + 1;
			}

			if (special + low < result)
				result = special + low;
		}

		cout << "Case #" << testCase << ": " << result << endl;
	}
	return 0;
}
