#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

#define FOR(i, a, b) for(i = (a) ; i<(b) ; i++)
#define RFOR(i, a, b) for(i = (a)-1 ; i>=(b); i--)
#define MEM(a,b) memset(a,b,sizeof(a))

#define SMALL 1
//#define SMALL 0

void Solve()
{
	int K, C, S, i;
	cin >> K >> C >> S;

	if (S == K)
	{
		FOR(i, 0, K)
		{
			(i < K - 1) ? cout << i + 1 << " " : cout << i + 1 << endl;
		}
	}
}

int main()
{
	if (SMALL)
	{
		freopen("D-small-attempt0.in", "r", stdin);
		freopen("D-small-attempt0.out", "w", stdout);
	}
	else
	{
		freopen("D-large.in", "r", stdin);
		freopen("D-large.out", "w", stdout);
	}

	int t, T;
	cin >> T;
	FOR(t, 0, T)
	{
		cout << "Case #" << t + 1 << ": ";
		Solve();
	}

	return 0;
}