#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector>
#include<set>
#include<memory.h>
using namespace std;

int f(long long x, int mask = 0,int deep=1)
{ 
	if (!x || x*deep > 100000000000000000ll) return -100000;
	long long y = x*deep;
	while (y) mask |= (1 << (y % 10)), y /= 10;
	if (mask == ((1 << 10) - 1)) return x*deep;
	return f(x, mask,deep+1);
}

int main()
{
	//freopen("input.in", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int test = 1; test <= t; ++test)
	{
		long long x;
		cin >> x;
		int d = f(x);
		
		cout << "Case #" << test << ": ";
		if (d < 0) cout << "INSOMNIA";
		else cout << d;
		cout << "\n";
	}
}