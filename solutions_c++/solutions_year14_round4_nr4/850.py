#include <stdio.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <set>
using namespace std;

const int MAXN = 1010;

const int MOD = 1000000007;



int a[MAXN];
char s[MAXN][110];
int N, M;
int cnt = 0, ans = 0;

void dfs(int m) {
	if (m == M) {
		int tt = 0;
		for (int i = 0; i < N; i++) {
			set<string> st;
			for (int j = 0; j < M; j++) {
				if (a[j] == i) {
					string c;
					st.insert(c);
					for (int k = 0; s[j][k]; k++) {
						c = c + s[j][k];
						st.insert(c);
					}
				}
			}
			tt += st.size();
		}
		if (tt > ans) {
			ans = tt;
			cnt = 0;
		}
		if (tt == ans) {
			cnt++;
		}
		return;
	}
	for (int i = 0; i < N; i++) {
		a[m] = i;
		dfs(m + 1);
	}
}



int main() {
	int T;
	freopen("x.txt", "r", stdin);freopen("w.txt", "w", stdout);
	
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++) {
		scanf("%d%d", &M, &N);
		for (int i = 0; i < M; i++) {
			scanf("%s", s[i]);
		}
		cnt = 0;
		ans = 0;
		dfs(0);
		printf("Case #%d: %d %d\n", cas, ans, cnt);
	}
}
