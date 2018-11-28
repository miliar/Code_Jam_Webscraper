#include <bits/stdc++.h>

using namespace std;

long long help[17] = {9, 19, 109, 199, 1099, 1999, 10999, 19999, 109999, 199999, 1099999, 1999999, 10999999, 19999999, 109999999, 199999999};

long long rev(long long x)
{
	vector <long long> a;
	a.clear();
	while (x > 0)
	{
		a.push_back(x % 10);
		x /= 10;
	}
	long long ret = 0;
	for (int i = 0; i < (int)a.size(); i++)
		ret = ret * 10 + a[i];
	return ret;
}


long long solve()
{
	long long x;
	cin >> x;
	long long max_base = 1;
	long long ans = 1;
	for (int i = 0; i < 17; i++)
	{
		if (max_base * 10 > x)
			break;
		max_base = max_base * 10;
		ans += help[i];
	}
	long long ans1 = ans + x - max_base;
	long long q = x;
	vector <long long> a;
	while (q > 0)
	{
		a.push_back(q % 10);
		q /= 10;
	}
	reverse(a.begin(), a.end());
	long long tmp = 0;
	for (int i = 0; i < (int)a.size(); i++)
	{
		tmp = tmp * 10 + a[i];
	//	cerr << tmp << endl;
		long long cur1 = rev(rev(tmp) + max_base);
	//	cerr << cur1 << endl;
		if (cur1 <= x)
		{
			ans1 = min(ans1, ans + rev(tmp) + 1 + x - cur1);
		}
	}
	q = 0;
	for (int i = 0; i < (int)(a.size() + 1) / 2; i++)
		q = q * 10 + a[i];
	q--;
	if (q < 0)
		return ans1;
	for (int i = (int)(a.size()  +1) /2; i < (int)a.size(); i++)
		q = q * 10 + a[i];
	a.clear();
	while (q > 0)
	{
		a.push_back(q % 10);
		q /= 10;
	}
	reverse(a.begin(), a.end());
	tmp = 0;
	for (int i = 0; i < (int)a.size(); i++)
	{
		tmp = tmp * 10 + a[i];
	//	cerr << tmp << endl;
		long long cur1 = rev(rev(tmp) + max_base);
	//	cerr << cur1 << endl;
		if (cur1 <= x)
		{
			ans1 = min(ans1, ans + rev(tmp) + 1 + x - cur1);
		}
	}
	return ans1;
}

int main()
{
	int test;
	cin >> test;
	for (int i = 1; i <= test; i++)
	{
		cout << "Case #" << i <<": " << solve() << endl;
	}
	return 0;
}