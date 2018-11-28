
//#include <bits/stdc++.h>
#include <stdlib.h>
#include<iomanip>
#include<iostream>
#include<algorithm>
#include<string>
#include<fstream>
#include<stdio.h>
#include<cstdio>
#include<map>
#include<vector>
#include<bitset>
using namespace std;
bool vis[10] = { 0 };
void clear()
{
	for (int i = 0; i < 10; i++)
		vis[i] = 0;
}
void check_digit(int n)
{
	while (n)
	{
		vis[n % 10] = 1;
		n /= 10;
	}
}
long long check(int x)
{
	for (int i = 1; i <= 1000; i++)
	{
		int tmp = i*x;
		check_digit(tmp);
		if (vis[0] && vis[1] && vis[2] && vis[3] && vis[4] && vis[5] && vis[6] && vis[7] && vis[8] && vis[9])return tmp;
	}
	return 0;
}
int main()
{
	freopen("myfile.txt ", "w", stdout);
	freopen("A-large.in", "r", stdin);

	int tc, x;
	cin >> tc;
	for (int i = 1; i <= tc; i++)
	{
		cin >> x;
		long long y = check(x);
		if (!y)cout << "Case #" << i << ": " << "INSOMNIA" << endl;
		else cout << "Case #" << i << ": " << y << endl;
		clear();
	}
	return 0;
}
