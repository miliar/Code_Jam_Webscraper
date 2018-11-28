#include <iostream>
using namespace std;

int T, N, m[1000], X, A, B;

int main() {
	scanf ("%d", &T);
	for (int t = 1 ; t <= T ; t++) {
		
		A = B = X = 0;
		scanf ("%d", &N);
		for (int i = 0 ; i < N ; i++)
			scanf ("%d", &m[i]);
		
		for (int i = 1 ; i < N ; i++) {
			A += max (0, m[i-1] - m[i]);
			X = max (X, m[i-1] - m[i]);
		}
		
		for (int i = 0 ; i < N-1 ; i++)
			B += min (m[i], X);
		
		printf ("Case #%d: %d %d\n", t, A, B);
	}
	return 0;
}