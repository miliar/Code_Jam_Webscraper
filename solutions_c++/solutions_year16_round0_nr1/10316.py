#pragma warning(disable : 4996)
#include <iostream>
#include <vector>
#include <set>
#include <string>

using namespace std;

int main()
{
	vector<int> ans_vec;
	set<int> number_set;
	int test_case = 0;

	ios::sync_with_stdio(false);
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> test_case;
	
	for (int i = 0; i < test_case; i++)
	{
		number_set.clear();
		int dan = 0;
		cin >> dan;
		int num = dan;

		if (dan == 0)
		{
			ans_vec.emplace_back(-1);
			continue;
		}

		while (number_set.size() != 10)
		{
			int temp = num;

			while (temp > 0)
			{
				number_set.emplace(temp % 10);
				temp /= 10;
			}

			num += dan;
		}

		ans_vec.emplace_back(num - dan);
	}

	for (int i = 0; i < ans_vec.size(); i++)
	{
		if (ans_vec.at(i) < 0)
		{
			printf("Case #%d: INSOMNIA\n", i + 1);
		}
		else
		{
			printf("Case #%d: %d\n", i + 1, ans_vec.at(i));
		}
	}

	return 0;
}