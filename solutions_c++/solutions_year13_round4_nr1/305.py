#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <set>
#include <map>
#include <numeric>
#include <functional>

#define rep(i,n) for(int i=0;i<(n);++i)
#define foreach(i,v) for(__typeof(v.begin()) i=v.begin();i!=v.end();++i)
#define ass(v) (v)||++*(int*)0;

using namespace std;

typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<bool> VB;
typedef vector<double> VD;
typedef long long LL;

const LL MOD = 1000002013;
const int MAX_M = 1024;

int N, M;
int O[MAX_M], E[MAX_M], P[MAX_M];

inline LL cost(LL len)
{
	return len * (len - 1) / 2 % MOD;
}

int solve()
{
	VI pos;
	for (int i = 0; i < M; ++i)
	{
		pos.push_back(O[i]);
		pos.push_back(E[i]);
	}
	sort(pos.begin(), pos.end());
	pos.resize(unique(pos.begin(), pos.end()) - pos.begin());

	int sz = pos.size();
	vector<LL> cnt(sz - 1, 0L);
	for (int i = 0; i < M; ++i)
	{
		int st = lower_bound(pos.begin(), pos.end(), O[i]) - pos.begin();
		int ed = lower_bound(pos.begin(), pos.end(), E[i]) - pos.begin();
		for (int j = st; j < ed; ++j)
		{
			cnt[j] += P[i];
		}
	}

	LL cost2 = 0;
	while (true)
	{
		bool done = true;
		for (int i = 0, j = 0; i < sz - 1; )
		{
			while (i < sz - 1 && cnt[i] == 0) ++i;
			j = i;
			while (j < sz - 1 && cnt[j] > 0) ++j;
			if (i >= sz - 1) break;

			done = false;

			LL gap = cnt[i];
			for (int k = i + 1; k < j; ++k)
			{
				if (gap > cnt[k]) gap = cnt[k];
			}
			for (int k = i; k < j; ++k)
			{
				cnt[k] -= gap;
			}

			gap %= MOD;
			cost2 += cost(pos[j] - pos[i]) * gap % MOD;
			cost2 %= MOD;

			i = j;
		}
		if (done) break;
	}

	LL cost1 = 0;
	for (int i = 0; i < M; ++i)
	{
		cost1 += cost(E[i] - O[i]) * P[i] % MOD;
		cost1 %= MOD;
	}

	//printf("cost1=%I64d cost2=%I64d\n", cost1, cost2);

	return (cost2 - cost1 + MOD) % MOD;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int cs = 1; cs <= T; ++cs)
	{
		scanf("%d%d", &N, &M);
		for (int i = 0; i < M; ++i)
		{
			scanf("%d%d%d", &O[i], &E[i], &P[i]);
		}

		int ans = solve();
		printf("Case #%d: %d\n", cs, ans);
	}

	return 0;
}
