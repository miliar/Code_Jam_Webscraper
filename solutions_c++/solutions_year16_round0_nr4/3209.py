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

int k, c, s;

void input() {
	scanf("%d%d%d", &k, &c, &s);
}

void solve() {
	long long multi = 1;
	for(int i = 1;i < c;i ++) multi *= k;

	long long res = 0;
	for(int i = 0;i < k;i ++) {
		printf(" %lld", res+1);
		res += multi;
	}
	printf("\n");
}

int main() {
	int t;
	scanf("%d", &t);
	for(int cas = 0; cas < t;cas ++) {
		input();
		printf("Case #%d:", cas+1);
		solve();
	}
	return 0;
}
