#include <algorithm>
#include <string>
#include <string.h>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <iostream>
#include <fstream>
#include <cmath>
#include <math.h>
#include <iomanip>
#include <stdlib.h>
#include <stdio.h>
#include <bitset>
#include <iterator>

using namespace std;

#define FOR(i,n) for (int i=0; i<n; ++i)
#define FORE(i,n) for (int i=0; i<=n; ++i)
#define REP(i,a,b) for (int i=a; i<b; ++i)
#define REPE(i,a,b) for (int i=a; i<=b; ++i)
#define mp make_pair
#define pb push_back

typedef long double dbl;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef long long int LL;
typedef vector<int> VI;
typedef vector<bool> VB;
typedef vector<VI> VVI;
const dbl pi = 3.14159265358979323846;
const int inf = (int) 1e9;
const dbl eps = 1e-9;

const int N = 105;

char s[N][N];
int x[N];
int y[N];
bool used[N][N];
bool used2[N][N];
int n,m;

bool check() {
	FOR(i,N) {
		x[i] = 0;
		y[i] = 0;
	}
	FOR(i,n) {
		FOR(j,m) {
			if (s[i][j] != '.') {
				++x[i];
				++y[j];
			}
		}
	}
	FOR(i,n) {
		FOR(j,m) {
			if (s[i][j] != '.' && x[i] == 1 && y[j] == 1) {
				return false;
			}
		}
	}
	return true;
}

int solve() {
	memset(used, false, sizeof(used));
	int res = 0;
	FOR(i,n) {
		int j = 0;
		while(j < m && s[i][j] == '.') {
			++j;
		}
		if (j < m && s[i][j] == '<' && !used[i][j]) {
			++res;
			used[i][j] = true;
		}
		j = m - 1;
		while(j >= 0 && s[i][j] == '.') {
			--j;
		}
		if (j >= 0 && s[i][j] == '>' && !used[i][j]) {
			++res;
			used[i][j] = true;
		}
	}
	FOR(j,m) {
		int i = 0;
		while(i < n && s[i][j] == '.') {
			++i;
		}
		if (i < n && s[i][j] == '^' && !used[i][j]) {
			++res;
			used[i][j] = true;
		}
		i = n - 1;
		while(i >= 0 && s[i][j] == '.') {
			--i;
		}
		if (i >= 0 && s[i][j] == 'v' && !used[i][j]) {
			++res;
			used[i][j] = true;
		}
	}
	return res;
}


int main()
{
#ifdef _DEBUG
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#else
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
#endif  
	int T;
	cin >> T;
	FOR(TT,T) {		
		cin >> n >> m;
		FOR(i,n) {
			FOR(j,m) {
				cin >> s[i][j];
			}
		}
		if (!check()) {
			cout << "Case #" << TT + 1 << ": IMPOSSIBLE\n";
			continue;
		}
		int res = solve();
		cout << "Case #" << TT + 1 << ": " << res << "\n";
	}
    return 0;
}