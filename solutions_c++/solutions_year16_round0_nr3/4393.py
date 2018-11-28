#include <algorithm>
#include <bitset>
#include <list>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <set>
#include <stack>
#include <string>
#include <utility>
#include <vector>
#include <queue>

using namespace std;

// lambda : [] (int a, int b) -> bool { body return }
// string r_str = R"(raw string)"

#define mp make_pair
#define mt make_tuple
#define eb emplace_back
#define pb push_back
#define fi first
#define se second
#define LL long long
#define ULL unsigned long long
#define PI (atan(1) * 4)
#define BASE 73
#define NMAX 10000
#define NMAX2 20001
#define MOD1 1000000007
#define ALL(V) (V).begin(), (V).end()
#define ALLR(V) (V).rbegin(), (V).rend()
#define CRLINE Duxar(__LINE__);
#define SHOWME(x) cerr << __LINE__ << ": " << #x << " = " << (x) << endl;
#define ENTER putchar('\n');
#define step(i) (i & (i - 1)) ^ i

int dx4[] = {-1, 0, 1, 0};
int dy4[] = {0, 1, 0, -1};

int dx8[] = {-1, -1, 0, 1, 1, 1, 0, -1};
int dy8[] = {0, 1, 1, 1, 0, -1, -1, -1};

void Duxar(int _this_line) {
#ifndef ONLINE_JUDGE
	printf("\n . . . . . . . . . . . . . Passed line - %d\n", _this_line);
#endif
}

bool AreEqual(double a, double b) {
	return (fabs(a - b) < 1e-10);
}

template <class T>
bool GetNr(T &_value) {
	T _sign = 1;
	char ch;
	_value = 0;
	while(!isdigit(ch = getchar())) {
		if (ch == -1) {
			return false;
		}
		ch == '-' ? _sign = -1 : _sign = 1 ;
	}
	do {
		_value = _value * 10 + (ch - '0');
	} while(isdigit(ch = getchar()));
	_value *= _sign;
	return true;
}

int lg;

LL GetXinBase(int x, int base) {
	LL ans = 0;
	for (unsigned pw = (1 << (lg + 2)); pw; pw >>= 1) {
		ans *= base;
		if (x & pw) {
			ans += 1;
		}
	}
	return ans;
}

LL GetDivisor(LL x) {
	for (LL i = 2; i * i <= x; ++i) {
		if (x % i == 0) {
			return i;
		}
	}
	return 0;
}

vector <LL> Verif(unsigned int x) {
	vector <LL> ans;
	assert(x == GetXinBase(x, 2));
	for (int i = 2; i < 11; ++i) {
		LL aux = GetXinBase(x, i);
//		printf("%d ", aux);
		LL divisor = GetDivisor(aux);
		if (divisor && divisor != aux) {
			ans.pb(divisor);
		}
		else {
			break;
		}
	}
	return ans;
}

void Solve() {
	unsigned int N, J, i;
	GetNr(N); GetNr(J);
	lg = N - 2;
	for (i = 0; i < (1 << lg) && J; ++i) {
		vector <LL> ans = Verif((((1 << lg) + i) << 1) + 1);
		if (ans.size() == 9) {
			--J;
			putchar('1');
			for (unsigned int pw = 1 << (lg - 1); pw; pw >>= 1) {
				if (i & pw) {
					putchar('1');
				}
				else {
					putchar('0');
				}
			}
			putchar('1');

			for (auto x: ans) {
				printf(" %lld", x);
			}
			putchar('\n');
		}
	}
}

int main(){
	string fileInput = "sum";
#ifdef INFOARENA
	freopen((fileInput + ".in").c_str(), "r", stdin);
	freopen((fileInput + ".out").c_str(), "w", stdout);
#else
#ifndef ONLINE_JUDGE
	freopen("/Users/duxar/Workplace/Xcode Projects/Selectie/Selectie/input", "r", stdin);
//	freopen("/Users/duxar/Workplace/Xcode Projects/Selectie/Selectie/result", "w", stdout);
#endif
#endif

	int i, t;
	GetNr(t);

	for (i = 1; i <= t; ++i) {
		printf("Case #%d:\n", i);
		Solve();
	}

	return 0;
}
