#include <cstdio>
#include <iostream>
#include <algorithm>
#include <numeric>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <cmath>

using namespace std;

const int MOD = 1000002013;

void add(int &a, int b)
{
	a = (1LL * a + b + MOD) % MOD;
}

int f(int i, int n)
{
	return (1LL * i * n - (1LL + i) * i / 2) % MOD;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T, t, n, i, j, k, m;
	long long p;

	cin >> T;
	for(t = 1; t <= T; t++)
	{
		cin >> n >> m;
		map<int, long long> in, out;
		set<int> times;
		int ans = 0;
		while(m--)
		{
			cin >> i >> j >> k;
			in[i] += k;
			out[j] += k;
			times.insert(i);
			times.insert(j);
			add(ans, (int)(1LL * k * f(j - i, n) % MOD));
		}
		set<pair<int, long long> > heap;
		for(set<int>::iterator it = times.begin(); it != times.end(); it++)
		{
			int time = *it;
			if (in.find(time) != in.end())
				heap.insert(make_pair(time, in[time]));
			if (out.find(time) != out.end())
			{
				int q = out[time];
				while(q > 0)
				{
					pair<int, int> latest = *(--heap.end());
					heap.erase(--heap.end());
					if (latest.second > q)
					{
						heap.insert(make_pair(latest.first, latest.second - q));
						add(ans, -1LL * q * f(time - latest.first, n) % MOD);
						break;
					}
					q -= latest.second;
					add(ans, -1LL * latest.second * f(time - latest.first, n) % MOD);
				}
			}
		}
		cout << "Case #" << t << ": " << ans << endl;
	}

	return 0;
}