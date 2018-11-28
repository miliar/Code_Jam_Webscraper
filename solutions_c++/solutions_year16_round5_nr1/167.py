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

const int N = 100;

int n;
string t;
int dp[N][N][2];

int get_score(char a, char b)
{
	if (a == b)
		return 10;
	return 5;
}

int get_dp(int l, int r, int c)
{
	if (0 <= l && l < n && 0 <= r && r < n && l <= r)
		return dp[l][r][c];
	return 0;
}

void relax_max(int &a, int b)
{
	a = max(a, b);
}

void solve(int test)
{
	cin >> t;
	vector<char> stack;
	int ans = 0;
	for (char c : t)
	{
		if (!stack.empty() && stack.back() == c)
		{
			stack.pop_back();
			ans += 10;
		}
		else
			stack.push_back(c);
	}
	ans += (int)stack.size() / 2 * 5;

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
