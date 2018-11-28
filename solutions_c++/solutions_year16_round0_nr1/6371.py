#include <iostream>
#include <queue>
#include <stack>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <functional>
#include <limits>

using namespace std;

void inputfunc(void);

int main(void)
{
	cin.sync_with_stdio(false);

	int T;
	cin >> T;

	for(auto i = 0; i < T; i++)
	{
		cout << "Case #" << i + 1 << ": ";
		inputfunc();
	}

	return 0;
}

void inputfunc(void)
{
	long long int N;
	cin >> N;

	if (N == N * 2 && N * 2 == N * 3)
	{
		cout << "INSOMNIA" << endl;
		return;
	}

	vector<bool> checklist(10);
	fill(checklist.begin(), checklist.end(), false);

	for (auto i = 1; ; i++)
	{
		long long int target_num = N * i;
		string converted = to_string(target_num);

		for (auto &elem : converted)
		{
			int target_digit = (int)(elem - '0');
			checklist[target_digit] = true;
		}

		bool result = true;
		for (int i = 0; i < 10; i++)
			result *= checklist[i];

		if (result)
		{
			cout << target_num << endl;
			return;
		}
	}
}
