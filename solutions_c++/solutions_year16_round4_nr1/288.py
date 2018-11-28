#include <stdio.h>
#include <math.h>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>

using namespace std;

#define pb push_back
#define mp make_pair

typedef long long lint;
typedef unsigned long long ull;

const int INF = 1000000000;
const lint LINF = 1000000000000000000ll;
const double eps = 1e-8;

int n, r, p, s;

string w[3];

int a[5];
string checkr(int winner, int k)
{
	if (k == n)
	{
		a[winner]--;
		return w[winner];
	}

	if (winner == 0)
	{
		string p1 = checkr(0, k + 1);
		string p2 = checkr(1, k + 1);
		return (p1 < p2) ? (p1 + p2) : (p2 + p1);
	}

	if (winner == 1)
	{
		string p1 = checkr(1, k + 1);
		string p2 = checkr(2, k + 1);
		return (p1 < p2) ? (p1 + p2) : (p2 + p1);
	}

	if (winner == 2)
	{
		string p1 = checkr(0, k + 1);
		string p2 = checkr(2, k + 1);
		return (p1 < p2) ? (p1 + p2) : (p2 + p1);
	}
}

string ans;
bool check(int winner)
{
	a[0] = p;
	a[1] = r;
	a[2] = s;

	ans = checkr(winner, 0);

	if (a[0] != 0 || a[1] != 0 || a[2] != 0)
		return false;

	return true;
}

void solve()
{
	scanf("%d%d%d%d", &n, &r, &p, &s);

	w[0] = "P";
	w[1] = "R";
	w[2] = "S";

	if (check(0))
	{
		printf("%s\n", ans.c_str());
		return;
	}

	if (check(1))
	{
		printf("%s\n", ans.c_str());
		return;
	}

	if (check(2))
	{
		printf("%s\n", ans.c_str());
		return;
	}

	printf("IMPOSSIBLE");

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
		printf("Case #%d: ", i + 1);
		solve();
	}

	return 0;
}
