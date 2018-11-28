#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
vector<string> v;
vector<vector<ll> > nums;	

ll myexp(ll x, ll n)
{
	ll res = 1;
	while (n > 0)
	{
		if (n&1)
		{
			res = res*x;
			n -= 1;
		}
		else
		{
			x = x*x;
			n /= 2;
		}
	}
	return res;
}

void rec(string s, ll idx, ll diff, ll &cnt, ll k)
{
	if (cnt >= k)
		return;
	if (idx + diff >= s.length()-diff-1)
		return;
	string temp = s;
	temp[idx] = '1';
	temp[idx+diff] = '1';
	nums.push_back(vector<ll>(0));
	v.push_back(temp);
	// cout << temp << endl;
	for (ll j = 2; j <= 10; ++j)
	{
		nums[cnt].push_back(1 + myexp(j, diff));
	}
	++cnt;
	for (ll j = idx+diff+1; j <= s.length()-diff-1; ++j)
	{
		rec(temp, j, diff, cnt, k);
	}
}

int main()
{
	ll n, t, numpairs, i, j, k, diff, T, cnt;
	string s, temp;
	cin >> T;
	for (t = 1; t <= T; ++t)
	{
		cin >> n >> k;
		v.clear();
		nums.clear();
		diff = 1;
		if (n == 16)
		{
			s = "1000000000000001";
		}
		else if (n == 32)
		{
			s = "10000000000000000000000000000001";
		}
		cnt = 0;
		while (diff < n && cnt <= k)
		{
			temp = s;
			temp[diff] = '1';
			temp[n-diff-1] = '1';
			// cout << diff << endl;
			for (i = diff+1; i < n-diff-1; ++i)
			{
				rec(temp, i, diff, cnt, k);
			}
			++diff;
		}
		// cout << v.size() << endl;
		cout << "Case #" << t << ": " << endl;
		for (i = 0; i < v.size(); ++i)
		{
			cout << v[i] << " ";
			// cout << nums[i].size() << endl;
			for (j = 0; j < nums[i].size(); ++j)
			{
				cout << nums[i][j] << " ";
			}
			cout << endl;
		}
	}
	return 0;
}