#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <ctime>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <cassert>
#include <bitset>

using namespace std;

int a[8][8] = {{0, 1, 2, 3, 4, 5, 6, 7},
			   {1, 4, 3, 6, 5, 0, 7, 2},
			   {2, 7, 4, 1, 6, 3, 0, 5},
			   {3, 2, 5, 4, 7, 6, 1, 0},
			   {4, 5, 6, 7, 0, 1, 2, 3},
			   {5, 0, 7, 2, 1, 4, 3, 6},
			   {6, 3, 0, 5, 2, 7, 4, 1},
			   {7, 6, 1, 0, 3, 2, 5, 4}};
			   
char st[10005];

int main() {
	int cases;
	scanf("%d", &cases);
	for (int o = 0; o < cases; ++o) {
		int n, m;
		bool ans = 0;
		scanf("%d %d", &n, &m);
		scanf("%s", st);
		//m %= 12;
		//if (!m) m = 12;
		int x = 0, y = m * n, z = m * n;
		for (int i = 0; i < m * n; ++i) {
			x = a[x][st[i % n] - 'h'];
			if (x == 1) {
				y = i;
				break;
			}
		}
		if (y < m * n) {
			x = 0;
			for (int i = y + 1; i < m * n; ++i) {
				x = a[x][st[i % n] - 'h'];
				if (x == 2) {
					z = i;
					break;
				}
			}
			if (z < m * n) {
				x = 0;
				for (int i = z + 1; i < m * n; ++i) {
					x = a[x][st[i % n] - 'h'];
				}
				if (x == 3) {
					ans = 1;
				}
			}
		}
		if (ans) {
			printf("Case #%d: YES\n", o + 1);
		} else {
			printf("Case #%d: NO\n", o + 1);
		}
	}
	return 0;
}