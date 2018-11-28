#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(void)
{
	int cases;
	cin >> cases;
	for (int t = 0; t < cases; ++t)
	{
		int n;
		cin >> n;
		vector<string> strs(n);
		for (int i = 0; i < n; ++i)
			cin >> strs[i];

		cout << "Case #" << (t + 1) << ": ";
		int ret = 0;
		vector<size_t> poss(n, 0);
		while (poss[0] < strs[0].size())
		{
			vector<int> hist(200, 0);
			char letter = strs[0][poss[0]];
			for (int i = 0; i < n; ++i)
			{
				string &s = strs[i];
				size_t &pos = poss[i];
				if (pos >= s.size() || s[pos] != letter)
					goto failed; // Must have at least one.
				size_t count = 0;
				while (pos < s.size() && s[pos] == letter)
				{
					++pos;
					++count;
				}
				hist[count]++;
			}
			// Accumulate hist
			int sumLeft = 0;
			int sumRight = 0;
			int moves = 0;
			for (int i = 1; i < 200; ++i)
			{
				moves += hist[i] * i;
				sumRight += hist[i];
			}
			int best = moves;
			for (int i = 1; i < 200; ++i)
			{
				sumLeft += hist[i - 1];
				moves += sumLeft;
				moves -= sumRight;
				sumRight -= hist[i];
				if (moves < best)
					best = moves;
			}
			ret += best;
		}
		// Check if all has finished.
		for (int i = 0; i < n; ++i)
		{
			if (poss[i] != strs[i].size())
			{
				ret = -1;
				break;
			}
		}

		if (ret != -1)
			cout << ret;
		else
		{
		failed:
			cout << "Fegla Won";
		}
		cout << endl;
	}
	return 0;
}
