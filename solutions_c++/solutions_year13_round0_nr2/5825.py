#include <stdio.h>
#include <algorithm>

#define NMAX 101
#define MMAX 101
#define AMAX 101

using namespace std;

int A[NMAX][MMAX], va[NMAX*MMAX], v[AMAX], M[NMAX][MMAX];

int main () {
	int t, c, n, m, i, j, k, l, kv, ino;

	scanf("%d", &t);
	c = 0;
	while (t--) {
		scanf("%d %d", &n, &m);
		for (i = 0; i < n; ++i) {
			for (j = 0; j < m; ++j) {
				scanf("%d", &A[i][j]);
				va[i*n+j] = A[i][j];
			}
		}
		sort (va, va+n*m);
		kv = 0;
		l = 0;
		while (l < n*m) {
			v[kv] = va[l];
			l++;
			while (va[l] == v[kv])
				l++;
			kv++;
		}

		/* Propaga vs (um a um) das bordas para dentro da matriz: */
		for (l = 0; l < kv-1; ++l) { /* (ultimo nao precisa) */
			for (i = 0; i < n; ++i) 
				for (j = 0; j < m; ++j) 
					M[i][j] = 0; /* marcacoes sao zeradas a cada vez que muda de valor */

			for (i = 0; i < n; ++i) {
				/* fronteira oeste (1000): */
				if (A[i][0] == v[l]) {
					M[i][0] |= 8;
					j = 1;
					while (j < m && A[i][j] == A[i][j-1]) {
						M[i][j] |= 8;
						j++;
					}
				}
				/* fronteira leste (0100): */
				if (A[i][m-1] == v[l]) {
					M[i][m-1] |= 4;
					j = m-2;
					while (j >= 0 && A[i][j] == A[i][j+1]) {
						M[i][j] |= 4;
						j--;
					}
				}
			}

			for (j = 0; j < m; ++j) {
				/* fronteira norte (0010): */
				if (A[0][j] == v[l]) {
					M[0][j] |= 2;
					i = 1;
					while (i < n && A[i][j] == A[i-1][j]) {
						M[i][j] |= 2;
						i++;
					}
				}
				/* fronteira sul (0001): */
				if (A[n-1][j] == v[l]) {
					M[n-1][j] |= 1;
					i = n-2;
					while (i >= 0 && A[i][j] == A[i+1][j]) {
						M[i][j] |= 1;
						i--;
					}
				}
			}

			/* Agora quem tiver pelo menos duas marcacoes (opostas) assume proximo valor: */
			for (i = 0; i < n; ++i) 
				for (j = 0; j < m; ++j) {
					if ( ((M[i][j] & 8) && M[i][j] & 4) || ((M[i][j] & 2) && (M[i][j] & 1)) ) 
						A[i][j] = v[l+1];
				}
		}

		/* Terminado todo este processo, agora tem que ter todos iguais ao ultimo valor possivel: */
		ino = 0;
		for (i = 0; i < n; ++i) {
			for (j = 0; j < m; ++j) {
				if (A[i][j] != v[kv-1]) {
					printf("Case #%d: NO\n", ++c);
					ino = 1;
					break;
				}
			}
			if (ino)
				break;
		}

		if (!ino)
			printf("Case #%d: YES\n", ++c);
	}

	return 0;
}
