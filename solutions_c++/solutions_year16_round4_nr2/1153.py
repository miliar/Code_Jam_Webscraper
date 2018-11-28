#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

typedef long double ld;

vector<ld> A, P;
vector<vector<pair<ld, bool>>> memo;

ld DP(int idx, int k)
{
	if(idx == int(A.size()))
	{
		if(k == 0) return 1.000000000;
		else return 0.00000;
	}
	else if(k < 0) return 0.00000;
	else if(memo[idx][k].second) return memo[idx][k].first;
	else
	{
		memo[idx][k].first = A[idx]*DP(idx+1, k-1) + (1.00-A[idx])*DP(idx+1, k);
		memo[idx][k].second = true;
		return memo[idx][k].first;
	}
}

int main(void)
{
	int t;
	scanf("%d", &t);
	for(int tt = 1;tt <= t;tt++) {
	int n, k;
	ld res = 0.0000000;
	scanf("%d%d", &n, &k);
	A.clear(); memo.clear();
	P.clear(); P.resize(n);
	for(int i = 0;i < n;i++) scanf("%Lf", &P[i]);

	for(int mask = 0;mask < (1<<n);mask++)
	{
		if(__builtin_popcount(mask) != k) continue;
		A.clear();
		memo.clear(); memo.resize(k+1, vector<pair<ld, bool>>(k/2+2, {0.00, false}));
		for(int i = 0;i < n;i++)
		{
			if(mask&(1<<i)) A.push_back(P[i]);
		}
		//cout << mask << " " << DP(0, k/2) << "\n";
		res = max(res, DP(0, k/2)); 
	}

	printf("Case #%d: %.8Lf\n", tt, res); }
}