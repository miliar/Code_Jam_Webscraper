#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <ctime>
#include <functional>
#include <sstream>
#include <fstream>
#include <valarray>
#include <complex>
#include <queue>
#include <cassert>
#include <bitset>
using namespace std;

#ifdef LOCAL
	#define debug_flag true
#else
	#define debug_flag false
#endif

#define dbg(args...) { if (debug_flag) { _print(_split(#args, ',').begin(), args); cerr << endl; } else { void(0);} }

vector<string> _split(const string& s, char c) {
	vector<string> v;
	stringstream ss(s);
	string x;
	while (getline(ss, x, c))
		v.emplace_back(x);
	return v;
}

void _print(vector<string>::iterator) {}
template<typename T, typename... Args>
void _print(vector<string>::iterator it, T a, Args... args) {
    string name = it -> substr((*it)[0] == ' ', it -> length());
    if (isalpha(name[0]))
	    cerr << name  << " = " << a << " ";
	else
	    cerr << name << " ";
	_print(++it, args...);
}

#ifdef LOCAL
    #define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
    #define eprintf(...) 42;
#endif

typedef long long int int64;

const int N = 203;
const int SH = 207;

int n, k;
double p[N], init_p[N];
double dp[SH * 2];
double new_dp[SH * 2];

double solve()
{
	assert(n == k);
	fill(dp, dp + SH * 2, 0);
	dp[SH] = 1;
	for (int i = 0; i < n; i++)
	{
		fill(new_dp, new_dp + 2 * SH, 0);
		for (int bal = 1; bal < 2 * SH - 1; bal++)
		{
			new_dp[bal - 1] += dp[bal] * p[i];
			new_dp[bal + 1] += dp[bal] * (1 - p[i]);
		}
		copy(new_dp, new_dp + 2 * SH, dp);
	}

	return dp[SH];
}

void solve(int test)
{
	scanf("%d%d", &n, &k);
	for (int i = 0; i < n; i++)
		scanf("%lf", &init_p[i]);
	sort(init_p, init_p + n);
	
	double ans = 0;
	int save_n = n;
	for (int a = 0; a <= k; a++)
	{
		int b = k - a;
		n = k;
		for (int i = 0; i < a; i++)
			p[i] = init_p[i];
		for (int i = 0; i < b; i++)
			p[a + i] = init_p[save_n - 1 - i];
		double cur_ans = solve();
		ans = max(ans, cur_ans);
	}


	printf("Case #%d: %.10lf\n", test, ans);
}

int main()
{
#ifdef LOCAL
	freopen ("input.txt", "r", stdin);
#endif

    int tests;
    scanf("%d", &tests);
    for (int test = 0; test < tests; test++)
    {
        dbg(test);
        solve(test + 1);
    }

	return 0;
}
