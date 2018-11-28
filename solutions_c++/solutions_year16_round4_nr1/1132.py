#pragma comment(linker, "/STACK:32000000")
#define _CRT_SECURE_NO_DEPRECATE

#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <stdarg.h>
#include <memory.h>
#include <string.h>

using namespace std;

const double pi = 3.1415926535897932384626433832795;
#define ALL(x) x.begin(), x.end()
#define LL long long
#define MP make_pair
#define PB push_back
#define CLR(a,b) memset(a, b, sizeof(a))
template<class T> inline T Sqr(const T &x) { return x*x; }
template<class T> inline T Abs(const T &x) { return x >= 0 ? x : -x; }
#define fo(i, n) for (int i = 0; i < (n); i++)
#define foz(i, a) for (int i = 0; i < (a).size(); i++)

string block[20][3];
char let[] = "PRS";
int ch[3][2] = { { 0, 1 }, { 1, 2 }, { 0, 2 } };

void init()
{
	for (int i = 0; i < 3; ++i)
		block[0][i] = let[i];
	for (int i = 1; i <= 12; ++i) {
		for (int j = 0; j < 3; ++j) {
			string& s1 = block[i - 1][ch[j][0]];
			string& s2 = block[i - 1][ch[j][1]];
			if (s1 < s2)
				block[i][j] = s1 + s2;
			else
				block[i][j] = s2 + s1;
		}
	}
}

typedef unsigned int uint;
//typedef long long numt;
//typedef __int128 numt;

bool check(string& w, int r, int p, int s) {
	for (int i = 0; i < w.size(); ++i) {
		switch (w[i]) {
		case 'R': --r; break;
		case 'P': --p; break;
		case 'S': --s; break;
		default:
			throw 42;
		}
	}
	if (r || p || s)
		return false;
	return true;
}

void solvecase()
{
	int n, r, p, s;
	cin >> n >> r >> p >> s;
	
	sort(let, let + 3);

	string best;
	for (int i = 0; i < 3; ++i)
		if (check(block[n][i], r, p, s))
			if (block[n][i] < best || best.empty())
				best = block[n][i];
	if (best.empty())	
		printf("IMPOSSIBLE");
	else {
			cout << best;
	}
}

void solve() {
	init();
	int n_tests;
	scanf("%d", &n_tests);
	for (int i = 1; i <= n_tests; i++)
	{
		printf("Case #%d: ", i);
		solvecase();
		printf("\n");
	}
}

#define dir "C:/Users/dmarin3/Downloads/"
#define problem_letter "A"
//#define fname "test"
//#define fname dir problem_letter "-small-attempt0"
//#define fname dir problem_letter "-small-attempt1"
//#define fname dir problem_letter "-small-attempt2"
#define fname dir problem_letter "-large"

int main()
{
	freopen(fname ".in", "r", stdin);
	freopen(fname ".out", "w", stdout);
	solve();
	return 0;
}
