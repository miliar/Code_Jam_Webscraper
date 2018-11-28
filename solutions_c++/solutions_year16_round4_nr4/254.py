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

const int N = 5;

int n;
bool init_can[N][N];
bool can[N][N];
bool used_a[N], used_b[N];

bool bit(int mask, int pos)
{
	return (mask & (1 << pos)) != 0;
}

bool can_lock(int push_cnt)
{
	if (push_cnt == n)
		return false;

	for (int i = 0; i < n; i++)
	{
		if (used_a[i])
			continue;

		used_a[i] = true;
		
		bool can_lock_f = false;

		bool any_free = false;
		for (int j = 0; j < n; j++)
			if (!used_b[j] && can[i][j])
				any_free = true;

		if (!any_free)
			can_lock_f = true;

		for (int j = 0; j < n && !can_lock_f; j++)
		{
			if (used_b[j] || !can[i][j])
				continue;

			used_b[j] = true;
		
			if (can_lock(push_cnt + 1))
				can_lock_f = true;

			used_b[j] = false;
		}

		used_a[i] = false;

		if (can_lock_f)
			return true;
	}

	return false;
}

void solve(int test)
{
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		string s;
		cin >> s;
		for (int j = 0; j < n; j++)
			can[i][j] = init_can[i][j] = (s[j] == '1');
	}

	int ans = n * n;
	for (int mask = 0; mask < (1 << (n * n)); mask++)
	{
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				can[i][j] = (init_can[i][j] | bit(mask, i * n + j));
		int cur_ans = __builtin_popcount(mask);
		if (!can_lock(0))
			ans = min(ans, cur_ans);
	}

	printf("Case #%d: %d\n", test, ans);
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
