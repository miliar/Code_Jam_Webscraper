/*
 * $File: b2.cpp
 * $Date: Sat May 31 22:47:21 2014 +0800
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

int cmp(int a, int b) {
	return b > a ? 1 : -1;
}

bool check_order(std::vector<int> &a, int l, int r, int ord) { // 1 for ascending, -1 for descending
	for (int i = l; i < r; i ++)
		if (cmp(a[i], a[i + 1]) != ord)
			return false;
	return true;
}


bool check(std::vector<int> &a) {
	int ind = -1, val = std::numeric_limits<int>::lowest();
	int n = a.size();
	for (int i = 0; i < n; i ++)
		if (a[i] > val)
			ind = i, val = a[i];
	if (!check_order(a, 0, ind, 1))
		return false;
	if (!check_order(a, ind, n - 1, -1))
		return false;
	return true;
}

void solve(int case_id)
{
	fprintf(stderr, "%d\n", case_id);
	int N;
	cin >> N;
	vector<int> a(N);
	for (int i = 0; i < N; i ++)
		cin >> a[i];

	int n = N;
	int ans = 0;
	int l = 0, r = N - 1;
	while (!check(a)) {
		int ind = -1, val = std::numeric_limits<int>::max();
		for (int i = l; i <= r; i ++)
			if (a[i] < val)
				val = a[i], ind = i;
		if (ind == l)
			l ++;
		else if (ind == r)
			r --;
		else {
			if (ind - l <= r - ind) {
				for (int i = ind; i > l; i --) {
					swap(a[i], a[i - 1]);
					ans ++;
				}
				l ++;
			} else {
				for (int i = ind; i < r; i ++) {
					swap(a[i], a[i + 1]);
					ans ++;
				}
				r --;
			}
		}
	}
	printf("%d\n", ans);
}

