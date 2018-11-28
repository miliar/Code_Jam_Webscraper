#include <cstdio>
#include <cstring>
#define MAXN 128
#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))
#define FOR(i,a,b) for(int (i)=(a);(i)<(b);(i)++)
using namespace std;

int R, C;
int d[MAXN][MAXN], s[MAXN][MAXN];
int maxr[MAXN], maxc[MAXN];
int main() {
	int tc;
	scanf("%d", &tc);
	FOR(t,0,tc) {
		bool impossible = false;
		scanf("%d %d", &R, &C);
		memset(maxr, -1, sizeof(maxr));
		memset(maxc, -1, sizeof(maxc));
		FOR(i,0,R) {
			FOR(j,0,C) {
				scanf("%d", &d[i][j]);
				maxr[i] = max(maxr[i], d[i][j]);
				maxc[j] = max(maxc[j], d[i][j]);
			}
		}
		
		FOR(i,0,R) {
			FOR(j,0,C) {
				s[i][j] = 100;
				s[i][j] = min(s[i][j], maxr[i]);
				s[i][j] = min(s[i][j], maxc[j]);
				if(s[i][j] != d[i][j]) {
//					fprintf(stderr, "(%d,%d=%d)\n", i, j, s[i][j]);
					impossible = true;
				}
			}
		}
		printf("Case #%d: ", t+1);
		if(impossible)
			printf("NO\n");
		else
			printf("YES\n");
	}
	return 0;
}
