#include <stdio.h>
#include <math.h>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <memory.h>

using namespace std;

#define pb push_back
#define mp make_pair

typedef long long lint;
typedef unsigned long long ull;

const int INF = 1000000000;
const lint LINF = 1000000000000000000ll;
const double eps = 1e-8;

char s[105];

void solve()
{
	int n, l;
	scanf("%d%d", &n, &l);

	set< string > good;
	string bad;

	for (int i = 0; i < n; i++)
	{
		scanf("%s", s);
		good.insert(string(s));
	}

	scanf("%s", s);
	bad = string(s);

	if (good.find(bad) != good.end())
	{
		printf("IMPOSSIBLE\n");
		return;
	}

	if (l == 1)
	{
		printf("? 0\n");
		return;
	}

	printf("?");
	for (int i = 1; i < l; i++)
		printf("0?");

	printf(" ");
	for (int i = 1; i < l; i++)
		printf("1");

	printf("\n");
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tn;
	scanf("%d", &tn);
	for (int i = 0; i < tn; i++)
	{
		fprintf(stderr, "Test #%d\n", i + 1);
		printf("Case #%d: ", i + 1);
		solve();
	}

	return 0;
}
