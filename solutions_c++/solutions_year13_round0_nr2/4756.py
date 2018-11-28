#include <cstdio>
#include <cstring>

#define max(a,b) (a<b ? b : a)

using namespace std;

int main() {
	int T, M, N;
	int A[105][105],
		h[105],
		v[105];
	bool Posible;
	scanf("%d\n", &T);
	for (int t=1 ; t<=T ; t++) {
		Posible = true;
		scanf("%d %d\n", &N, &M);

		memset(h, 0, sizeof(h));
		memset(v, 0, sizeof(v));

		for (int n=0 ; n<N ; n++) {
			for (int m=0 ; m<M ; m++) {
				scanf("%d", &A[n][m]);
				v[n] = max(v[n], A[n][m]);
				h[m] = max(h[m], A[n][m]);
			}
		}

		for (int n=0 ; Posible &&  n<N ; n++) {
			for (int m=0 ; Posible && m<M ; m++) {
				Posible = Posible && (A[n][m]==v[n] || A[n][m]==h[m]);
			}
		}

		if (Posible) printf("Case #%d: YES\n", t);
		else		 printf("Case #%d: NO\n", t);
	}
	return 0;
}
