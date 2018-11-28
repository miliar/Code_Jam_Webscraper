#include <map>
#include <set>
#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long lint;
#define pp(a,b) push_back(make_pair((a),(b)))
#define pb push_back
#define mp make_pair
#define buybuy {printf("-1\n");return 0;}

int next() {int x; cin >> x; return x;}
lint lnext() {lint x; cin >> x; return x;}
//template<typename T> outln(T x) {cout << x; cout << "\n";}
#define prt(a) cout << a << "\n";
#define prtn(a, n) for(int iiiiiiiiiii = 0; iiiiiiiiiii < n; iiiiiiiiiii++) cout << a[iiiiiiiiiii] << " "; cout << "\n";
#define prtall(a) for (auto iiiiiiiiiii : a) cout << iiiiiiiiiii << " "; cout << "\n";

int gcd(int x, int y) {
	return x*y ? x > y ? gcd(y, x) : gcd(y % x, x) : x + y;
}
int lcm(int x, int y) {return x / gcd(x, y) * y;}

int main() {
	int tests = next();
	lint mod = 1000000007;
	for (int test = 1; test <= tests; test++) {
		int r = next();
		int c = next();
		
		int k = 13;
		lint a[r + 1][k]; // was 3
		lint b[r + 1][k]; // was 2
		for (int i = 0; i <= r; i++) for (int j = 0; j < k; j++) a[i][j] = b[i][j] = 0;
		//for (int i = 1; i < k; i++) if (c % i == 0) a[0][i] = b[0][i] = 1;
		a[0][1] = b[0][1] = 1;

		for (int i = 1; i <= r; i++) {
			// a
			if (i == 1) for (int j = 1; j < k; j++) a[i][j] = 0;
			else for (int j = 1; j < k; j++) a[i][j] = b[i - 2][j];
			
			// b
			for (int j = 1; j < k; j++) b[i][j] = a[i - 1][j];
			if (i >= 2)
				for (int j = 1; j < k; j++) if (c % 3 == 0) if (lcm(j, 3) < k) b[i][lcm(j, 3)] = (b[i][lcm(j, 3)] + 3 * a[i - 2][j]) % mod;
			if (i >= 2)
				for (int j = 1; j < k; j++) if (c % 6 == 0) if (lcm(j, 6) < k) b[i][lcm(j, 6)] = (b[i][lcm(j, 6)] + 6 * a[i - 2][j]) % mod;
			if (i >= 3)
				for (int j = 1; j < k; j++) if (c % 4 == 0) if (lcm(j, 4) < k) b[i][lcm(j, 4)] = (b[i][lcm(j, 4)] + 4 * a[i - 3][j]) % mod;
		}
		
		lint answ[k];
		for (int i = 1; i < k; i++) {
			answ[i] = (a[r][i] + b[r][i]) % mod;
			//while (answ[i] % i != 0) answ[i] += mod;
			answ[i] /= i;
		}

		//prtn(a[r], k);
		//prtn(b[r], k);
		//prtn(answ, k);
		/*for (int i = 1; i < k; i++)
			for (int j = 1; j < i; j++) if (i % j == 0) answ[i] = (answ[i] - answ[j] + mod) % mod;
		*/
		int ret = 0;
		for (int i = 1; i < k; i++) ret += answ[i];
		ret %= mod;
		printf("Case #%d: %d\n", test, ret);
	}

}
