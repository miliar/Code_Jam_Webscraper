#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
#include<set>
#include<memory.h>
#include<map>
#include<string>
#include<time.h>
using namespace std;

long long power(long long x, int y)
{
	if (!y) return 1;
	if (y % 2) return x*power(x, y - 1);
	else return power(x*x, y / 2);
}

long long f(long long i, long long k, long long c)
{
	return (i - 1)*power(k, c) + 1;
}

void solve()
{
	long long k, c, s;
	cin >> k >> c >> s;
	c--;
	for (int i = 1; i <= s; ++i) cout << " " << f(i, k, c);
	cout << "\n";
}

int main()
{
	ios::sync_with_stdio(0);
	//freopen("input.in", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int test = 1; test <= t; ++test)
	{
		//printf("Case #%d: ", test);
		cout << "Case #" << test << ":";
		solve();
	}
	return 0;
}