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

void solve(int test)
{
	int64 k, c, s;
	scanf("%lld%lld%lld", &k, &c, &s);
	if (s < k)
	{
		printf("Case #%d: IMPOSSIBLE\n", test);
		return;
	}

	int64 ptr = 1;
	
	int64 sh = 1;
	for (int i = 0; i < c - 1; i++)
		sh *= k;

	printf("Case #%d:", test);
	for (int i = 0; i < k; i++)
	{
		printf(" %lld", ptr);
		ptr += sh;
	}
	printf("\n");
}

int main()
{
#ifdef LOCAL
	freopen ("input.txt", "r", stdin);
#endif

	int tests;
	scanf("%d", &tests);
	for (int i = 0; i < tests; i++)
		solve(i + 1);

	return 0;
}
