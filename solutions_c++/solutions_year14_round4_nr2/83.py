#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <ctime>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <string>
#include <sstream>
using namespace std;

#define FOR(i,a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); ++ i)

const int maxn = 1000;

void update(int &a, int b)
{
	if (a == -1 || a > b) {
		a = b;
	}
}

int f[maxn + 1][maxn + 1], a[maxn], bak[maxn];
int position[maxn], before[maxn + 1][maxn], after[maxn + 1][maxn];

int solve()
{
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; ++ i) {
		scanf("%d", &a[i]);
		bak[i] = a[i];
	}
	sort(bak, bak + n);
	for (int i = 0; i < n; ++ i) {
		a[i] = lower_bound(bak, bak + n, a[i]) - bak;
		position[a[i]] = i; 
	}
	
	for (int i = 0; i < n; ++ i) {
		before[0][i] = i;
		after[0][i] = n - 1 - i;
	}
	
	for (int i = 0; i < n; ++ i) {
		for (int j = 0; j < n; ++ j) {
			before[i + 1][j] = before[i][j] - (position[i] < j);
			after[i + 1][j] = after[i][j] - (position[i] > j);
		}
	}
	
	memset(f, -1, sizeof(f));
	f[0][0] = 0;
	
	for (int i = 0; i < n; ++ i) {
		for (int up = 0; up <= i; ++ up) {
			if (f[i][up] != -1) {
				//up
				update(f[i + 1][up + 1], f[i][up] + before[i][position[i]]);
				
				//down
				update(f[i + 1][up + 1], f[i][up] + after[i][position[i]]);
			}
		}
	}
	
	int answer = -1;
	for (int up = 0; up <= n; ++ up) {
		if (f[n][up] != -1) {
			update(answer, f[n][up]);
		}
	}
	return answer;
}

int main()
{
	int tests, test = 1;
	for (scanf("%d", &tests); test <= tests; ++ test) {
		printf("Case #%d: %d\n", test, solve());
	}
	return 0;
}
