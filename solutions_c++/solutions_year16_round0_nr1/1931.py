#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;
using ll = long long;

void SolveCase(int caseId);
ll GetResult(ll N);

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
	int N;
	scanf("%d", &N);
	if(N == 0)
		printf("Case #%d: INSOMNIA\n", caseId);
	else
		printf("Case #%d: %lld\n", caseId, GetResult(N));
}

ll GetResult(ll N)
{
	int digitsLeft = 10;
	bool digitOccured[10];
	for(int i = 0; i < 10; ++i)
		digitOccured[i] = false;
	
	auto CheckNumber = [&digitsLeft, &digitOccured](ll x) -> bool
	{
		while(x > 0)
		{
			auto r = x % 10;
			auto nextX = x / 10;
			if(not digitOccured[r])
			{
				digitOccured[r] = true;
				--digitsLeft;
			}
			x = nextX;
		}
		return digitsLeft == 0;
	};
	
	ll current = N;
	while(not CheckNumber(current))
		current += N;
	return current;
}
