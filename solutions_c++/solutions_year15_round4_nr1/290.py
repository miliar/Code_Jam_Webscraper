/*
 * Problem : 
 * Author : Hwhitetooth
 * Date : 
 * Result :
 */

#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cctype>
#include <cstring>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;

const int N = 100 + 10;
const int D[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

int a[N][N];
int testCases, n, m;
int ans;

int main() {
	scanf("%d", &testCases);
	for (int _ = 1; _ <= testCases; ++_) {
		ans = 0;
		printf("Case #%d: ", _);
		scanf("%d%d", &n, &m);
		for (int i = 0; i < n; ++i) {
			static char buf[N];
			scanf("%s", buf);
			for (int j = 0; j < m; ++j) {
				switch (buf[j]) {
					case '.':
						a[i][j] = 4;
						break;
					case '^':
						a[i][j] = 0;
						break;
					case 'v':
						a[i][j] = 1;
						break;
					case '<':
						a[i][j] = 2;
						break;
					case '>':
						a[i][j] = 3;
						break;
				}
			}
		}
		int flag = 1;
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				if (a[i][j] == 4) {
					continue;
				}
				flag = 0;
				for (int k = 0; k < 4; ++k) {
					for (int x = i + D[k][0], y = j + D[k][1]; x >= 0 && x < n && y >= 0 && y < m; x += D[k][0], y += D[k][1]) {
						if (a[x][y] < 4) {
							flag = 1;
							break;
						}
					}
					if (flag) {
						break;
					}
				}
				if (! flag) {
					break;
				}
			}
			if (! flag) {
				break;
			}
		}
		if (! flag) {
			printf("IMPOSSIBLE\n");
			continue;
		}
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				if (a[i][j] == 4) {
					continue;
				}
				int flag = 0;
				for (int x = i + D[a[i][j]][0], y = j + D[a[i][j]][1]; x >= 0 && x < n && y >= 0 && y < m; x += D[a[i][j]][0], y += D[a[i][j]][1]) {
					if (a[x][y] < 4) {
						flag = 1;
						break;
					}
				}
				if (! flag) {
					++ans;
				}
			}
		}
		printf("%d\n", ans);
	}
	return 0;
}