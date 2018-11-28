#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>

#define max(a, b) (((a) > (b)) ? (a) : (b))
#define min(a, b) (((a) > (b)) ? (b) : (a))
#define abs(a) (((a) > 0) ? (a) : (-(a)))

using namespace std;

const int MaxN = 100;

int a[MaxN][MaxN];
int n, m;

int tmp[MaxN][MaxN];

bool solve() {
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			tmp[i][j] = 100;
	for (int i = 0; i < n; i++) {
		int Max = 0;
		for (int j = 1; j < m; j++)
			if (a[i][j] > a[i][Max])
				Max = j;
		int x = a[i][Max];
		for (int j = 0; j < m; j++)
			if (tmp[i][j] > x)
				tmp[i][j] = x;
	}
	for (int j = 0; j < m; j++) {
		int Max = 0;
		for (int i = 1; i < n; i++)
			if (a[i][j] > a[Max][j])
				Max = i;
		int x = a[Max][j];
		for (int i = 0; i < n; i++)
			if (tmp[i][j] > x) 
				tmp[i][j] = x;
	}
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			if (a[i][j] != tmp[i][j]) return false;
	return true;
}

int main () {
	int test;
	scanf ("%d", &test);
	for (int t = 0; t < test; t++) {
		scanf ("%d%d", &n, &m);
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				scanf ("%d", &a[i][j]);
		bool can = solve();
		if (can)
			printf("Case #%d: YES\n", t+1);
		else
			printf("Case #%d: NO\n", t+1);
	}
}

