//============================================================================
// Name        : cj_C.cpp
// Author      : huangxs139
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
using namespace std;

int a, b;
int cnta, cntb;
int ans;

int main() {
	int t;
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("data.out", "w", stdout);
	scanf("%d", &t);
	for (int cas = 1; cas <= t; cas++) {
		scanf("%d %d", &a, &b);
		ans = 0;
		cnta = cntb = 0;
		if (a > 1)	cnta++;
		if (a > 4) cnta++;
		if (a > 9) cnta++;
		if (a > 121) cnta++;
		if (a > 484) cnta++;
		if (b >= 1)	cntb++;
		if (b >= 4) cntb++;
		if (b >= 9) cntb++;
		if (b >= 121) cntb++;
		if (b >= 484) cntb++;
		ans = cntb - cnta;
		printf("Case #%d: %d\n", cas, ans);
	}
	return 0;
}
