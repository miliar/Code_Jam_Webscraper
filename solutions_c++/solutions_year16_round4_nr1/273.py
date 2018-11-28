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

int get_winner(int p, int r, int s)
{
	while (p + r + s != 1)
	{
		if ((p + r - s) % 2 != 0)
			return -1;
		
		int a = (p + r - s) / 2;
		int b = r - a;
		int c = s - b;

		if (a < 0 || b < 0 || c < 0)
			return -1;

		if (a + c != p)
			return -1;

		if (a + b != r)
			return -1;

		if (b + c != s)
			return -1;

		p = a;
		r = b;
		s = c;
	}

	if (p == 1)
		return 0;
	if (r == 1)
		return 1;
	if (s == 1)
		return 2;

	assert(false);
}

string names = "PRS";

string get_ans(int n, int w)
{
	if (n == 0)
		return names.substr(w, 1);
	string s1 = get_ans(n - 1, w);
	string s2 = get_ans(n - 1, (w + 1) % 3);
	return min(s1 + s2, s2 + s1);
}

void solve(int test)
{
	int n, r, p, s;
	scanf("%d%d%d%d", &n, &r, &p, &s);
	int w = get_winner(p, r, s);

	if (w == -1)
	{
		printf("Case #%d: IMPOSSIBLE\n", test);
		return;
	}

	string ans = get_ans(n, w);
	printf("Case #%d: %s\n", test, ans.c_str());
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
