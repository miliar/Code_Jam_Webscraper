#pragma warning(disable: 4996)
#pragma comment(linker,"/STACK:64000000")
#include <iostream>
#include <sstream>
#include <stdio.h>
#include <memory.h>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <cassert>
#include <time.h>
#include <bitset>
#include <exception>
#include <functional>

using namespace std;

#define mp make_pair
#define _(a,b) memset( (a), b, sizeof( a ) )
#define all(a) a.begin(), a.end()
#define sz(a) (int)a.size()
#define fori(i,n) for (int i = 0; i < (n); ++ i)
#define forv(i,v) for (int i = 0; i < (sz(v)); ++ i)
#define fi(n) for (int i = 0; i < n; ++ i)
#define fj(n) for (int j = 0; j < n; ++ j)
typedef unsigned long long ull;
typedef long long lint;
typedef pair < int, int > pii;
typedef double ld;

const int INF = 1000 * 1000 * 1000;
const lint LINF = 1000000000000000000LL;
const double eps = 1e-9;

void prepare(string s)
{
#ifdef WIN32
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	if (s == "input_txt")
	{
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
	}
	else if (sz(s) != 0)
	{
		freopen((s + ".in").c_str(), "r", stdin);
		freopen((s + ".out").c_str(), "w", stdout);
	}
#endif
}
int n = 4;
int a[10][10];
int b[10][10];
int first, second;

ld c, f, x;

int MAGIC = 1000 * 1000 + 41;

bool Upd(ld &res, ld val)
{
	if (res > val)
	{
		res = val;
		return true;
	}
	return false;
}

void read()
{
	cin >> c >> f >> x;

	ld income = 2.;
	ld ans = x;
	ld cur_time = 0.;
	for (int i = 0; i < MAGIC; ++i)
	{
		Upd(ans, x / income + cur_time);
		cur_time += c / income;
		income += f;
	}
	printf("%.7lf", ans);
}


bool solve()
{

	return false;
}

int main()
{
	prepare("");
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		cout << "Case #" << (i + 1) << ": ";
		cerr << "Case #" << (i + 1) << endl;
		read();
		solve();
		cout << endl;
	}

	return 0;
}
