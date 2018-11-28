#include <bits/stdc++.h>
using namespace std;

#define forn(i,n) for (int i = 0; i < int(n); ++i)
#define pb push_back
#define mp make_pair
#define sz(a) int(a.size())
#define all(a) a.begin(),a.end()

typedef pair<int,int> pt;
#define x first
#define y second

typedef long long li;
typedef long double ld;

using namespace std;

bool solve(int);

int main() {
#ifdef SU1
	freopen("input.txt", "r", stdin);
//	freopen("output.txt", "w", stdout);
#endif

	int t;
	cin >> t;

	int test = 0;
	while (solve(test++));
	
	return 0;
}

int n;

int mask(int x) {
	int res = 0;
	while (x) {
		res |= (1 << (x % 10));
		x /= 10;
	}
	return res;
}

bool solve(int tc) {
	if (!(cin >> n))
		return false;
	int seen = 0;
	printf("Case #%d: ", tc + 1);
	
	if (n == 0) {
		puts("INSOMNIA");
		return true;
	}

	int a = 0;
	int res = 0;
	while (seen != 1023) {
		a += n;
		seen |= mask(a);
		res++;
	}
	printf("%d\n", a);
	return true;
}
