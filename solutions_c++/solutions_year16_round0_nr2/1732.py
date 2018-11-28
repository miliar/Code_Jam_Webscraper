#include <iostream>
#include <fstream>
#include <cstdio>
#include <climits>
#include <vector>
#include <map>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <string>
#include <cstring>
#include <algorithm>
#include <bitset>
#include <cmath>
#include <functional>

using namespace std;

#define ll long long
#define vt vector
#define mod 1000000007

bool allSame(string& p)
{
	char x = p[0];
	for (int i = 1; i < p.length(); i++)
		if (x != p[i])
			return false;
	return true;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int cases = 1; cases <= t; cases++)
	{
		string p;
		cin >> p;
		int ans = 0;
		while (!allSame(p))
		{
			char x = p[0];
			int flipTill = 0;
			for (int i = 1; i < p.length(); i++)
				if (x != p[i])
				{
					flipTill = i;
					break;
				}
			for (int i = 0; i < flipTill; i++)
				if (x == '+')
					p[i] = '-';
				else
					p[i] = '+';
			ans++;
		}
		if (p[0] == '-')
			ans++;
		printf("Case #%d: %d\n", cases, ans);
	}
	return 0;
}