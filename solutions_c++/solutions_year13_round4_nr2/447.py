#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>
#include <deque>
#include <map>
#include <stack>
#include <string>
#include <ctime>

using namespace std;

#define rep(x, y, z) for(int x = (y), end##x = (z); x < end##x; x++)
#define all(x) (x).begin(),(x).end()

#ifdef LOCAL_DEBUG

#define DebugPrint(...) fprintf(stderr, __VA_ARGS__);

#else

#define DebugPrint(...)

#endif

typedef long long ll;
typedef pair<int, int> pii;

void test(int testNum);
void init();

int main()
{
	//
#ifdef LOCAL_DEBUG

	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);

#else

	//freopen("test.in", "r", stdin);
	//freopen("test.out", "w", stdout);

#endif

	clock_t cl = clock();

	init();

	int tc;
	scanf("%d", &tc);

	rep(i, 0, tc)
		test(i+1);

#ifdef LOCAL_DEBUG

	fprintf(stderr, "\nTime used: %lf\n", (clock() - cl) / (double)CLOCKS_PER_SEC);

#endif

	return 0;
}

int n;

bool check1(ll num, ll p)
{
	ll greaterCount = num+1;
	ll curVal = 0;
	rep(i, 0, n)
	{
		ll cv = 0;
		if (greaterCount > 1)
			cv = 1;
		greaterCount = greaterCount / 2;

		curVal |= cv << n - i - 1;
	}
	if (curVal >= p)
		return false;
	return true;
}

bool check2(ll num, ll p)
{
	ll greaterCount = num;
	ll curVal = 0;
	ll lesserCount = 1LL << n;
	lesserCount = lesserCount - num;

	rep(i, 0, n)
	{
		ll cv = 1;
		if (lesserCount > 1)
			cv = 0;
		lesserCount = lesserCount / 2;

		curVal |= cv << n - i - 1;
	}
	if (curVal >= p)
		return false;
	return true;
}

void init()
{

}

void test(int testNum)
{
	printf("Case #%d: ", testNum);
	
	ll n, p;
	cin >> n >> p;
	::n = n;

	ll lbi = 0, ubi = (1LL << n) - 1;

	ll val1 = 0;

	ll lb = lbi, ub = ubi;

	while (lb <= ub)
	{
		ll mid = (lb + ub) / 2;
		if (check1(mid, p))
		{
			val1 = mid;
			lb = mid+1;
		}
		else
		{
			ub = mid - 1;
		}
	}

	ll val2 = 0;

	lb = lbi, ub = ubi;
	while (lb <= ub)
	{
		ll mid = (lb + ub) / 2;
		if (check2(mid, p))
		{
			val2 = mid;
			lb = mid+1;
		}
		else
		{
			ub = mid - 1;
		}
	}

	cout << val1 << " " << val2 << endl;
}