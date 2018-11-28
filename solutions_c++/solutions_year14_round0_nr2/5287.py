#pragma comment(linker, "/STACK:167177216")

#include <stdio.h>
#include <stack>
#include <deque>
#include <math.h>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <string>
#include <memory.h>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <time.h>
#include <bitset>
using namespace std;

#define mp make_pair
#define pb push_back
#define pii pair<int, int>
#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define x first
#define y second

typedef long long li;
typedef long double ld;
typedef unsigned long long uli;

const int INF = 1e9;
const ld eps = 1e-12;
const li mod = INF + 7;
const li INF64 = (li)(INF) * (li)(INF);

const int ddx[] = {-1, 1, 1, -1};
const int ddy[] = {1, 1, -1, -1};
const int dx[] = {-1, -1, 0, 1, 1, 1, 0, -1};
const int dy[] = {0, 1, 1, 1, 0, -1, -1, -1};
const int dx4[] = {-1, 0, 1, 0};
const int dy4[] = {0, 1, 0, -1};
const int dxh[] = {-2, -2, -1, 1, 2, 2, 1, -1};
const int dyh[] = {1, -1, -2, -2, -1, 1, 2, 2};
const string dirs[] = {"RIGHT", "UP", "LEFT", "DOWN"};

ld c, f, x;

ld ff(int mid)
{
	ld curv = 2.0;
	ld curans = 0.0;
	ld curt = 0.0;
	ld curcnt = 0.0;
	int it = 0;
	while(it < mid)
	{
		it++;
		ld need = c;
		ld t = need / curv;
		curans += t;
		curv += f;
	}

	return curans + x / curv;
}

void solve()
{
	cin >> c >> f >> x;
	//ld curv = 2.0;
	ld ans = ld(1e18);
	int l = 0, r = 100000;
	while(r - l > 2)
	{
		int mid1 = l + (r - l) / 3;
		int mid2 = r - (r - l) / 3;
		if(ff(mid1) < ff(mid2))
			r = mid2;
		else
			l = mid1;

		
	}

	for(int i = max(0, l - 2); i <= r + 2; i++)
			ans = min(ans, ff(i));
	//cout.precision(20);
	//cout << ans << endl;
	printf("%.15lf\n", ans);
	return;
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    ios_base::sync_with_stdio(false);
	int tests;
	cin >> tests;
	forn(test, tests)
	{
		cout << "Case #" << test + 1 << ": ";
		solve();
	}
	return 0;
}
