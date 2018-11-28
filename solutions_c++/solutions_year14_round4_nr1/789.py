#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main(void)
{
	int cases;
	cin >> cases;
	for (int t = 0; t < cases; ++t)
	{
		int n, diskSize;
		cin >> n >> diskSize;
		vector<int> ss(n);
		for (int i = 0; i < n; ++i)
			cin >> ss[i];

		sort(ss.begin(), ss.end());
		int ret = 0;
		size_t b = 0;
		size_t e = ss.size();
		for (; b < e; ++ret)
		{
			if (b + 1 == e)
			{
				// One file left
				--e;
			}
			else if (ss[b] + ss[e - 1] <= diskSize)
			{
				// Store two
				++b;
				--e;
			}
			else
			{
				// Store the big one.
				--e;
			}
		}
		cout << "Case #" << (t + 1) << ": " << ret << endl;
	}
	return 0;
}
