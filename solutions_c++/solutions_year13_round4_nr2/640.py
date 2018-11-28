#include <iostream>
#include <cassert>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>
#include <fstream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <set>
#include <map>
#include <iomanip>
#define nextLine() { for (int c = getchar(); c != '\n' && c != EOF; c = getchar()); }
#define sqr(a) ((a)*(a))
#define has(mask,i) (((mask) & (1<<(i))) == 0 ? false : true)
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
using namespace std;

#define pii pair<int,int>
#define mp make_pair
#define pb push_back
#define fi first
#define se second

#if ( _WIN32 || __WIN32__ )
    #define LLD "%I64d"
#else
    #define LLD "%lld"
#endif

typedef long long LL;
typedef long double ldb;
typedef vector <int> vi;
typedef vector <vi> vvi;
typedef vector <bool> vb;
typedef vector <vb> vvb;

const int INF = (1 << 30) - 1;
const ldb EPS = 1e-9;
const ldb PI = fabs(atan2(0.0, -1.0));

int n;
LL p;

bool check(LL x)
{
	LL lt = x;
	LL place = 0;
	LL size = 1LL << n;
	for (int i = 0; lt > 0 && i < n; i++)
	{
		place += size / 2;
		lt = (lt - 1) / 2;
		size /= 2;
	}
	return place < p;
}

bool check2(LL x)
{
	LL lt = (1LL << n) - x - 1;

	LL place = 0;
	LL size = 1LL << n;
	for (int i = 0; i < n; i++)
	{
		if (lt == 0)
			place += size / 2;
		else	
			lt = (lt - 1) / 2;
		size /= 2;
	}
	return place < p;
}

LL canGuranted()
{
	LL left = 0;
	LL right = 1 << n;
	while (right - left > 1)
	{
		LL md = (left + right) / 2;
		if (check(md)) left = md;
		else right = md;
	}
	return left;
}

LL canProbably()
{
	LL left = 0;
	LL right = 1 << n;
	while (right - left > 1)
	{
		LL md = (left + right) / 2;
		if (check2(md)) left = md;
		else right = md;
	}
	return left;
}

void solve(int test)
{
	LL x = canGuranted();
	LL y = canProbably();
	printf("Case #%d: "LLD" "LLD"\n", test, x, y);
}

int main()
{
	int tests;
	scanf("%d", &tests);
	for (int test = 1; test <= tests; test++)
	{
		cin >> n >> p;
		solve(test);
	}	
	return 0;
}