#include <iostream>
#include <fstream>
#include <cstdio>
#include <iomanip>
#include <cassert>
#include <climits>
#include <cmath>
#include <vector>
#include <string>
#include <cstring>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <algorithm>
using namespace std;

typedef pair<int, int> pii;
#define mp make_pair
#define sqr(x) ((x)*(x))
const double PI = 3.1415926535;

int t, n, m, pow10[10], cnt;
char s[33];
long long ans[50], l, r;

bool is_pal(long long n)
{
	sprintf(s, "%I64d", n);
	int len = strlen(s);
	for (int i = 0, j = len-1; i < j; ++i, --j)
		if (s[i] != s[j])
			return false;
	return true;
}

int main()
{
#ifdef MYLOCAL
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif
	
	pow10[0] = 1;
	for (int i = 1; i < 10; ++i)
		pow10[i] = pow10[i-1] * 10;
	for (int i = 1; i < 30000000; ++i)
	{
		for (int j = 1; j < 7; ++j)
			if (i % pow10[j] > 3 * pow10[j-1])
				i += pow10[j] - i % pow10[j];
		if (is_pal(i) && is_pal((long long)i*i))
			ans[cnt++] = (long long)i*i;
	}

	cin >> t;
	for (int ii = 0; ii < t; ++ii)
	{
		cout << "Case #" << ii+1 << ": ";
		cin >> l >> r;
		int res = 0;
		for (int i = 0; i < cnt; ++i)
			if (ans[i] >= l && ans[i] <= r)
				++res;
		cout << res << '\n';
	}

	return 0;
}