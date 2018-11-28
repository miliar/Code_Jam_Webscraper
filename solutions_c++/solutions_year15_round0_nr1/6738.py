#include <iostream>

using namespace std;

bool success(int* data, int n, int added)
{
	int standing = data[0] + added;

	for (int i = 1; i < n; ++i)
	{
		if (standing < i)
		{
			return false;
		}

		standing += data[i];
	}

	return true;
}

int binary(int* data, int n, int lo, int hi)
{
	int mid;
	int best = hi;

	while (lo <= hi)
	{
		mid = lo + (hi - lo) / 2;

		if (success(data, n, mid))
		{
			best = mid;
			hi = mid - 1;
		}
		else
		{
			lo = mid + 1;
		}
	}

	return best;
}

int main()
{
	int t;
	cin >> t;

	int caseNumber = 1;
	while (t-- > 0)
	{
		int s;
		cin >> s;
		int data[s + 1];

		char c;
		for (int i = 0; i <= s; ++i)
		{
			cin >> c;
			data[i] = c - '0';
		}

		int added = binary(data, s + 1, 0, s + s);

		cout << "Case #" << caseNumber << ": ";
		cout << added << endl;
		++caseNumber;
	}
}
