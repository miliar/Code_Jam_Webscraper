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

int N;
LL P;

LL solve1()
{
	if (P == (1LL << N)) return (1LL << N) - 1;

	int k = 0;
	LL s = 0;
	while (true)
	{
		if (s >= P) break;

		++k;
		s += 1LL << (N - k);
	}
	return (1LL << k) - 2;
}

LL solve2()
{
	//if (P == 1) return 0;

	int k = 0;
	LL s = 0;
	while (true)
	{
		if (s >= P) break;

		s += (1LL << k);
		++k;
	}

	return (1LL << N) - (1LL << (N - k + 1));
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int cs = 1; cs <= T; ++cs)
	{
		scanf("%d%I64d", &N, &P);
		LL ans1 = solve1();
		LL ans2 = solve2();
		printf("Case #%d: %I64d %I64d\n", cs, ans1, ans2);
	}
	return 0;
}
