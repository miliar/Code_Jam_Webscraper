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
	string initial_state;
	cin >> initial_state;

	vector<bool> checklist(initial_state.size());
	for (int i = 0; i < initial_state.size(); i++)
		checklist[i] = (initial_state[i] == '+') ? true : false;

	int count_total = 0;
	while (true)
	{
		bool check = true;
		for (int i = (int)initial_state.size() - 1; i >= 0; i--)
		{
			if (!checklist[i])
			{
				check = false;
				for (int j = i; j >= 0; j--)
					checklist[j] = !checklist[j];
			}

			if (!check)
				break;
		}

		if (check)
			break;

		count_total++;
	}

	cout << count_total << endl;
}
