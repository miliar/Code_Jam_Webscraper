#include <cstdio>

int T, q = 1;

int main()
{
	for (scanf ("%d", &T); T--;)
	{
		int N, M;
		int okay = 1;
		char f[111][111] = {};
		scanf ("%d%d", &N, &M);
		for (int i=0; i<N; i++) {
			for (int j=0; j<M; j++)
				scanf ("%d", &f[i][j]);
		}
		int dx[] = { -1, 0, 1, 0 },
			dy[] = { 0, 1, 0, -1 };
		for (int i=0; i<N; i++) {
			int cnt = 0;
			for (int j=0; j<M; j++) {
				cnt += f[i][j] == 2;
			}
			if (!cnt) {
				for (int j=0; j<M; j++) {
					f[i][j] = 0;
				}
			}
		}
		for (int i=0; i<M; i++) {
			int cnt = 0;
			for (int j=0; j<N; j++) {
				cnt += f[j][i] == 2;
			}
			if (!cnt) {
				for (int j=0; j<N; j++) {
					f[j][i] = 0;
				}
			}
		}
		for (int i=0; i<N; i++) {
			for (int j=0; j<M; j++) {
				if (f[i][j] == 1) okay = 0;
			}
		}
		printf ("Case #%d: ", q++);
		puts (okay ? "YES" : "NO");
	}
	return 0;
}