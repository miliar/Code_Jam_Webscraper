/*
 * main.cpp
 *
 *  Created on: 9 Apr 2016
 *      Author: ljchang
 */

#include <cstdio>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

int N, R, P, S;
char res[14][5000];

void input() {
	scanf("%d%d%d%d", &N, &R, &P, &S);
}

void search(int N, int R, int P, int S) {
	char *str = res[N];
	res[N][1<<N] = '\0';
	if(N == 1) {
		if(R == 1&&P == 1) {
			str[0] = 'P';
			str[1] = 'R';
		}
		else if(R == 1&&S == 1) {
			str[0] = 'R';
			str[1] = 'S';
		}
		else if(P == 1&&S == 1) {
			str[0] = 'P';
			str[1] = 'S';
		}
		else strcpy(str, "IMPOSSIBLE");
		//printf("%s\n", str);
		return ;
	}

	if(P+R < S||(P+R-S)%2 != 0||P+S < R||(P+S-R)%2 != 0||R+S < P||(R+S-P)%2 != 0) {
		strcpy(str, "IMPOSSIBLE");
		return ;
	}

	int x = (P+R-S)/2, y = (P+S-R)/2, z = (R+S-P)/2;
	P = x; S= y; R = z;
	//printf("%d %d %d\n", R, P, S);
	search(N-1, R, P, S);
	if(strcmp(res[N-1], "IMPOSSIBLE") == 0) {
		strcpy(res[N], "IMPOSSIBLE");
		return ;
	}

	res[N][1<<N] = '\0';
	for(int i = 0;i < 1<<(N-1);i ++) {
		if(res[N-1][i] == 'P') {
			res[N][2*i] = 'P';
			res[N][2*i+1] = 'R';
		}
		else if(res[N-1][i] == 'S') {
			res[N][2*i] = 'P';
			res[N][2*i+1] = 'S';
		}
		else if(res[N-1][i] == 'R') {
			res[N][2*i] = 'R';
			res[N][2*i+1] = 'S';
		}
	}
	//printf("%s\n", res[N]);
}

void search2(char *str, int len) {
	if(len == 1) {
		if(str[0] > str[1]) swap(str[0], str[1]);
		return ;
	}
	search2(str, len/2);
	search2(str+len, len/2);
	char tmp[5000];
	strcpy(tmp, str);
	tmp[len] = '\0';
	if(strcmp(tmp, str+len) > 0) {
		for(int i = 0;i < len;i ++) {
			swap(str[i], str[i+len]);
		}
		//strcpy(str+len, tmp);
	}
}

void solve() {
	search(N, R, P, S);
	//printf("%s\n", res[N]);
	char *ans = res[N];
	if(strcmp(res[N], "IMPOSSIBLE") != 0) {
		search2(ans, 1<<(N-1));
	}
	printf(" %s\n", ans);
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
