#include <time.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include <map>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int memo[10][15], v[15], n, E, r;
bool mark[10][15];

int DP(int i, int e) {
	if(i >= n) return 0;
	int &best = memo[i][e];
	if(mark[i][e]) return best;
	mark[i][e] = true; best = 0;
	for(int j = e; j >= 0; --j) {
		best = max(best, DP(i + 1, min(e - j + r, E)) + j * v[i]);
	}
	return best;
}

int main()
{
	int T;
	scanf("%d",&T);
	for(int k = 0; k < T; ++k) {
		memset(mark, false, sizeof(mark));
		scanf("%d %d %d", &E, &r, &n);
		for(int i = 0; i < n; ++i)
			scanf("%d",&v[i]);
		printf("Case #%d: %d\n",k + 1, DP(0,E));
	}
	return 0;
}
