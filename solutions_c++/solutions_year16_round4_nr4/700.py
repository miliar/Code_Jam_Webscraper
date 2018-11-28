#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cstring>
#include <cstdio>
using namespace std;

int red(long long r)
{
	int res = 0;
	while (r > 0)
	{
		res++;
		r = r & (r - 1);
	}
	return res;
}

int main()
{
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; ++tt)
	{
		int n;
		cin >> n;
		char c;
		vector<long long> l;
		for (int i = 0; i < n; ++i)
		{
			long long tmp = 0;
			for (int j = 0; j < n; ++j)
			{
				cin >> c;
				tmp = tmp * 2 + c - '0';
			}
			l.push_back(tmp);
		}
		int base = 0;
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < n; ++j)
				if (l[i] & l[j])
				{
					long long nl = l[i] | l[j];
					base += red(nl - l[i]);
					l[i] = nl;
				}
		sort(l.rbegin(), l.rend());
		vector<pair<int, int> > p;
		while ((l.size() > 0) && (l.back() == 0))
		{
			p.push_back(make_pair(1, 0));
			l.pop_back();
		}
		while (l.size() > 0)
		{
			long long cur = l.back();
			int cnt = 1;
			l.pop_back();
			while ((l.size() > 0) && (l.back() == cur))
			{
				cnt++;
				l.pop_back();
			}
			p.push_back(make_pair(cnt, red(cur)));
		}
		sort(p.begin(), p.end());
		
		int res = n * n;
		do
		{
			int cur = base, cp = 0, cf = 0, cnt = 0;
			bool valid = true;
			for (int i = 0; i < p.size(); ++i)
			{
				cp += p[i].first;
				cf += p[i].second;
				cnt += p[i].first * p[i].second;
				if (cp >= cf)
				{
					cur += cp * cp - cnt;
					cp = 0;
					cf = 0;
					cnt = 0;
				}
				if (cur + max(cp, cf) * max(cp, cf) - cnt > res)
				{
					valid = false;
					break;
				}
			}
			if ((valid) && (cp == 0) && (cf == 0) && (cur < res))
				res = cur;
		} while (next_permutation(p.begin(), p.end()));
		
		cout << "Case #" << tt << ": " << res << endl;
		cerr << "Case #" << tt << ": " << res << endl;
	}

	return 0;
}
