#include <stdio.h>

int PopCount(int bits) 
{ 
    bits = (bits & 0x55555555) + (bits >> 1 & 0x55555555);
    bits = (bits & 0x33333333) + (bits >> 2 & 0x33333333);
    bits = (bits & 0x0f0f0f0f) + (bits >> 4 & 0x0f0f0f0f);
    bits = (bits & 0x00ff00ff) + (bits >> 8 & 0x00ff00ff);
    return (bits & 0x0000ffff) + (bits >>16 & 0x0000ffff);
} 

int main()
{
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		int N;
		scanf("%d", &N);
		int a = 0;
		for (int i=0; i<N; i++) {
			for (int j=0; j<N; j++) {
				char c;
				scanf(" %c", &c);
				a <<= 1;
				if (c == '1') {
					a |= 1;
				}
			}
		}
		int res = N*N;
		for (int i=0; i<(1<<(N*N)); i++) {
			if (i & a) {
				continue;
			}
			int bb = i|a;
			int b[4] = {0};
			for (int j=0; j<N; j++) {
				b[j] = (bb>>(N*(N-j-1)))&((1<<N)-1);
			}
			bool f[4] = {false};
			for (int j=0; j<N; j++) {
				if (f[j]) {
					continue;
				}
				int ct = 1;
				for (int k=j+1; k<N; k++) {
					if (b[j] == b[k]) {
						ct++;
						f[k] = true;
					} else if (b[j] & b[k]) {
						goto esc;
					}
				}
				if (ct != PopCount(b[j])) {
					goto esc;
				}
			}
			int ne = PopCount(i);
			if (ne < res) {
				res = ne;
			}

esc:
			;
		}
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}