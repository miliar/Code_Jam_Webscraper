#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

#define MAXN 1024

int n[MAXN], dc[MAXN], rc[MAXN], o[MAXN];
bool used[MAXN];

bool cmp(const int &a, const int &b) {
	return dc[a] < dc[b];
}

int main() {
	int t, T, i, j, N, RES, tmp;
	
	cin >> T;
	for (t=1; t<=T; t++) {
		cin >> N;
		for (i=0; i<N; i++) cin >> n[i];
		
		RES = 0;
		for (i=0; i<N; i++) {
			dc[i] = rc[i] = 0;
			for (j=0; j<i; j++) if (n[j] > n[i]) dc[i]++;
			for (j=i+1; j<N; j++) if (n[j] > n[i]) rc[i]++;
			RES += min(dc[i], rc[i]);
		}
		cout << "Case #" << t << ": " << RES << endl;
		
	}

	return 0;
}
