#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <climits>
#include <algorithm>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <cstdlib>
#include <string>
#include <sstream>
using namespace std;

#define sqr(x) ((x)*(x))
#define lowbit(x) ((x)&(-x))

double c, f, x;

struct node
{
	double tim;
	double fre;
	node() {}
	node(double t, double f)
	{
		tim = t;
		fre = f;
	}
};
const int MAXN = 100005;

void solve()
{
	double ans = x / 2.0;
	node pre(0, 2.0);
	node now;
	while (true)
	{
		double wait = x / pre.fre + pre.tim;
		ans = min(ans, wait);
		double need = pre.tim + c / pre.fre;
		node now(need, pre.fre + f);
//		printf("%lf\n", wait);
		if (ans < wait) break;
		pre = now;
	}
	printf("%.7lf\n", ans);
}

int main() 
{
	int T, cases = 0;
	scanf("%d", &T);
	while (T--)
	{
		scanf("%lf%lf%lf", &c, &f, &x);
		printf("Case #%d: ", ++cases);
		solve();
	}
	return 0;
}

