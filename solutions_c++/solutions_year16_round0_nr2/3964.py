/*
 * main.cpp
 *
 *  Created on: 9 Apr 2016
 *      Author: ljchang
 */




#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

char s[128];

void input() {
	scanf("%s", s);
}

void solve() {
	int n = strlen(s);
	s[n] = '+';
	int res = 0;
	for(int i = 0;i < n;i ++) if(s[i] != s[i+1]) ++ res;
	printf("%d\n", res);
}

int main() {
	int t;
	scanf("%d", &t);
	for(int cas = 0; cas < t;cas ++) {
		input();
		printf("Case #%d: ", cas+1);
		solve();
	}
	return 0;
}
