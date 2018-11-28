#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cstring>
using namespace std;

typedef double DB;
typedef unsigned int UI;
typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<bool> VB;
typedef vector<char> VC;
typedef vector<double> VD;
typedef vector<string> VS;
typedef vector<VI> VVI;
typedef vector<PII> VPII;

#define PB push_back
#define MP make_pair
#define ALL(x) (x).begin(), (x).end()
#define CLR(a, x) memset(a, x, sizeof(a))

template <class T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template <class T> inline void checkMax(T& a, T b) { if (b > a) a = b; }

inline void RD(int & a) {
    a = 0;
    char c = getchar();
    while (c < '0' || c > '9') c = getchar();
    while (c >= '0' && c <= '9') { a = a * 10 + c - '0'; c = getchar(); }
}
inline void RD(int & a, int & b) { RD(a); RD(b); }
inline void RD(int & a, int & b, int &c) { RD(a); RD(b); RD(c); }
inline void RD(int & a, int & b, int & c, int & d) { RD(a); RD(b); RD(c); RD(d); }

const int MOD = 1000000007;
LL inv(LL a) { return a == 1 ? 1 : (MOD - MOD / a) * inv(MOD % a) % MOD; }
LL mPow(LL x, int n) { LL ret = 1; while (n) { if (n & 1) ret = ret * x % MOD; x = x * x % MOD; n >>= 1; } return ret; }
LL mC(int n, int m) { LL ret = 1; for(int i = 1; i <= m; i++, n--) { ret = ret * n % MOD * inv(i) % MOD; } return ret; }

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	int cas;
	cin >> cas;
	for (int t = 1; t <= cas; t++) {
		DB C, F, X;
		cin >> C >> F >> X;

		DB rank = 2.0, cur_time = 0.0, ans = X * 0.5;
		while (true) {
			DB k = C / rank;
			cur_time += k;
			rank += F;
			DB tmp = cur_time + X / rank;

			// printf("here : when: %.2f rank = %.2f exp = %.2f\n", cur_time, rank, tmp);
			// system("PAUSE");

			if (tmp < ans) {
				ans = tmp;
			} else {
				break;
			}
		}

		printf("Case #%d: %.7f\n", t, ans);
	}

    return 0; 
}