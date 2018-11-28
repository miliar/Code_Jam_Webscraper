#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <queue>

using namespace std;

int main() {
	int cases,cn=0;
	scanf("%d",&cases);
	while (cases--) {
		int N,M,G[105][105];
		scanf("%d%d",&N,&M);
		for (int i=0; i < N; ++i) {
			for (int j=0; j < M; ++j)
				scanf("%d",&G[i][j]);
		}
		bool possible = true;
		for (int i=0; i < N; ++i) {
			for (int j=0; j < M; ++j) {
				int h = G[i][j];
				bool a = true, b = true;
				for (int k=0; k < N; ++k) {
					if (G[k][j] > h) {
						a = false;
						break;
					}
				}
				for (int k=0; k < M; ++k) {
					if (G[i][k] > h) {
						b = false;
						break;
					}
				}
				if (!a && !b) {
					possible = false;
					goto end;
				}
			}
		}
		end:
		printf("Case #%d: %s\n", ++cn, possible ? "YES" : "NO");
	}
	return 0;
}
