#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <cstring>
#include <cassert>
#include <utility>
#include <iomanip>

using namespace std;

const int MAXN = 105;

const int di[] = {-1, 1, 0, 0};
const int dj[] = {0, 0, 1, -1};
const char a[] = {'^', 'v', '>', '<'};

int tn;
int n, m;
char c[MAXN][MAXN];
bool bad = false;
int ans;

int main() {
	//assert(freopen("input.txt","r",stdin));
	//assert(freopen("output.txt","w",stdout));

	scanf("%d\n", &tn);

	for (int test = 1; test <= tn; test++) {
		
		scanf("%d %d\n", &n, &m);
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= m; j++) {
				scanf("%c", &c[i][j]);
			}
			scanf("\n");
		}

		ans = 0;
		bad = false;

		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= m; j++) {
				if (c[i][j] == '.')
					continue;
				
				bool any = false;
				for (int k = 0; k < 4; k++) {
					int ci = i, cj = j;
					while (true) {
						ci += di[k], cj += dj[k];
						if (ci < 1 || ci > n || cj < 1 || cj > m)
							break;
						if (c[ci][cj] != '.') {
							any = true;
							break;
						} 
					}
				}

				if (!any)
					bad = true;

				bool change = true;
				for (int k = 0; k < 4; k++) {
					if (a[k] != c[i][j])
						continue;
					int ci = i, cj = j;
					while (true) {
						ci += di[k], cj += dj[k];
						if (ci < 1 || ci > n || cj < 1 || cj > m)
							break;
						if (c[ci][cj] != '.') {
							change = false;
							break;
						} 
					}
				}

				if (change)
					ans++;
			}
		}

		if (bad)
			printf("Case #%d: IMPOSSIBLE\n", test);
		else	
			printf("Case #%d: %d\n", test, ans);
	}

	return 0;
}