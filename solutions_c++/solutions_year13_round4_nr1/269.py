#pragma comment(linker, "/STACK:33554432")

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>
#include <memory.h>

using namespace std;

typedef long long LL;
typedef vector<int> vint;
typedef vector<vector<int> > vvint;

const int MOD = 1000002013;

int T;
LL n;
int m;

LL O[1 << 10], E[1 << 10], P[1 << 10];

LL len[1 << 11];
LL cnt[1 << 11];

LL f(LL n)
{
	return (n * (n + 1) / 2) % MOD;
}

LL cost(LL len)
{
	LL res = f(n);
	res = (res - f(n - len) + MOD) % MOD; 
	return res;
}

map<LL, int> M;

LL pos[1 << 11];
LL Min[1 << 11];
LL S[1 << 11];


int N;

int ID(LL pos)
{
	if (M[pos] == 0)
		M[pos] = M.size();
	return M[pos] - 1;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	scanf("%d", &T);
	for(int I = 1; I <= T; ++I)
	{
		scanf("%lld%d", &n, &m);

		N = 0;

		for(int i = 0; i < m; ++i)
		{
			scanf("%lld%lld%lld", &O[i], &E[i], &P[i]);
			O[i]--, E[i]--;
			pos[N] = O[i];
			pos[N + 1] = E[i];
			N += 2;
		}
		
		sort(pos, pos + N);
		
		M.clear();

		for(int i = 0; i < N; ++i)
			ID(pos[i]);


		memset(cnt, 0, sizeof(cnt));
		memset(len, 0, sizeof(len));

		for(int i = 0; i < m; ++i)
		{
			int from = ID(O[i]);
			int to = ID(E[i]);
			for(int j = from; j < to; ++j)
				cnt[j] += P[i];
		}

		for(int i = 0; i < N - 1; ++i)
			if (pos[i] != pos[i + 1])
				len[ID(pos[i])] = pos[i + 1] - pos[i];

		LL res = 0;

		for(int i = 0; i < m; ++i)
		{
			LL cur = cost(E[i] - O[i]);
			cur = (cur * P[i]) % MOD;
			res = (res + cur) % MOD;
		}

		for(int i = 0; i < N; ++i)
		{
			int from = ID(pos[i]);
			if (cnt[from])
			{
				memset(Min, 0, sizeof(Min));
				memset(S, 0, sizeof(S));
				int to = from;

				Min[from] = cnt[from];
				S[from] = len[from];
				while (cnt[to])
				{
					if (to > from)
					{
						Min[to] = min(cnt[to], Min[to - 1]);
						S[to] = S[to - 1] + len[to];
					}
					to++;
				}
				to--;
				LL cur = 0;
				for(int j = to; j >= from; --j)
				{
					if (Min[j] > cur)
					{
						LL d = Min[j] - cur;
						cur = Min[j];
						LL sub = cost(S[j]);
						sub = (d % MOD) * sub % MOD;
						res = (res - sub + MOD) % MOD;
					}
					cnt[j] -= cur;
				}
			}
		}

		printf("Case #%d: %lld\n", I, res);
	}

	return 0;
}
