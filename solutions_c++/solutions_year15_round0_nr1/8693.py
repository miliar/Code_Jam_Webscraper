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

typedef long long i64;
const int INF = 0x3f3f3f3f;
const i64 INFLL = 0x3f3f3f3f3f3f3f3fLL;

int s;
char p[1010];

int main() {
	int t;
	scanf("%d", &t);
	for(int i = 0; i < t; ++i) {
		scanf("%d %s", &s, p);
		int cnt = 0, ans = 0; 
		for(int j = 0; j < s + 1; ++j) {
			if(cnt < j)
				ans += j - cnt, cnt += (j - cnt);
			cnt += (p[j] - 48);
		}
		printf("Case #%d: %d\n", i + 1, ans);
	}
	return 0;
}

