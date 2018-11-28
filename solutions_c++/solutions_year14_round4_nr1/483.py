/*
 * $File: a.cpp
 * $Date: Sat May 31 22:07:52 2014 +0800
 * $Author: Xinyu Zhou <zxytim@gmail.com>
 */

#include <cstdio>
#include <cassert>
#include <cmath>
#include <cstdlib>
#include <ctype.h>
#include <cstring>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>

using namespace std;

typedef long long int ll;
typedef unsigned long long int ull;

template<typename T> void updatemax(T &a, T b) { if (b > a) a = b; }
template<typename T> void updatemin(T &a, T b) { if (b < a) a = b; }

void solve(int case_id);

int main()
{
	int ncase;
	scanf("%d", &ncase);
	for (int id = 1; id <= ncase; id ++)
	{
		printf("Case #%d: ", id);
		solve(id);
	}
	return 0;
}

void solve(int case_id)
{
	int N, X;
	cin >> N >> X;
	vector<int> a(N);
	for (int i = 0; i < N; i ++)
		cin >> a[i];

	sort(a.begin(), a.end());
	int l = 0, r = (int)a.size() - 1;
	int ans = 0;
	while (l < r) {
		if (a[l] + a[r] <= X)
			ans ++, l ++, r --;
		else if (a[l] > a[r])
			ans ++, l ++;
		else ans ++, r --;
	}
	if (l == r)
		ans ++;
	printf("%d\n", ans);
}

