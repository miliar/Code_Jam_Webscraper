#include <algorithm>
#include <iostream>
#include <cstring>
#include <vector>
using namespace std;
const int MAX = 1005;
int s[MAX], a[MAX], mn[MAX], mx[MAX];
int main()
{
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	for (int _ = 1; _ <= t; _++)
	{
		memset(mn, 0, sizeof(mn));
		memset(mx, 0, sizeof(mx));
		memset(s, 0, sizeof(s));
		memset(a, 0, sizeof(a));
		int n, k;
		cin >> n >> k;
		for (int i = 0; i < n - k + 1; i++)
			cin >> s[i];
		for (int i = 0; i < k; i++)
		{
			a[i] = 0;
			for (int j = i; j + k < n; j += k)
			{
				a[j + k] = a[j] - s[j] + s[j + 1];
				mn[i] = min(mn[i], a[j + k]);
				mx[i] = max(mx[i], a[j + k]);
			}
		}
		s[0] %= k;
		s[0] += k;
		s[0] %= k;
		while (s[0])
		{
			int ind = 0;
			for (int i = 1; i < k; i++)
				if (mn[ind] > mn[i])
					ind = i;
			mn[ind]++;
			mx[ind]++;
			s[0]--;
		}
		while (true)
		{
			int ind1 = 0, ind2 = 0;
			for (int i = 1; i < k; i++)
			{
				if (mn[ind1] > mn[i])
					ind1 = i;
				if (mn[ind2] < mn[i])
					ind2 = i;
			}
			int val = (mn[ind2] - mn[ind1]) / 2;
			if (val == 0)
				break;
			mn[ind2] -= val;
			mx[ind2] -= val;
			mn[ind1] += val;
			mx[ind1] += val;
		}
		vector<int> vals;
		int r = 0;
		int ind = 0;
		for (int i = 1; i < k; i++)
			if (mn[ind] > mn[i])
				ind = i;
		for (int i = 0; i < k; i++)
		{
		 	vals.push_back(mx[i] - mn[i]);
			if (mn[ind] < mn[i])
				r++;
		}
		sort(vals.begin(), vals.end());
		while (r--)
		{
			int ind = 0;
			for (int i = 1; i < k; i++)
				if (vals[ind] > vals[i])
					ind = i;
			vals[ind]++;
		}
		sort(vals.begin(), vals.end());
		cout << "Case #" << _ << ": " << vals.back() << endl;
	}
	return 0;
}
