

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
#include "stdio.h"
using namespace std;

char s[6000];

vector<string> v;
vector<int> getarr(string &s1, string &s2)
{
	int i = 0;

	int n = s1.length();
	s2 = "";
	int res = 0;
	vector<int> rr;
	while (i<n)
	{
		int oldi = i;
		while (i < n && s1[i] == s1[i + 1])
			i++;
		s2 += s1[oldi];
		res = i - oldi + 1;
		rr.push_back(res);
		i++;
	}

	return rr;
}

int diff(string &s1, string &s2)
{
	int res = 0;
	int j = 0;
	int i = 0;
	
	int n = s1.length();
	int m = s2.length();
	while (1)
	{
		int oldi = i;
		int oldj = j;
		while (i < n && s1[i] == s1[i + 1])
			i++;
		while (j < m && s2[j] == s2[j + 1])
			j++;

		int ci = i - oldi + 1;
		int cj = j - oldj + 1;

		if (s1[oldi] == s2[oldj])
		{
			res += abs(ci - cj);
		}
		else
			return 1000000;

		if (i == n - 1 && j == m - 1)
			return res;
		else if (i == n - 1 || j == m - 1)
			return 1000000;
		i++;
		j++;
	}
}

vector<int> vvv[200];

void solve_case(int test_case)
{
	int n;
	cin >> n;
	v.clear();
	for (int i = 0; i < n; ++i)
	{
		s[0] = '\0';
		scanf("%s", &s[0]);
		int m = strlen(s);
		string ss = "";
		for (int j = 0; j < m; ++j)
			ss += s[j];
		v.push_back(ss);
	}
	cout << "Case #" << test_case << ": ";

	int res = 0;
	string sres = "";
	for (int i = 0; i < n; ++i)
	{
		string ss;
		vector<int> vn = getarr(v[i], ss);
		vvv[i] = vn;
		if (sres == "")
			sres = ss;
		else
		if (sres != ss)
		{
			cout << "Fegla Won";
			cout << endl;
			return;
		}
	}
	int nn = vvv[0].size();
	for (int i = 0; i < nn; ++i)
	{
		int sum = 0;
		for (int j = 0; j < n; ++j)
			sum += vvv[j][i];

		int ans1 = (int)floor(sum * 1.0/ n + 0.5);
		int ans = 0;
		for (int j = 0; j < n; ++j)
			ans += abs(vvv[j][i] - ans1);

		res += ans;
	}

	cout << res << endl;

}

int main()
{

#ifdef __OLIMP__
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int T;
	scanf("%d", &T);

	for (int tc = 1; tc <= T; tc++)
		solve_case(tc);

	return 0;
}