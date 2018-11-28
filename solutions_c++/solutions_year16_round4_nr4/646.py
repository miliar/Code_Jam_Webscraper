#include <bits/stdc++.h>
using namespace std;

string a[4];

int cann[5][1 << 16];

char b[4][4];
int w[4];
int m[4];

bool check(int ii, int n) {
	 if (ii == n) {
		 return true;
	 }
	 bool can = false;
	 for (int i = 0; i < n; i++) {
		 if (w[i]) {
			 continue;
		 }
		 for (int j = 0; j < n; j++) {
			 if (m[j]) {
				 continue;
			 }
			 if (b[i][j]) {
				 w[i] = 1;
				 m[j] = 1;
				 //for (int k = 0; k < i; k++) {
				 //	 cout << " ";
				 //}
				 //cout << "go " << i << " to " << j << endl;
				 if (!check(ii + 1, n)) {
					 return false;
				 }
				 //for (int k = 0; k < i; k++) {
				 //	 cout << " ";
				 //}
				 //cout << "back " << i << " to " << j << endl;
				 w[i] = 0;
				 m[j] = 0;
				 can = true;
			 }
		 }
	 }
	 return can;
}

void precalc() {
	for (int n = 1; n <= 4; n++) {
		for (int mask = 0; mask < (1 << (n * n)); mask++) {
			for (int i = 0; i < n * n; i++) {
				int k = i / n;
				int j = i % n;
				if (mask & (1 << i)) {
					b[k][j] = 1;
				}
				else {
					b[k][j] = 0;
				}
			}

			for (int i = 0; i < n; i++) {
				w[i] = m[i] = 0;
			}
			if (check(0, n)) {
				cann[n][mask] = 1;
			}
		}
	}

}

void solve(){
	int n;
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> a[i];
		for (int j = 0; j < n; j++) {
			a[i][j] -= '0';
		}
	}

	int bestcnt = 16;
	for (int mask = 0; mask < (1 << (n * n)); mask++) {
		if (!cann[n][mask]) {
			continue;
		}
		bool is = true;
		int cnt = 0;
		for (int i = 0; i < n * n; i++) {
			int k = i / n;
			int j = i % n;
			if (mask & (1 << i)) {
				b[k][j] = 1;
			}
			else {
				b[k][j] = 0;
			}
			if (b[k][j] < a[k][j]) {
				is = false;
			}
			if (b[k][j] > a[k][j]) {
				cnt++;
			}
		}
		if (!is) {
			continue;
		}
		if (cnt < bestcnt) {
			bestcnt = cnt;
		}
	}

	cout << bestcnt;


}

int main(){
#ifdef HELTHAZAR
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	precalc();

	int test;
	cin >> test;
	for (int t = 1; t <= test; t++) {
		//printf("Case #%d: ", t);
		cout << "Case #" << t << ": ";
		solve();
		cout << endl;
		//printf("\n");
	}
}
