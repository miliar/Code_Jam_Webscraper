#include <iostream>
#include <string>

#define MAXN 10

using namespace std;

int tests, n, kk, ans, cc[MAXN];
string tmp;
bool in[MAXN][MAXN];

bool chk(int a, int b, int c, int d) {
	//if (c == 257) printf("XXXXX %d %d %d %d\n", a, b, c, d);
	if (a == n) {
		int tmp = (((c>>(n * b))|cc[b])&((1<<n)-1));
		//if (c == 257) printf("YYYYY %d\n", tmp);
		if ((d&tmp) == tmp) return false;
		else return true;
	}
	if (a == b) return chk(a + 1, b, c, d);
	bool ok = false;
	for (int i = 0 ; i < n ; i ++) {
		if ((in[a][i] || ((c>>(n * a + i))&1)) && !chk(a + 1, b, c, d|(1<<i))) return false;
		if ((in[a][i] || ((c>>(n * a + i))&1))) ok  = true;
	}
	return ok;
}

int main() {
	cin >> tests;
	for (int test = 1 ; test <= tests ; test ++) {
		cout << "Case #" << test << ": ";
		cin >> n;
		for (int i = 0 ; i < n ; i ++) {
			cin >> tmp;
			for (int j = 0 ; j < n ; j ++) in[i][j] = (tmp[j] == '1');
			cc[i] = 0;
			for (int j = 0 ; j < n ; j ++) if (in[i][j]) cc[i] += (1<<j);
		}
		if (n == 1) {
			if (in[0][0]) cout << "0\n";
			else cout << "1\n";
			continue;
		}
		ans = n * n * 10000;
		for (int k = 0 ; k < (1<<(n * n)) ; k ++) {
			bool ok = true;
			int c = 0;
			for (int i = 0 ; i < (n * n) ; i ++) if ((k>>i)&1) c ++;
			for (int i = 0 ; i < n ; i ++) for (int j = 0 ; j < n ; j ++) if (((k>>(n * i))&cc[i]) != 0) ok = false;
			if (!ok) continue;
			for (int i = 0 ; i < n ; i ++) {
				if (!chk(0, i, k, 0)) {
					ok = false;
					break;
				}
			}
			if (ok) {
				//if (c < ans) printf("AAAAA %d\n", k);
				ans = min(ans, c);
			}
		}
		cout << ans << endl;
	}
	return 0;
}