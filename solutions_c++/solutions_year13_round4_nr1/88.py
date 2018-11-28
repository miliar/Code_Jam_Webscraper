#include <vector>
#include <algorithm>
#include <cstdio>
#include <iostream>

using namespace std;

int T, _N, _M;
long long N, M;

const long long MOD = 1000002013;

struct bus
{
	int pos;
	int inout;
	int num;

	bool operator < (const bus &b) const
	{
		if (pos != b.pos) return pos < b.pos;
		return inout < b.inout;
	}
};

int main()
{
	scanf("%d", &T);
	for (int cn = 1; cn <= T; ++cn)
	{
		scanf("%d%d", &_N, &_M);
		N = _N, M = _M;
		long long ret1 = 0, ret2 = 0;
		vector<bus> v;

		for (int i = 0; i < M; ++i)
		{
			int s, e, _p;
			long long p;
			scanf("%d%d%d", &s, &e, &_p);
			p = _p;

			long long k = e - s;
			long long t1 = (k * N) % MOD;
			long long t2 = (k * (k - 1) / 2) % MOD;
			t1 = t1 - t2;
			if (t1 < 0) t1 += MOD;
			ret1 = (ret1 + (p * t1) % MOD) % MOD;

			bus b;

			b.pos = s;
			b.inout = 0;
			b.num = _p;
			v.push_back(b);

			b.pos = e;
			b.inout = 1;
			b.num = _p;
			v.push_back(b);
		}
		sort(v.begin(), v.end());

		vector<bus> stack;
		for (int i = 0; i < v.size(); ++i)
		{
			if (v[i].inout == 0)
			{
				stack.push_back(v[i]);
			} 
			else 
			{
				int npos = v[i].pos;
				int nnum = v[i].num;

				while (nnum > 0)
				{
					int idx = stack.size() - 1;

					if (stack[idx].num >= nnum) 
					{
						// nnum Έν
						{
							long long k = npos - stack[idx].pos;
							long long t1 = (k * N) % MOD;
							long long t2 = (k * (k - 1) / 2) % MOD;
							t1 = t1 - t2;
							if (t1 < 0) t1 += MOD;
							ret2 = (ret2 + (nnum * t1) % MOD) % MOD;
						}

						stack[idx].num -= nnum;
						if (stack[idx].num == 0)
						{
							stack.pop_back();
						}
						break;
					}
					else
					{
						nnum -= stack[idx].num;
						// stack[idx].num Έν
						{
							long long k = npos - stack[idx].pos;
							long long t1 = (k * N) % MOD;
							long long t2 = (k * (k - 1) / 2) % MOD;
							t1 = t1 - t2;
							if (t1 < 0) t1 += MOD;
							ret2 = (ret2 + (stack[idx].num * t1) % MOD) % MOD;
						}
						stack.pop_back();
					}

				}
			}
		}
		ret1 -= ret2;
		if (ret1 < 0) ret1 += MOD;
		cout << "Case #" << cn << ": " << (ret1) << endl;
	}
}

