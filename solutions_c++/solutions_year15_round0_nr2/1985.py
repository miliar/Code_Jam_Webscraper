#include <iostream>
using namespace std;

#define MAXN 1024

int n[MAXN];

int count(int num, int k) {
	return num/k + (num%k ? 1 : 0) - 1;
}

int main() {
	int T, t, N, i, j, MAX, tmp, RES;
	
	cin >> T;
	for (t=1; t<=T; t++) {
		cin >> N;
		
		MAX = 0;
		for (i=0; i<N; i++) { cin >> n[i]; MAX = max(MAX, n[i]); }
		
		RES = MAX;
		for (i=1; i<=MAX; i++) {
			tmp = 0;
			for (j=0; j<N; j++) tmp += count(n[j], i);
			RES = min(RES, tmp+i);
		}
		cout << "Case #" << t << ": " << RES << endl;
	}

	return 0;
}
