#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;
using ll = long long;

void SolveCase(int caseId);
void Greedy(ll K, ll C);
void H(ll K, ll C, ll S);

int main()
{
	int T;
	scanf("%d", &T);
	for(int i = 1; i <= T; ++i)
		SolveCase(i);
	return 0;
}

void SolveCase(int caseId)
{
	ll K, C, S;
	scanf("%lld%lld%lld", &K, &C, &S);
	printf("Case #%d: ", caseId);
	if(K == S)
		Greedy(K, C);
	else
		H(K, C, S);
	puts("");
}

void Greedy(ll K, ll C)
{
	ll d = C == 1 ? 0 : pow(K, C-1);
	for(ll i = 1; i <= K; ++i)
	{
		ll lookupI = (i-1)*d + i;
		printf("%lld ", lookupI);
	}
}

ll GetFirstLookup(ll K, ll C);
void H(ll K, ll C, ll S)
{
	if(K >= C + S)
	{
		printf("IMPOSSIBLE");
		return;
	}
	ll left = max(max(1ll, K - C + 1), S);
	ll firstLookupI = GetFirstLookup(K, C);
	ll lastI = pow(K, C);
	for(ll i = 0; i < left && firstLookupI <= lastI; ++i)
		printf("%lld ", firstLookupI + i);
}

ll GetFirstLookup(ll K, ll C)
{
	ll lookupI = 1;
	for(ll i = 1, e = min(K, C); i < e; ++i)
		lookupI += (e-i)*pow(K, e-i);
	return lookupI;
}

