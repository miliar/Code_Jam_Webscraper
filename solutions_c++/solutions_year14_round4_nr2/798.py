#include <algorithm>
#include <iostream>
#include <memory.h>
#include <vector>
using namespace std;

int solve(int *const a, int n)
{
	int ret = 0;
	int b = 0;
	int e = n;
	for (int i = 0; i < n; ++i)
	{
		int minIdx = b;
		for (int j = b+1; j < e; ++j)
		{
			if (a[j] < a[minIdx])
				minIdx = j;
		}
		int mi = a[minIdx];
		if (minIdx - b < e - minIdx - 1)
		{
			int k = minIdx - b;
			memmove(a + b + 1, a + b, k * sizeof(int));
			a[b++] = mi;
			ret += k;
		}
		else
		{
			int k = e - minIdx - 1;
			memmove(a + e - k - 1, a + e - k, k * sizeof(int));
			a[--e] = mi;
			ret += k;
		}
	}
	return ret;
}

int main(void)
{
	int cases;
	cin >> cases;
	for (int t = 0; t < cases; ++t)
	{
		int n;
		cin >> n;
		vector<int> a(n);
		for (int i = 0; i < n; ++i)
			cin >> a[i];

		int ret = solve(a.data(), n);
		cout << "Case #" << (t + 1) << ": " << ret << endl;
	}
	return 0;
}
