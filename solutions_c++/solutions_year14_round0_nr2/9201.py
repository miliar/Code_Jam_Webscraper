#include <iostream>
#include <string>
#include <set>
#include <algorithm>
#include <stack>
#include <vector>
#include <math.h>

#define FOR(i,s,e) for (int i=(s); i<(e); i++)
#define FOE(i,s,e) for (int i=(s); i<=(e); i++)
#define FOD(i,s,e) for (int i=(s)-1; i>=(e); i--)
#define CLR(a,x) memset(a, x, sizeof(a))
#define SIZE(v) ((int)(v).size())
#define FOREACH(i,v) for(typeof((v).begin()) i=(v).begin();i!=(v).end();i++)
typedef long long ll;
typedef std::pair<ll,ll> PII;
typedef std::vector<PII> VPII;
using namespace std;

void solve()
{
	double C, F, X;
	cin >> C >> F >> X;
	double min_time = X / 2.0;
	double s = 2;
	double cur_t = 0;
	double pre_time = min_time;
	while (true)
	{
		cur_t += C / s;
		s += F;
		double time = cur_t + X / s;
		if (time < min_time)	min_time = time;
		if (pre_time < time)	break;
		pre_time = time;
	}
	printf("%.7f\n", min_time);

}



int main()
{
#ifndef ONLINE_JUDGE
	freopen("B-large.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		printf("Case #%d: ", i+1);
		solve();
	}
	return 0;
}
