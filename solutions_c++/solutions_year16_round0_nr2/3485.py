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

string s;

bool solve(int tc) {
	if (!(cin >> s))
		return false;
	while (sz(s) && s.back() == '+')
		s.pop_back();
	s.erase(unique(all(s)), s.end());
	printf("Case #%d: %d\n", tc + 1, sz(s));
	return true;
}
