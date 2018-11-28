#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll MAX =  100;
int main()
{
	int t, T, i, n, k, cnt, num;
	vector<pair<int, int> > p;
	bool flag;
	string s;
	cin >> T;
	for (t = 1; t <= T; ++t)
	{
		cin >> n;
		p.clear();
		for(i = 0; i < n; ++i)
		{
			cin >> k;
			p.push_back(make_pair(k, i));
		}
		sort(p.begin(), p.end());
		flag = true;
		cout << "Case #" << t << ": ";
		while (flag)
		{
			s = "";
			cnt = num = 0;
			for (i = n-1; i >= 0; --i)
			{
				if (p[i].first == 1)
					++num;
			}
			if (num != 3)
			{
				if (p[n-1].first != 0 )
				{
					s += (char)('A'+p[n-1].second);
					--(p[n-1].first);
					++cnt;
				}
				if (p[n-2].first != 0 )
				{
					s += (char)('A'+p[n-2].second);
					--(p[n-2].first);
					++cnt;
				}
			}
			else
			{
				s += (char)('A'+p[n-1].second);
				--(p[n-1].first);
				++cnt;
			}
			cout << s << " ";
			if (cnt == 0)
				flag = false;
			sort(p.begin(), p.end());
		}
		cout << endl;
	}
	return 0;
}
