// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <cstdio>
#include <map>
#include <list>
#include <iostream>
#include <cstdlib>
#include <vector>

using namespace std;

int mp[1000];
char str[10005];
int l, x;

int rule[4][4] = {
	{ 0, 1, 2, 3 },
	{ 1, 0, 3, 2 },
	{ 2, 3, 0, 1 },
	{ 3, 2, 1, 0 }
};
int sign[4][4] = {
	{ +1, +1, +1, +1 },
	{ +1, -1, +1, -1 },
	{ +1, -1, -1, +1 },
	{ +1, +1, -1, -1 }
};

pair<int, int> mul(pair<int, int> a, pair<int, int> b)
{
	int sig = a.first * b.first * sign[a.second][b.second];
	int num = rule[a.second][b.second];
	return make_pair(sig, num);
}

bool ok()
{
	pair<int, int> sum = make_pair(1, mp['1']);
	for (int i = 0; i < l * x; i++)
	{
		pair<int, int> cur = make_pair(1, str[i % l]);
		sum = mul(sum, cur);
	}
	
	if (sum != make_pair(-1, mp['1']))
		return false;

	bool has = false;
	sum = make_pair(1, mp['1']);
	for (int i = 0; i < l * x; i++)
	{
		pair<int, int> cur = make_pair(1, str[i % l]);
		sum = mul(sum, cur);

		if (has && sum == make_pair(1, mp['k']))
			return true;
		has |= sum == make_pair(1, mp['i']);
	}
	return false;
}

int main()
{
	mp['1'] = 0;
	mp['i'] = 1;
	mp['j'] = 2;
	mp['k'] = 3;

	freopen("C-small-attempt1.in", "r", stdin);
	freopen("c-small.txt", "w", stdout);

	int t;
	scanf("%d", &t);
	for (int T = 1; T <= t; T++)
	{
		scanf("%d %d %s", &l, &x, str);

		for (int i = 0; i < l; i++)
			str[i] = mp[str[i]];

		printf("Case #%d: %s\n", T, ok() ? "YES" : "NO");

	}
}