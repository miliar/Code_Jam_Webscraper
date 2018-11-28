//============================================================================
// Name        : 2016_gcj_b.cpp
// Author      : 
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

#define RUN

char s[110];

int main() {

#ifdef RUN
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
#endif

	int t;
	int ans;
	scanf("%d", &t);
	for (int cas = 1; cas <= t; cas++) {
		printf("Case #%d: ", cas);
		scanf("%s", s);
		ans = 0;
		for (int i = 1; s[i]; i++)
			if (s[i] != s[i-1])
				ans += 1;
		if (s[strlen(s)-1] == '-')
			ans += 1;
		printf("%d\n", ans);
	}
	return 0;
}
