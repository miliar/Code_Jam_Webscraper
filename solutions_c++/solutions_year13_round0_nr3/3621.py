#include <cstdio>
#include <cmath>
#include <cctype>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <memory.h>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <functional>
#include <ctime>

#define FOR(i, n) for (int i = 0; i < n; i++)

#pragma comment(linker, "/STACK:250777216")

using namespace std;

typedef long long LL;
typedef vector<int> vint;
typedef vector<vint> vvint;
const int MOD = int(1e9) + 7;
const int HMOD = (1 << 22) - 1;
const int BASE = int(1e9);

int t, a, b;
int answ = 0;

bool Check(string s)
{
	for (int i = 0; i < s.length()/2; i++)
		if (s[i] != s[s.length() - i - 1])
			return false;
	return true;
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d", &t);
	string s;
	for (int i = 0; i < t; i++)
	{
		answ = 0;
		scanf("%d%d", &a, &b);
		int sq1 = floor(sqrt( (double) a)), sq2 = floor(sqrt( (double) b + 0.5));
		if (sq1*sq1 < a)
			sq1++;
		if (sq2*sq2 > b)
			sq2--;
		for (int i = sq1; i <= sq2; i++)
		{
			s.clear();
			int cur = i;
			while (cur)
			{
				s.push_back(cur % 10);
				cur /= 10;
			}
			if (!Check(s))
				continue;
			cur = i*i;
			s.clear();
			while (cur)
			{
				s.push_back(cur % 10);
				cur /= 10;
			}
			if (Check(s))
				answ++;
		}
		printf("Case #%d: %d\n", i + 1, answ);
	}
	return 0;
}