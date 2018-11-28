#include <map>
#include <set>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cctype>
#include <cstdio>
#include <vector>
#include <cassert>
#include <complex>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
#define int long long

const string ip = "IMPOSSIBLE";

string go(int n, int p, int r, int s)
{
	if (n == 1)
	{
		if (p == 2 or r == 2 or s == 2)
			return ip;
		if (p == 0) return "RS";
		if (r == 0) return "PS";
		if (s == 0) return "PR";
		assert(0);
	}
	int a = p + r - s;
	int b = p + s - r;
	int c = s + r - p;
	if (a % 2 or b % 2 or c % 2) return ip;
	if (a < 0 or b < 0 or c < 0) return ip;
	string buf = go(n - 1, a / 2, b / 2, c / 2);
	if (buf == ip) return ip;
	string ret = "";
	for (char c : buf)
	{
		if (c == 'P') ret += "PR";
		if (c == 'R') ret += "PS";
		if (c == 'S') ret += "RS";
	}
	return ret;
}

#undef int
int main()
{
#define int long long
	int t; cin >> t;
	for (int tt = 1; tt <= t; tt++)
	{
		cerr << "Executing Case #" << tt << "\n";
		int n, p, r, s;
		cin >> n >> r >> p >> s;
		cout << "Case #" << tt << ": " << go(n, p, r, s) << "\n";
	}
	return 0;
}
