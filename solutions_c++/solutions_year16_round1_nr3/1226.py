#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll MAX = 1010;
bool find_perm(int a[], int n, int num)
{
	int i;
	bool flag;
	vector<int> perm;
	for (i = 1; i <= n; ++i)
	{
		if (num & (1<<(i-1)))
		{
			perm.push_back(i);
		}
	}
	sort(perm.begin(), perm.end());
	int p = (int)perm.size();
	if (p == 0)
		return false;
	else if (p == 1)
		return true;
	do
	{
		flag = true;
		for (i = 1; i < p-1; ++i)
		{
			if (a[perm[i]] != perm[i+1] && a[perm[i]] != perm[i-1])
				flag = false;
		}
		if (a[perm[0]] != perm[p-1] && a[perm[0]] != perm[1])
			flag = false;
		if (a[perm[p-1]] != perm[p-2] && a[perm[p-1]] != perm[0])
			flag = false;
		if (flag)
		{
			// for (i = 0; i < p; ++i)
			// {
			// 	cout << perm[i] << " ";
			// }
			// cout << endl;
			break;
		}
	// check p-1, 1
	}while(next_permutation(perm.begin(), perm.end()));
	return flag;
}
int main()
{
	int T, t, n, i, a[MAX], res, num;
	cin >> T;
	for (t = 1; t <= T; ++t)
	{
		cin >> n;
		for (i = 1; i <= n; ++i)
		{
			cin >> a[i];
		}
		res = 0;
		for (num = 0; num < (1 << n); ++num)
		{
			// cout << num << endl;
			if (find_perm(a, n, num))
			{
				if (__builtin_popcount(num) > __builtin_popcount(res))
					res = num;
			}
		}
		printf("Case #%d: %d\n", t, __builtin_popcount(res));
	}
	return 0;
}