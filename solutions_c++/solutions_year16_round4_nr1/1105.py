#include <stdio.h>
#include <cassert>
#include <cstring>
#include <map>
#include <set>
#include <time.h>
#include <algorithm>
#include <stack>
#include <queue>
#include <utility>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <limits>

using namespace std;

typedef pair <int, int> ii;
typedef pair <long long, long long> ll;

int re[135][4];
int key[135][4];
int tm[135][4];

int win(int x, int y) {
	if (x > y) swap(x, y);
	if (x == 0 && y == 1)
		return 1;
	else if (x == 0 && y == 2)
		return 0;
	else if (x == 1 && y == 2)
		return 2;
}

bool ok = 1;

void go(int n, int r, int p, int s, int dep) {
	ii q[3] = { ii( r, 0 ), ii( p, 1), ii( s, 2) };
	sort(q, q + 3);
	int t[3];
	t[0] = q[0].first;
	t[1] = q[1].first;
	t[2] = q[2].first;
	if (t[1] + t[0] < t[2]) ok = 0;
	int m = t[1] - t[0];
	if (t[2] < m) ok = 0;
	t[2] -= m;
	t[1] -= m;
	if (t[2] % 2 != 0) ok = 0;
	t[1] -= t[2] / 2;
	t[0] -= t[2] / 2;

	int t12 = (t[2] / 2 + m);
	int t01 = t[1];
	int t02 = t[2] / 2 ;
	int k[3] = { 0, };
	k[win(q[1].second, q[2].second)] += t12;
	k[win(q[0].second, q[1].second)] += t01;
	k[win(q[0].second, q[2].second)] += t02;

	for (int i = 0; i < 3; i++)
		re[dep][i] = k[i];
	if (ok) {
		if (dep == 1) {
			key[dep][0] = 1;
			key[dep][1] = 0;
			key[dep][2] = 2;
			tm[dep][0] = 1;
			tm[dep][1] = 0;
			tm[dep][2] = 2;

		}
		else {
			tm[dep][0] = win(tm[dep - 1][0], tm[dep - 1][1]);
			tm[dep][1] = win(tm[dep - 1][0], tm[dep - 1][2]);
			tm[dep][2] = win(tm[dep - 1][1], tm[dep - 1][2]);

			for(int i=0; i<3; i++)
				key[dep][tm[dep][i]] = i;
			
		}
		if(k[0] + k[1] + k[2] > 1)
			go(n, k[0], k[1], k[2], dep + 1);
	}
}

void print(int dep, int c) {
	if (dep == 1) {
		if (c == 0) printf("R");
		if (c == 1) printf("P");
		if (c == 2) printf("S");
	}
	else {
		if (c == 0) {
			if (key[dep-1][0] < key[dep-1][2]) {
				print(dep - 1, 0);
				print(dep - 1, 2);
			}
			else {
				print(dep - 1, 2);
				print(dep - 1, 0);
			}
		}
		else if (c == 1) {
			if (key[dep - 1][1] < key[dep - 1][0]) {
				print(dep - 1, 1);
				print(dep - 1, 0);
			}
			else {
				print(dep - 1, 0);
				print(dep - 1, 1);
			}

		}
		else {
			if (key[dep - 1][1] < key[dep - 1][2]) {
				print(dep - 1, 1);
				print(dep - 1, 2);
			}
			else {
				print(dep - 1, 2);
				print(dep - 1, 1);
			}
		}
	}
}


void solve() {
	int n, r, p, s;
	scanf("%d %d %d %d", &n, &r, &p, &s);
	ok = 1;
	go(n, r, p, s, 1);
	if (ok) {
		/*
		for (int i = 1; i <= n; i++)
			printf("round %d : %d %d %d\n", i, re[i][0], re[i][1], re[i][2]);
		for (int i = 1; i <= n; i++)
			printf("key %d : %d %d %d\n", i, key[i][0], key[i][1], key[i][2]);
			*/
		int lst = 0;
		for (int k = 0; k < 3; k++)
			if (re[n][k])
				lst = k;
		print(n+1, lst);
		puts("");
	}
	else
		puts("IMPOSSIBLE");

}

int main() {

//	freopen("in.txt", "r", stdin);
//	freopen("out.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int R = 1; R <= T; R++) {
		printf("Case #%d: ", R);
		solve();

	}

}