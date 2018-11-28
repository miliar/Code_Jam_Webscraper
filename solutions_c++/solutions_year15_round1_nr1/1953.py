#include <iostream>
#include <vector>

using namespace std;

int main() {

	int t;
	cin >> t;

	for (int i = 0; i < t; ++i)
	{
		int n, case1 = 0, case2 = 0, former = 0, max = 0;
		vector<int> number;
		cin >> n;

		number.clear();

		for (int j = 0; j < n; ++j)
		{
			int tmp;
			cin >> tmp;

			number.push_back(tmp);

			if (tmp < former)
			{
				case1 += former - tmp;
				if (former - tmp > max)
				{
					max = former - tmp;
				}

			}
			former = tmp;
		}

		// cout << max << endl;

		for (int j = 0; j < n - 1; ++j)
		{
			if (number[j] >= max)
			{
				case2 += max;
			}
			else
			{
				case2 += number[j];
			}
		}

		cout << "Case #" << i + 1 << ": " << case1 << " " << case2 << endl;

	}

	return 0;
}