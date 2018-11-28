#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<map>
#include<set>
#include<vector>
#include<string>

using namespace std;

bool check(int new_sum, vector<int>& freq, int j)
{
	bool is_valid = true;
	for (int k = 1; k < 27; ++k)
	{
		if (freq[k] == 0 || k == j)
			continue;

		if ((new_sum) / 2 < freq[k])
		{
			is_valid = false;
			break;
		}
	}

	if (is_valid)
	{
		return true;
	}
	return false;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		int N;
		cin >> N;
		vector<int> freq(27, 0);
		int sum = 0;
		for (int j = 1; j <= N; ++j)
		{
			int tmp;
			cin >> tmp;
			freq[j] += tmp;
			sum += tmp;
		}
		vector<vector<int>> ans;

		while(sum != 0)
		{
			bool is_second = true;
			if (sum - 2 >= 0)
			{
				for (int j = 1; j < 27; ++j)
				{
					if (freq[j] == 0)
						continue;
					freq[j]--;

					for (int k = 1; k < 27; ++k)
					{
						if (freq[k] == 0)
							continue;

						if (j == k && freq[j] <= 1)
							continue;

						freq[k]--;

						if (check(sum - 2, freq, k))
						{
							sum -= 2;
							ans.push_back({ j, k });
							is_second = false;
							break;
						}
						freq[k]++;
					}

					if (!is_second)
						break;

					freq[j]++;
				}
			}	

			if (!is_second)
				continue;

			for (int j = 1; j < 27; ++j)
			{
				if (freq[j] == 0)
					continue;

				if (check(sum - 1, freq, j))
				{
					sum -= 1;
					freq[j] -= 1;
					ans.push_back({j});
					break;
				}
			}
		}
		
		printf("Case #%d:", i + 1);
		for (int j = 0; j < ans.size(); ++j)
		{
			cout << " ";
			for (int k = 0; k < ans[j].size(); ++k)
			{
				cout << (char)('A' + ans[j][k] - 1);
			}
		}
		cout << "\n";
	}
	return 0;
}