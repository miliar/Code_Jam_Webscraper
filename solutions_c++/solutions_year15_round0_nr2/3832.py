#include <iostream>
#include <cstdio>
#include <ctime>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <set>
#include <utility>
#include <fstream>
#include <cassert>

#define INF 999999999999999999LL
#define MOD 1000000007
#define MAX 201000
#define ALL 50
#define DEBUG false

using namespace std;

int n,t, x;
multiset<int> S;

int gcd(int a, int b)
{
	if (a == 0) {
		return b;
	}

	return gcd(b%a, a);
}

int dfs2(multiset<int> curSet)
{
	if (*curSet.rbegin() <= 2)
		return *curSet.rbegin();

	int curMax = *curSet.rbegin();

	curSet.erase(--curSet.end());
	curSet.insert(curMax/2);
	curSet.insert(curMax/2 + (curMax % 2));

	return min(dfs2(curSet) + 1, curMax);
}

int dfs(multiset<int> curSet)
{
	if (*curSet.rbegin() <= 2)
		return *curSet.rbegin();

	int curMax = *curSet.rbegin();

	int res = min(curMax, dfs2(curSet));

	curSet.erase(--curSet.end());

	int curGcd = -1;
	for (int i = 2; i*i <= curMax; ++i) {
		if (gcd(curMax, i) != 1) {
			curGcd = i;
		}
	}

	if (curGcd == -1) {
		curSet.insert(curMax/2);
		curSet.insert(curMax/2 + (curMax % 2));
	} else {
		curSet.insert(curMax/curGcd);
		curSet.insert(curMax - (curMax/curGcd));
	}

	return min(dfs(curSet) + 1, res);
}

int main()
{
	scanf("%d", &t);
	for (int test = 1; test <= t; ++test) {
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) {
			scanf("%d", &x);
			S.insert(x);
		}

		int res = min(dfs(S), dfs2(S));

		cout << "Case #" << test << ": " << res << endl;

		S.clear();
	}

	return 0;
}
