#include <cstdio>
#define rep(i, a, b) for(int i=int(a); i<int(b); i++)

int grid[110][110];

void solve() {
	int N, M;
	scanf("%d %d", &N, &M);

	rep(i, 0, N) {
		rep(j, 0, M) {
			scanf("%d", &(grid[i][j]));
		}
	}

	
	rep(i, 0, N) {
		rep(j, 0, M) {
			bool ok = true;

			rep(k, 0, N) {
				if(grid[k][j] > grid[i][j])
					ok = false;
			}

			if(ok) {
				continue;
			}

			ok = true;

			rep(k, 0, M) {
				if(grid[i][k] > grid[i][j])
					ok = false;
			}

			if(!ok) {
				printf("NO\n");
				return;
			}
		}
	}

	printf("YES\n");
	return;

}


int main() {
	int T;
	scanf("%d", &T);
	rep(i, 0, T) {
		printf("Case #%d: ", i+1);
		solve();
	}
	return 0;
}
