#include <stdio.h>
#include <algorithm>

int p[10000];

int main()
{
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		int R, C, N;
		scanf("%d %d %d", &R, &C, &N);
		int res = R*C*2;
		for (int mode = 0; mode < 2; mode++) {
			memset(p, 0, sizeof(int)*10000);
			int rest = N;
			for (int i=0; i<C; i++) {
				for (int j=0; j<R; j+=std::max(R-1, 1)) {
					if ((i+j)%2 == mode && rest > 0 && p[i*R+j] == 0) {
						p[i*R+j] = 1;
						rest--;
					}
				}
			}
			for (int i=0; i<C; i+=std::max(C-1, 1)) {
				for (int j=0; j<R; j++) {
					if ((i+j)%2 == mode && rest > 0 && p[i*R+j] == 0) {
						p[i*R+j] = 1;
						rest--;
					}
				}
			}
			for (int i=1; i<C-1; i++) {
				for (int j=1; j<R-1; j++) {
					if ((i+j)%2 == mode && rest > 0 && p[i*R+j] == 0) {
						p[i*R+j] = 1;
						rest--;
					}
				}
			}
			for (int i=0; i<C; i+=std::max(C-1, 1)) {
				for (int j=0; j<R; j+=std::max(R-1, 1)) {
					if ((i+j)%2 != mode && rest > 0 && p[i*R+j] == 0) {
						p[i*R+j] = 1;
						rest--;
					}
				}
			}
			for (int i=0; i<C; i++) {
				for (int j=0; j<R; j+=std::max(R-1, 1)) {
					if ((i+j)%2 != mode && rest > 0 && p[i*R+j] == 0) {
						p[i*R+j] = 1;
						rest--;
					}
				}
			}
			for (int i=0; i<C; i+=std::max(C-1, 1)) {
				for (int j=0; j<R; j++) {
					if ((i+j)%2 != mode && rest > 0 && p[i*R+j] == 0) {
						p[i*R+j] = 1;
						rest--;
					}
				}
			}
			for (int i=1; i<C-1; i++) {
				for (int j=1; j<R-1; j++) {
					if ((i+j)%2 != mode && rest > 0 && p[i*R+j] == 0) {
						p[i*R+j] = 1;
						rest--;
					}
				}
			}
			int cnt = 0;
			for (int i=0; i<C; i++) {
				for (int j=0; j<R; j++) {
					if (i != C-1) {
						if (p[i*R+j] && p[(i+1)*R+j]) {
							cnt++;
						}
					}
					if (j != R-1) {
						if (p[i*R+j] && p[i*R+j+1]) {
							cnt++;
						}
					}
				}
			}
			res = std::min(res, cnt);
		}
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}
