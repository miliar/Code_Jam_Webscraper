#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
//#include <unordered_set>
//#include <unordered_map>

using namespace std;

int T, N, ans[3][1111111], R, P, S, cnt;

void dfs(int now, int deep, int id) {
	if(deep == 0) {
		ans[cnt][id] = now;
		return;
	}
	dfs(now, deep - 1, id * 2);
	dfs((now + 1) % 3, deep - 1, id * 2 + 1);
}

bool test(int n, int m, int left1, int right1, int left2, int right2) {
	for(int i = left1, j = left2; i < right1; i++, j++) {
		if(ans[n][i] > ans[m][j])
			return true;
		if(ans[n][i] < ans[m][j])
			return false;
	}
	return false;
}

int main() {
	scanf("%d", &T);
	for(int CC = 1; CC <= T; CC++) {
		scanf("%d", &N);
		int top = 1<<N;
		scanf("%d%d%d", &R, &P, &S);
		cnt = 0;
		for(int i = 0; i < 3; i++) {
			dfs(i, N, 0);
			int n[3] = {0}, k = cnt;
			for(int j = 0; j < top; j++)
				n[ans[k][j]]++;
			if(n[0] == P && n[1] == R && n[2] == S) {
				int k = cnt++;
				for(int len = 2; len <= (1 << N); len *= 2) {
					for(int i = 0; i < (1 << N); i += len) {
						if(test(k, k, i, i + len / 2, i + len / 2, i + len)) {
							int tmp;
							for(int j = i; j < i + len / 2; j++) {
								tmp = ans[k][j];
								ans[k][j] = ans[k][j + len / 2];
								ans[k][j + len / 2] = tmp;
							}
						}
					}
				}
			}
		}
		int best = 0;
		for(int i = 0; i < cnt; i++)
			if (test(best, i, 0, top, 0, top))
				best = i;
		if(cnt == 0)
			printf("Case #%d: IMPOSSIBLE\n", CC);
		else {
			printf("Case #%d: ", CC);
			char hashing[3] = {'P', 'R', 'S'};
			for(int i = 0; i < (1 << N); i++)
				printf("%c", hashing[ans[best][i]]);
			putchar('\n');
		}
	}
	return 0;
}

