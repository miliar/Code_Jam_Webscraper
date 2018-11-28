#include <cstdio>
#include <algorithm>
using namespace std;
int a[1005], id[1005], pos[1005], pos2[1005];
int T, N;
bool b[105];
int mxx;

void dfs(int p, bool up, int last) {
	if (p == N) {
	
		int cnt = 0;
		for (int i = 0; i < N; ++i) {
			for (int j = i+1; j < N; ++j) {
				if ((pos2[i] > pos2[j]) ^ (pos[i] > pos[j])) {
					++cnt;
				}
			}
		}

		if (cnt < mxx) {
			mxx = cnt;
		}
		return;
	}
	
	if (up) {
		for (int i = last + 1; i < N; ++i) {
			if (b[i]) continue;

			b[i] = true;
			id[p] = i;
			pos2[i] = p;
			dfs(p + 1, up, i);
			dfs(p + 1, false, i);
			b[i] = false;
		}
	} else {
		for (int i = 0; i < last; ++i) {
			if (b[i]) continue;
			
			b[i] = true;
			id[p] = i;
			pos2[i] = p;
			dfs(p + 1, false, i);
			b[i] = false;
		}
	}

}

int main() {
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc) {
		scanf("%d", &N);
		for (int i =  0; i < N;++i) {
			scanf("%d", &a[i]);
			id[i] = a[i];
		}
		
		sort(id, id+N);
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				if (a[i] == id[j]) {
					a[i] = j;
					pos[j] = i;
				}
			}
		}

		mxx = 2000000000;
		dfs(0, true, -1);
		printf("Case #%d: %d\n", tc, mxx);
	}
	return 0;
}
