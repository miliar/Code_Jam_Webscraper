#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <queue>

#define LL long long
#define mp(x, y) make_pair(x, y)
#define pb(x) push_back(x)
#define size(S) S.size()
#define PII pair<int, int>
#define PID pair<int, double>

using namespace std;

int T, n, m, map[110][110];

inline bool ok(int x, int y) {
	bool valid = true;
	for (int i = 1; i <= n; i++) 
		if (map[i][y] > map[x][y]) {
			valid = false;
			break;
		}
	if (valid) return true;
	
	valid = true;
	for (int i = 1; i <= m; i++) 
		if (map[x][i] > map[x][y]) {
			valid = false;
			break;
		}
	if (valid) return true;
	
	return false;
}

int main(){
	scanf("%d", &T);
	for (int cases = 1; cases <= T; cases++) {
		cout << "Case #" << cases << ": ";
		scanf("%d%d", &n, &m);
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= m; j++)
				scanf("%d", map[i] + j);
		
		bool valid = true;
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= m; j++)
				if (!ok(i, j)) {
					valid = false;
					break;
				}
			if (!valid) break;
		}
		
		if (valid) cout << "YES" <<endl;
		else cout << "NO" << endl;
	}
}