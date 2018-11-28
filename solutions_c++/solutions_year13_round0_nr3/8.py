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

bool stringComp(const string& str1, const string& str2)
{
	if (str1.length() < str2.length())
		return 1;
	if (str1.length() > str2.length())
		return 0;
	return str1 < str2;
}

vector<string> results;

void init()
{
	FILE *f = fopen("builtResults.txt", "r");

	char buf[120];

	while (fscanf(f, " %*d %*s %s", buf) > 0)
	{
		results.push_back(string(buf));
	}

	sort(all(results), stringComp);

	fclose(f);
}

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

void test(int testNum)
{
	printf("Case #%d: ", testNum);

	string a, b;
	char buf[150];
	scanf(" %s", buf);
	a = string(buf);
	scanf(" %s", buf);
	b = string(buf);
	int upper = upper_bound(all(results), b, stringComp) - results.begin() - 1;
	int lower = lower_bound(all(results), a, stringComp) - results.begin() - 1;
	int res = upper - lower;

	printf("%d\n", res);
}