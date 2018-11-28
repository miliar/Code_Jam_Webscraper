//Jakub "Cubix651" Cisło
//Task: Ticket Swapping
#include <cstdio>
#include <vector>
#include <algorithm>
#define ST first
#define ND second
#define MP make_pair
#define PB push_back
using namespace std;
typedef unsigned long long LL;

const LL MOD = 1000002013;

int n, m, t;
vector<pair<int, int> > S, T;

LL cost(int o, int e)
{
	int k = e-o;
	return ((LL)n*k - (LL)k*(k-1)/2);
}

LL solve()
{
	scanf("%d%d", &n, &m);
	LL org = 0, now = 0;
	int a, b, c;
	while(m--)
	{
		scanf("%d%d%d", &a, &b, &c);
		S.PB(MP(a, -c));
		S.PB(MP(b, c));
		org = (((c * (cost(a, b) % MOD)) % MOD) + org) % MOD;
	}
	//printf("%lld\n", org);
	sort(S.begin(), S.end());

	for(int i = 0; i < S.size(); ++i)
	{
		//printf("%d %d\n", S[i].ST, S[i].ND);
		if(S[i].ND < 0)
		{
			T.PB(MP(S[i].ST, -S[i].ND));
			//printf(": %d %d\n", T.back().ST, T.back().ND);
		}
		else
		{
			while(S[i].ND != 0)
			{
				if(T.back().ND <= S[i].ND)
				{
					//printf("%d %d %d %d %d\n", S[i].ST, S[i].ND, T.back().ST, T.back().ND, T.size());
					now = (((T.back().ND * (cost(T.back().ST, S[i].ST) % MOD)) % MOD) + now) % MOD;
					S[i].ND -= T.back().ND;
					T.pop_back();
				}
				else
				{
					//printf("A moze tu: %d %d %d %d %d\n", S[i].ST, S[i].ND, T.back().ST, T.back().ND, T.size());
					now = (((S[i].ND * (cost(T.back().ST, S[i].ST) % MOD)) % MOD) + now) % MOD;
					T.back().ND -= S[i].ND;
					S[i].ND = 0;
				}
			}
		}
	}
	//printf("TU: %lld\n", now);
	if(now > org)
		org += MOD;

	S.clear();
	T.clear();
	return org - now;
}

int main()
{
	scanf("%d", &t);
	for(int tt = 1; tt <= t; ++tt)
	{
		printf("Case #%d: %lld\n", tt, solve());
	}
	return 0;
}
