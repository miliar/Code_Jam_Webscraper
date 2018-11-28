#include <stdio.h>
#include <string>
#include <string.h>
#include <algorithm>
#include <set>
using namespace std;

const int MAXN = 30;

char s[MAXN][MAXN];

int N;

int ans;

bool check() {
	//for (int i = 0; i < N; i++) puts(s[i]); puts("");
	


	for (int i = 0; i < N; i++) {
		set<set<int> > st;
		set<int> empty;
		st.insert(empty);
		int safe = 0;

		//printf("i = %d\n", i);

		for (int j = 0; j < N; j++) {

			//printf("j = %d\n", j);

			if (s[i][j] == '1') {
				set<set<int> > tmp = st;
				for (auto u : tmp) {
					set<int> v = u;
					v.insert(j);

					set<int> others;
					for (auto k : v) {
						for (int l = 0; l < N; l++) {
							if (s[l][k] == '1') {
								others.insert(l);
							}
						}
					}

					//printf("%lu %lu\n", v.size(), others.size());

					if (v.size() >= others.size()) {
						safe = 1;
					}
					st.insert(v);
				}
			}

			//printf("safe = %d\n", safe);
		}
		if (safe == 0) return false;
	}
	return true;
}

void dfs(int m, int n, int cost) {
	if (cost >= ans) return;
	if (m == N) {
		if (check()) {
			ans = cost;
		}
	} else if (n == N) {
		dfs(m + 1, 0, cost);
	} else {
		dfs(m, n + 1, cost);
		if (s[m][n] == '0') {
			s[m][n] = '1';
			dfs(m, n + 1, cost + 1);
			s[m][n] = '0';
		}
	}
}

int main() {
	int cas;

	scanf("%d", &cas);
	for (int re = 1; re <= cas; re++) {
		
		scanf("%d", &N);
		for (int i = 0; i < N; i++) {
			scanf("%s", s[i]);
		}
		ans = N * N;
		dfs(0, 0, 0);
		printf("Case #%d: %d\n", re, ans);
	}
}