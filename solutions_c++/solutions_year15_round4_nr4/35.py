#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <vector>
#include <climits>
#include <cmath>
#include <cstdint>
#include <vector>
#include <algorithm>

using namespace std;

/* (a+b)%m */
uint64_t large_mod_add(uint64_t a, uint64_t b, uint64_t m) {
	// assumption: 0 <= a < m, 0 <= b < m, m > 0
	if (m <= (1ull << 63)) {
		return (a + b) % m;
	}
	uint64_t s = (a + b) % m;
	bool overflow = b && (a >= -b); // a + b >= 2^64
	if (!overflow) return s;
	// 0 <= s < m
	// m < s+2^64 < 3m
	// 0 < s+(2^64-m) < 2m
	// overflow condition: s+(2^64-m) >= 2^64 <=> s >= m, contradiction
	return (s - m) % m;
}

/* (a-b)%m */
uint64_t large_mod_sub(uint64_t a, uint64_t b, uint64_t m) {
	// assumption: 0 <= a < m, 0 <= b < m, m > 0
	if (a > b) return a - b;
	else if (a == b) return 0;
	else return m - b + a;
}

/* (a*b)%m */
uint64_t large_mod_mul(uint64_t a, uint64_t b, uint64_t m) {
	// assumption: 0 <= a < m, 0 <= b < m, m > 0
	if (m <= (1ull << 32)) {
		return a*b%m;
	}
	if (a > b) swap(a, b);
	if (a == 0) return 0;
	uint64_t r = 0;
	while (a>1) {
		if (a & 1) r = large_mod_add(r, b, m);
		b = large_mod_add(b, b, m);
		a >>= 1;
	}
	return large_mod_add(b, r, m);
}

/* Calculate n^k mod m
* Dependencies: large_mod_add, large_mod_mul */
uint64_t power(uint64_t n, uint64_t k, uint64_t m) {
	uint64_t ret = 1;
	n %= m;
	while (k) {
		if (k & 1) ret = large_mod_mul(ret, n, m);
		n = large_mod_mul(n, n, m);
		k >>= 1;
	}
	return ret;
}

/* Calculate n^k mod m
* Dependencies: large_mod_add, large_mod_mul, power */
long long power(long long n, long long k, long long m) {
	if (m < 0) m = -m;
	n %= m; if (n < 0) n += m;
	return power((uint64_t)n, (uint64_t)k, (uint64_t)m);
}

/* Calculate gcd(a,b)
* Dependencies: none */
long long gcd(long long a, long long b) {
	if (b == 0) return a;
	return gcd(b, a % b);
}

/* find a pair (c,d) s.t. ac + bd = gcd(a,b)
* Dependencies: none */
pair<long long, long long> extended_gcd(long long a, long long b) {
	if (b == 0) return make_pair(1, 0);
	pair<long long, long long> t = extended_gcd(b, a % b);
	return make_pair(t.second, t.first - t.second * (a / b));
}

/* Find x in [0,m) s.t. ax ≡ gcd(a, m) (mod m)
* Dependencies: extended_gcd(a, b) */
long long modinverse(long long a, long long m) {
	return (extended_gcd(a, m).first % m + m) % m;
}

long long chinese_remainder_two(long long a1, long long n1, long long a2, long long n2)
{
	return large_mod_mul(a1, n2 * modinverse(n2, n1), n1 * n2) + a2 * n1 * modinverse(n1, n2);
}

pair<long long, long long> chinese_remainder(vector<long long> a, vector<long long> n) {
	pair<long long, long long> res(a[0], n[0]);
	for (int i = 1; i < a.size(); i++){
		auto g = gcd(res.second, n[i]);
		if ((a[i] - res.first) % g) {
			res = make_pair(-1, -1);
			break;
		}
		res.first = chinese_remainder_two(res.first / g, res.second / g, a[i] / g, n[i] / g) * g + a[i] % g;
		res.second = res.second / g * n[i];
		res.first %= res.second;
	}
	return res;
}

using namespace std;

long long dt12[102][102];
long long dt3top[102][102];
const long long mod = 1000000007;


int board[38][38];

int check_board(int height, int width)
{
	for (int i = 0; i < height; i++) {
		for (int j = 0; j < width; j++) {
			if (board[i][j]) { // 2
				int cnt = 0;
				cnt += (board[i][(j + 1) % width]);
				cnt += (board[i][(j + width - 1) % width]);
				if (i + 1 < height)cnt += (board[i + 1][j]);
				if (i > 0)cnt += (board[i - 1][j]);
				if (cnt != 2) return 0;
			}
			else { // 1
				int cnt = 0;
				cnt += !(board[i][(j + 1) % width]);
				cnt += !(board[i][(j + width - 1) % width]);
				if (i + 1 < height)cnt += !(board[i + 1][j]);
				if (i > 0)cnt += !(board[i - 1][j]);
				if (cnt != 1) return 0;
			}
		}
	}
	return 1;
}

int mid_check_board(int height, int width)
{
	for (int i = 0; i < height; i++) {
		for (int j = 0; j < width; j++) {
			if (!board[i][j]) { // 1
				int cnt = 0;
				cnt += !(board[i][(j + 1) % width]);
				cnt += !(board[i][(j + width - 1) % width]);
				if (i + 1 < height)cnt += !(board[i + 1][j]);
				if (i > 0)cnt += !(board[i - 1][j]);
				if (cnt > 1) return 0;
			}
		}
	}
	return 1;
}

int dfs(int r, int c, int height, int width)
{
	if (!mid_check_board(height, width)) return 0;
	if (c == width) return dfs(r + 1, 0, height, width);
	if (r == height) return check_board(height, width);
	int res = dfs(r, c+1, height, width);
	if (r + 1 < height && board[r][c] == 1 && board[r+1][c] == 1){
		board[r][c] = 0;
		board[r + 1][c] = 0;
		res += dfs(r, c + 1, height, width);
		board[r][c] = 1;
		board[r + 1][c] = 1;
	}
	if (board[r][c] == 1 && board[r][(c+1)%width] == 1){
		board[r][c] = 0;
		board[r][(c + 1) % width] = 0;
		res += dfs(r, c + 1, height, width);
		board[r][c] = 1;
		board[r][(c + 1) % width] = 1;
	}
	return res;
}

long long getans(int R, int C)
{
	long long val = 0;
	for (int i = 0; i <= R; i++) {
		val += dt12[i][C] * dt3top[R - i][C] % mod;
	}
	val %= mod;
	return val;
}

int main(){
	for (int C = 0; C <= 100; C++) {
		dt3top[0][C] = 1;
		dt12[0][C] = 1;
	}
	for (int C = 1; C <= 100; C++) {
		dt12[1][C] = 1;
	}
	for (int C = 3; C <= 100; C += 3) {
		if (C/3%2) dt12[2][C] = 3;
		else dt12[2][C] = 9;
	}
	for (int C = 4; C <= 100; C += 4) {
		dt12[3][C] = 4;
	}
	//for (int R = 1; R <= 6; R++) {
	//	for (int C = 1; C <= 15; C++) {
	//		for (int i = 0; i < R; i++) for (int j = 0; j < C; j++) board[i][j] = 1;
	//		dt12[R][C] = dfs(0, 0, R, C);
	//		printf("%d ", dt12[R][C]);
	//	}
	//	puts("");
	//}
	for (int R = 1; R <= 100; R++) {
		for (int C = 1; C <= 100; C++) {
			/* fill dt3top: 3이 위에 있음 */
			long long val = 0;
			if (R >= 2) val = dt12[R-2][C];
			for (int i = 1; i < R - 2; i++) {
				val += dt12[i][C] * dt3top[R-2-i][C] % mod;
			}
			val %= mod;
			dt3top[R][C] = val;
		}
	}
	int T;
	scanf("%d", &T);
	for (int testcase = 1; testcase <= T; testcase++)
	{
		int R, C;
		scanf("%d%d", &R, &C);
		long long ans = 0;
		long long divval = 0;
		for (int i = 1; i <= C; i++) {
			ans += getans(R, gcd(i, C));
			ans %= mod;
			divval++;
		}
		ans =  ans * modinverse(divval, mod) % mod;
		ans += mod;
		ans %= mod;
		printf("Case #%d: %lld\n", testcase, ans);
	}
	return 0;
}