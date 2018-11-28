#include <bits/stdc++.h>

#define itn itn
#define all(x) (x).begin(), (x).end()

using namespace std;

inline int nxt(){
	int x;
	scanf("%d", &x);
	return x;
}

void solve(){
	int n = nxt(), m = nxt();
	vector<string> a(n);
	for (int i = 0; i < n; i++)
		cin >> a[i];
	int ans = 0;
	vector<int> r(n), c(m);
	for (int i = 0; i < n; i++){
		for (int j = 0; j < m; j++){
			if (a[i][j] != '.'){
				r[i]++;
				c[j]++;
			}
		}
	}
	for (int i = 0; i < n; i++){
		for (int j = 0; j < m; j++){
			if (a[i][j] != '.'){
				int xx = 0, yy = 0;
				if (a[i][j] == '<')
					yy--;
				if (a[i][j] == '>')
					yy++;
				if (a[i][j] == '^')
					xx--;
				if (a[i][j] == 'v')
					xx++;
				int x = i;
				int y = j;
				do {
					x += xx;
					y += yy;
					if (x >= n || x < 0 || y >= m || y < 0)
						break;
				} while (a[x][y] == '.');
				if (x >= n || x < 0 || y >= m || y < 0){
					if (r[i] > 1 || c[j] > 1)
						ans++;
					else {
						printf("IMPOSSIBLE\n");
						return;
					}
				}
			}
		}
	}
	printf("%d\n", ans);
}

int main(){

	int T = nxt();
	for (int _ = 0; _ < T; _++){
		printf("Case #%d: ", _ + 1);
		solve();
		cerr << "Test #" << _ + 1 << " completed\n";
	}

	return 0;
}