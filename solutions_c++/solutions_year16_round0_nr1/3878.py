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

int n;

void input() {
	scanf("%d", &n);
}

void solve() {
	if(n == 0) {
		printf("INSOMNIA\n");
		return ;
	}

	char vis[10];
	memset(vis, 0, sizeof(char)*10);
	int cnt = 0;

	int i = 1;
	while(cnt < 10) {
		int tmp = i*n;
		if(tmp > 100000000) printf("WA\n");
		while(tmp) {
			if(!vis[tmp%10]) {
				vis[tmp%10] = 1;
				++ cnt;
			}
			tmp /= 10;
		}
		if(cnt == 10) {
			printf("%d\n", i*n);
			return ;
		}
		++ i;
	}
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
