#pragma comment(linker, "/STACK:500000000") 
#include <functional>
#include <algorithm> 
#include <iostream> 
#include <string.h> 
#include <stdlib.h> 
#include <sstream> 
#include <fstream>
#include <ctype.h> 
#include <stdio.h> 
#include <bitset>
#include <vector> 
#include <string> 
#include <math.h> 
#include <time.h> 
#include <queue> 
#include <stack> 
#include <list>
#include <map> 
#include <set> 
#define Int long long 
#define INF 0x3F3F3F3F 
#define eps 1e-9
using namespace std;

int n, m;
string s[111];
Int Hash[111][111];
int mask[111];
int res, cnt;

void add(set<Int> &s, int idx)
{
	for (int i = 0; i < ::s[idx].size(); i++)
		s.insert(Hash[idx][i]);
}

void rec(int pos)
{
	if (pos == m)
	{
		set<Int> S[4];
		for (int i = 0; i < m; i++)
		{
			add(S[mask[i]], i);
		}
		int sum = 0;
		for (int i = 0; i < n; i++)
		{
			sum += S[i].size();
			if (S[i].size())
				sum++;
		}
		if (sum > res)
		{
			res = sum;
			cnt = 1;
		}
		else if (sum == res)
			cnt++;
		return;
	}
	for (int i = 0; i < n; i++)
	{
		mask[pos] = i;
		rec(pos + 1);
	}
}

int main()
{
	int tests, i;
	scanf("%d", &tests);
	for (int test = 1; test <= tests; test++)
	{
		scanf("%d %d", &m, &n);
		for (i = 0; i < m; i++)
		{
			cin >> s[i];
			Hash[i][0] = s[i][0] - 'A' + 1;
			Int p = 31;
			for (int j = 1; j < s[i].size(); j++, p *= 31)
				Hash[i][j] = Hash[i][j - 1] + (s[i][j] - 'A' + 1) * p;
		}
		res = cnt = 0;
		rec(0);
		printf("Case #%d: %d %d\n", test, res, cnt);
	}
}