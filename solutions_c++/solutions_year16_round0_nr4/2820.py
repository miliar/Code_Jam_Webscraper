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
	assert(cin >> t);

	int test = 0;
	while (solve(test++));
	
	return 0;
}

int k, c, s;

bool solve(int tc) {
	if (!(cin >> k >> c >> s))
		return false;
	printf("Case #%d:", tc + 1);
	assert(k == s);
	forn(i, k)
		printf(" %d", i + 1);
	puts("");
	return true;
}
