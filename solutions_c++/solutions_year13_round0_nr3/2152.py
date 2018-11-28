#ifndef CANT_USE_TEMPLATE
#define  _CRT_SECURE_NO_WARNINGS
#include <functional>
#include <algorithm>
#include <memory.h>
#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <bitset>
#include <string>
#include <cstdio>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <set>
#include <map>
using namespace std;

#define MP make_pair
#define ALL(v) v.begin(), v.end()
#define SZ(v) (int)v.size()
#define sqr(x) ((x)*(x))
#endif

#define  TASK ""

long long A, B;
long long ans;
vector < long long > v;

bool isPalindrom(long long x)
{
	string s;
	while (x > 0)
	{
		s += x % 10 + '0';
		x /= 10;
	}
	for (int i = 0; i < SZ(s) / 2; i++)
		if (s[i] != s[SZ(s) - 1 - i])
			return false;
	return true;
}

void solve(int x)
{
	int t = x, T = x;
	while (t > 0)
	{
		T = T * 10 + t % 10;
		t /= 10;
	}
	long long X = (long long)T * T;
	if (isPalindrom(X) && X >= A && X <= B)
		v.push_back(X);
	if (x > 99999)
	{
		return;
	}
	for (int i = 0; i < 10; i++)
		solve(x * 10 + i);
}

long long calc[13] = {
	121,
	1002001,
	10000200001,
	10221412201,
	1234321,
	12102420121,
	12345654321,
	1,
	484,
	4008004,
	40000800004,
	4,
	9
};

int main()
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	//freopen(TASK ".in", "r", stdin);
	//freopen(TASK ".out", "w", stdout);
#endif
	int t;
	cin >> t;
	/*A = 1;	B = 1e14;
	for (int i = 1; i < 10; i++)
	{
		solve(i);
		if (isPalindrom(i * i) && i * i >= A && i * i <= B)
			v.push_back(i * i);
	}*/
	for (int k = 0; k < t; k++)
	{
		cin >> A >> B;
		ans = 0;
		for (int i = 0; i < 13; i++)
			if (A <= calc[i] && calc[i] <= B)
				ans++;
		cout << "Case #" << k + 1 << ": " << ans << endl;
	}
	return 0;
}