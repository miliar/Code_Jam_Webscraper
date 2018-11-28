#pragma comment(linker, "/STACK:640000000")
#include<iostream>
#include<cstdio>
#include<cassert>
#include<cstring>
#include<ctime>
#include<cstdlib>
#include<cmath>
#include<string>
#include<sstream>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<vector>
#include<bitset>
#include<algorithm>

#define pb push_back
#define ppb pop_back
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define sz(x) (int)(x).size()
#define ll long long
#define bit __builtin_popcountll
#define sqr(x) (x) * (x)
#define forit(it,S) for(__typeof((S).begin()) it = (S).begin(); it != (S).end(); it++)

using namespace std;

typedef pair<int, int> pii;

const double eps = 1e-9;
const double pi = acos(-1.0);

char s[111][111];
int c[111][111];

void solve() {
	int n,m; cin >> n >> m;
	for (int i = 0; i < n; i++) {
		scanf("%s",s[i]);
		for (int j = 0; j < m; j++) {
			c[i][j] = 0;
		}
	}
	int res = 0;
	for (int i = 0; i < n; i++) {		
		for (int j = 0; j < m; j++) if (s[i][j] != '.') {
			if (s[i][j] == '<') res++;
			c[i][j]++;
			break;
		}
		for (int j = m - 1; j >= 0; j--) if (s[i][j] != '.') {
			if (s[i][j] == '>') res++;
			c[i][j]++;
			break;
		}
	}
	for (int j = 0; j < m; j++) {
		for (int i = 0; i < n; i++) if (s[i][j] != '.') {
			if (s[i][j] == '^') res++;
			c[i][j]++;
			break;
		}
		for (int i = n - 1; i >= 0; i--) if (s[i][j] != '.') {
			if (s[i][j] == 'v') res++;
			c[i][j]++;
			break;
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) if (c[i][j] == 4) {
			cout << "IMPOSSIBLE" << endl;
			return;
		}
	}
	cout << res << endl;
}

int main() {
	#ifdef LOCAL
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	#endif

	int Cases; cin >> Cases;

	for (int Case = 1; Case <= Cases; Case++) {
		printf("Case #%d: ",Case);
		solve();
	}
	
	return 0;
}
