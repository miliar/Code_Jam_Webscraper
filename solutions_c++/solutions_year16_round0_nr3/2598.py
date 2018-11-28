#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <string>
#include <bitset>
#include <algorithm>
using namespace std;

#define FOR(i, a, b) for(i = (a) ; i<(b) ; i++)
#define RFOR(i, a, b) for(i = (a)-1 ; i>=(b); i--)
#define MEM(a,b) memset(a,b,sizeof(a))

#define SMALL 1
//#define SMALL 0

typedef long long LL;

void Solve()
{
	int N, J;
	cin >> N >> J;
	int i, j, t = 1;
	vector<LL> proofVec;
	LL val = (1 << (N-1)) +1;
	LL max,m;
	LL conv = 0;
	bitset<16> coin;
	coin.set();
	max = coin.to_ullong();

	cout << "Case #1:" << endl;
	while (val <= max && t<=J)
	{
		coin = val;
		bool IsJam = true;
		FOR(i, 2, 11)
		{
			RFOR(j, N, 0)
			{
				conv *= i;
				conv += coin[j];
			}
			LL num = 0;
			for (m = 2; m <= sqrt(double(conv)); m++)
			{
				if (conv % m == 0)
				{
					num = m;
					proofVec.push_back(m);
					break;
				}
			}
			conv = 0;
			if (num == 0)
			{
				IsJam = false;
				break;
			}
		}
		if (IsJam)
		{
			cout << coin << " ";
			FOR(i, 0, proofVec.size())
			{
				cout << proofVec[i] << " ";
			}
			cout << endl;
			t++;
		}
		proofVec.clear();
		val += 2;
	}
}

int main()
{
	if (SMALL)
	{
		freopen("C-small-attempt2.in", "r", stdin);
		freopen("C-small-attempt2.out", "w", stdout);
	}
	else
	{
		freopen("C-large.in", "r", stdin);
		freopen("C-large.out", "w", stdout);
	}

	int t;
	cin >> t;
	Solve();
	return 0;
}