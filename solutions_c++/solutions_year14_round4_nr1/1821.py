#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <set>
#include <queue>

using namespace std;

#define fi "A-small-attempt1.in"
#define fo "out.txt"
const int MAXN = 10000 + 5;
const int INF = 1000000000;
const long long INFL = 1000000000000000000L;
const int MAXS = 5000 + 5;

int N, X;
int S[MAXN];
int visited[MAXN];
int res;
void recursion(int, int);

int main() {
	freopen(fi, "r", stdin);
	freopen(fo, "w", stdout);

	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		printf("Case #%d: ", t);
		scanf("%d%d", &N, &X);
		for (int i = 0; i < N; ++i) {
			scanf("%d", S + i);
		}
		memset(visited, 0, sizeof visited);
		res = INF;
		recursion(1, 0);
		printf("%d\n", res);
	}
}

void recursion(int x, int cnt) {
	if (x > res) return;
	if (cnt == N) {
		res = x - 1;
		return;
	}
	if (cnt + 2 <= N) {
		for (int i = 0; i < N; ++i) {
			if (!visited[i]) {
				for (int k = 0; k < N; ++k) {
					if (k != i && !visited[k] && S[i] + S[k] <= X) {
						visited[i] = visited[k] = 1;
						recursion(x + 1, cnt + 2);
						visited[i] = visited[k] = 0;
					}
				}
			}
		}
	}
	for (int i = 0; i < N; ++i) {
			if (!visited[i]) {
				visited[i] = 1;
				recursion(x + 1, cnt + 1);
				visited[i] = 0;
			}
		}
}
