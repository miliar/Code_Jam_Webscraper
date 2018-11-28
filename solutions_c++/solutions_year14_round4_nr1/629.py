#include <iostream>
#include <algorithm>
using namespace std;

#define MAXN 10100

int d[MAXN], n[MAXN];

int main() {
	int N, i, j, t, T, X, tmp, D, RES;
	
	cin >> T;
	for (t=1; t<=T; t++) {
		cin >> N >> X;
		for (i=0; i<N; i++) cin >> n[i];
		sort(n, n+N);
		
		D = RES = 0;
		for (i=N-1; i>=0; i--) {
			for (j=0; j<D; j++) if (d[j]+n[i] <= X) break;
			if (j == D) { d[D++] = n[i]; RES++; }
			else {
				for (; j<D-1; j++) d[j] = d[j+1];
				D--;
			}
		}
		cout << "Case #" << t << ": " << RES << endl;
	}

	return 0;
}
