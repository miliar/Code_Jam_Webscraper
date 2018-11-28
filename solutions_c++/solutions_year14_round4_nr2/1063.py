#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

inline int Abs(int a)
{
	return a < 0 ? -a : a;
}

int f(vector <int> arr, bool ord)
{
	int n = arr.size();
	if (!ord)
		reverse(arr.begin(), arr.end());
	int ans = 0;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < i; j++)
			if (arr[j] > arr[i])
				ans++;
	return ans;
}

int g(vector <int> arr)
{
	if (arr.size() == 1)
		return 0;
	int idx = 0;
	for (int i = 1; i < arr.size(); i++)
		if (arr[i] < arr[idx])
			idx = i;
	vector <int> cur;
	for (int i = 0; i < arr.size(); i++)
		if (i != idx)
			cur.push_back(arr[i]);
	return min(idx, int(arr.size()) - idx - 1) + g(cur);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int tc = 0; tc < t; tc++)
	{
		int n;
		cin >> n;
		vector <int> arr(n);
		for (int i = 0; i < n; i++)
			cin >> arr[i];
		int mp = 0;
		int ans = 1e9;
		for (int i = 0; i < n; i++)
			if (arr[i] > arr[mp])
				mp = i;
		for (int i = -1; i < n; i++)
		{
			/*
			int now = Abs(mp - i);
			vector <int> a1, a2, cur;
			cur = arr;
			if (mp < i)
			{
				for (int j = mp; j < i; j++)
					cur[j] = arr[j + 1];
				cur[i] = arr[mp];
			}
			else
			{
				for (int j = i; j < mp; j++)
					cur[j + 1] = arr[j];
				cur[i] = arr[mp];
			}

			for (int j = 0; j < i; j++)
				a1.push_back(cur[j]);
			for (int j = i + 1; j < n; j++)
				a2.push_back(cur[j]);
			now += f(a1, true);
			now += f(a2, false);
			ans = min(ans, now);
			if (ans == 0)
				break;
			*/
			ans = min(ans, g(arr));
			/*
			int now = 0;
			vector <int> a1, a2;
			for (int j = 0; j <= i; j++)
				a1.push_back(arr[j]);
			for (int j = i + 1; j < n; j++)
				a2.push_back(arr[j]);
			now += f(a1, true);
			now += f(a2, false);
			ans = min(ans, now);
			if (ans == 0)
				break;
			*/
		}
		printf("Case #%d: %d\n", tc + 1, ans);
	}
}