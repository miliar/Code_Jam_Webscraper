#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <complex>
#include <vector>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <string.h>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>

using namespace std;

typedef long long LL;
const int maxn = 9;
char mp[maxn][maxn];
int row (int x) {
	char tmp = 0;
	for (int i = 0; i < 4; ++ i) {
		if (mp[x][i] == '.') return 0;
		if (mp[x][i] != 'T') {
			tmp = mp[x][i];
			break;
		}
	}
	for (int i = 0; i < 4; ++ i) {
		if (mp[x][i] != 'T' && mp[x][i] != tmp) return 0;
	}
	return 1;
}
int col (int x) {
	char tmp = 0;
	for (int i = 0; i < 4; ++ i) {
		if (mp[i][x] == '.') return 0;
		if (mp[i][x] != 'T') {
			tmp = mp[i][x];
			break;
		}
	}
	for (int i = 0; i < 4; ++ i) {
		if (mp[i][x] != 'T' && mp[i][x] != tmp) return 0;
	}
	return 1;
}
int fun () {
	char tmp = 0;
	for (int i = 0; i < 4; ++ i) {
		if (mp[i][i] == '.') return 0;
		if (mp[i][i] != 'T') {
			tmp = mp[i][i];
			break;
		}
	}
	for (int i = 0; i < 4; ++ i) {
		if (mp[i][i] != 'T' && mp[i][i] != tmp) return 0;
	}
	return 1;
}
int ok () {
	char tmp = 0;
	for (int i = 0; i < 4; ++ i) {
		if (mp[i][3-i] == '.') return 0;
		if (mp[i][3-i] != 'T') {
			tmp = mp[i][3-i];
			break;
		}
	}
	for (int i = 0; i < 4; ++ i) {
		if (mp[i][3-i] != 'T' && mp[i][3-i] != tmp) return 0;
	}
	return 1;
}
int main () {
	freopen ("in", "r", stdin);
	freopen ("out", "w", stdout);
	int t;
	scanf ("%d", &t);
	for (int cas = 1; cas <= t; ++ cas) {
		for (int i = 0; i < 4; ++ i)
			scanf ("%s", mp[i]);
		char flag = 0;
		for (int i = 0; i < 4; ++ i) {
			if (flag) break;
			if (row(i)) {
				if (mp[i][0] != 'T') flag = mp[i][0];
				else flag = mp[i][1];
			}
			if (col (i)) {
				if (mp[0][i] != 'T') flag = mp[0][i];
				else flag = mp[1][i];
			}
		}
		if (fun ()) {
			if (mp[0][0] != 'T') flag = mp[0][0];
			else flag = mp[1][1];
		}
		if (ok ()) {
			if (mp[0][3] != 'T') flag = mp[0][3];
			else flag = mp[1][2];
		}
		printf ("Case #%d: ", cas);
		if (flag) printf ("%c won\n", flag);
		else {
			int cnt = 0;
			for (int i = 0; i < 4; ++ i)
				for (int j = 0; j < 4; ++ j)
					cnt += (mp[i][j] == '.');
			if (cnt == 0) puts ("Draw");
			else puts ("Game has not completed");
		}
	}
	return 0;
}