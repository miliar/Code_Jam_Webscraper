#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <string>
#include <bitset>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <stack>
#include <sstream>
#include <utility>
#include <numeric>
#include <functional>
using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define F(i,a) FOR(i,0,a)
#define ALL(x) x.begin(),x.end()
#define PB push_back
#define X first
#define Y second
#define S size()
#define MS(a, v) memset(a, v, sizeof a)
#define NL printf("\n")
#define SP system("pause")
#define INF 1e9
#define PI acos(-1)
#define EPS 1e-9
typedef long long LL;
typedef pair<int, int> pii;
typedef vector<int> vi;

double c, f, x;

double ttime(double v) { return x / v; }

double solve() {
	double vel = 2.0, ans = ttime(vel), t = 0, aux;
	while(true) {
		t += c / vel;
		vel += f;
		aux = ttime(vel);
		if(t + aux > ans) break;
		ans = t + aux;
	}
	return ans;
}

int main()
{
	// ios_base::sync_with_stdio(0);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t;
	scanf("%d", &t);
	F(tc, t) {
		scanf("%lf %lf %lf", &c, &f, &x);
		printf("Case #%d: %.7lf\n", tc + 1, solve());

	}
	return 0;
}
