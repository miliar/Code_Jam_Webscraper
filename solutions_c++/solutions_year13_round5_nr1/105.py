#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
using namespace std;

const int fields = 37;
const long long inf = (long long) 1e15;

long long x[40], xBet[40];
long long maxBet;
int n;
double ans;

bool doubleEqual (double val1, double val2)
{
	return fabs(val1 - val2) < 1e-9;
}

bool doubleGreater (double val1, double val2)
{
	return val1 > val2 && !doubleEqual(val1, val2);
}

long long getNeedCash (int l, int r, long long bet)
{
	long long res = 0;

	for (int i = l; i <= r; i++)
	{
		if (x[i] > bet)
			throw 42;

		res += bet - x[i];
	}

	return res;
}

void getBetAns (int size, int allSize)
{
	double curAns = 0;

	for (int i = 0; i < allSize; i++)
	{
		curAns -= xBet[i] - x[i];
	}

	for (int i = 0; i < size; i++)
	{
		curAns += (1 / (size * 1.) ) * (xBet[i] - x[i] ) * 36;
	}

	if (doubleGreater(curAns, ans) )
		ans = curAns;
}

void getAns (int size, long long bet, long long & rem)
{
	if (rem < 0)
		throw 42;

	for (int i = 0; i < size; i++)
	{
		xBet[i] = bet;
	}

	getBetAns(size, size);
	for (int i = 0; i < size - 1; i++)
	{
		rem--;
		if (rem < 0)
			break;

		xBet[size - 1 - i]++;

		getBetAns(size - 1 - i, size);
	}
}

void solve ()
{
	for (int i = n; i < 37; i++)
		x[i] = 0;

	sort(x, x + fields);
	x[fields] = inf;

	ans = 0;

	long long prevMax = x[0];

	for (int i = 0; i < fields; )
	{
		int l = i, r = i;

		while (r < fields && x[r] == x[l] )
			r++;
		r--;
		i = r + 1;

		long long curMax = x[r + 1];
		long long curStart = max(curMax - 2, prevMax);

		long long cashNeed = getNeedCash(0, r, curMax);

		if (cashNeed > maxBet)
		{
			long long lb = prevMax, rb = curMax;
			long long res = prevMax;
			while (lb <= rb)
			{
				long long mid = (lb + rb) / 2;

				if (getNeedCash(0, r, mid) <= maxBet)
				{
					res = mid;
					lb = mid + 1;
				}else
				{
					rb = mid - 1;
				}
			}

			long long curStart = max(res - 5, prevMax);
			long long curMaxBet = maxBet - getNeedCash(0, r, curStart);
			for (long long temp = curStart; temp <= res; temp++)
			{
				getAns(r + 1, temp, curMaxBet);
				curMaxBet--;
			}

			break;
		}

		long long curMaxBet = maxBet - getNeedCash(0, r, curStart);
		for (long long j = curStart; j < curMax; j++)
		{
			getAns(r + 1, j, curMaxBet);
			curMaxBet--;
		}

		prevMax = curMax;
	}

	printf("%.12lf", ans);
}

int main ()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int test, t;

	scanf("%d\n", &test);
	for (t = 0; t < test; t++)
	{
		if (t)
			printf("\n");

		printf("Case #%d: ", t + 1);

		// input

		scanf("%lld%d\n", &maxBet, &n);
		for (int i = 0; i < n; i++)
		{
			scanf("%lld", &x[i] );
		}
		scanf("\n");

		// #input

		solve();
	}

	return 0;
}