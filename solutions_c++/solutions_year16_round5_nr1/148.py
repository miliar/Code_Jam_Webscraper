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

char s[20005];
int n;

char a[20005];
int ak;

void solve()
{
	scanf("%s", s);
	n = strlen(s);

	int pts = 0;

	ak = 0;
	for (int i = 0; i < n; i++)
	{
		if (ak == 0)
		{
			a[ak++] = s[i];
			continue;
		}

		if (a[ak - 1] == s[i])
		{
			pts += 10;
			ak--;
			continue;
		}

		if (n - i <= ak)
		{
			pts += 5;
			if (a[ak - 1] == s[i]) pts += 5;
			ak--;
			continue;
		}

		a[ak++] = s[i];
	}

	printf("%d", pts);

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
