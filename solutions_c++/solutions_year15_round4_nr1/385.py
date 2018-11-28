#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <numeric>
#include <complex>

using namespace std;

typedef long long ll;

#define mp make_pair
#define pb push_back
#define PI 3.1415926535897932384626433832795
typedef pair<int, int>  pii;
typedef vector<int>     vi;
typedef vector< pii >   vpii;

#define MAXN 110

char s[MAXN][MAXN];
int n, x, y, ans;
bool ok;

bool good_left(int yy, int xx) {
	xx--;
	while (xx >= 1) {
		if (s[yy][xx] != '.') return true;
		xx--;
	}
	return false;
}

bool good_right(int yy, int xx) {
	xx++;
	while (xx <= x) {
		if (s[yy][xx] != '.') return true;
		xx++;
	}
	return false;
}

bool good_down(int yy, int xx) {
	yy++;
	while (yy <= y) {
		if (s[yy][xx] != '.') return true;
		yy++;
	}
	return false;
}

bool good_up(int yy, int xx) {
	yy--;
	while (yy >= 1) {
		if (s[yy][xx] != '.') return true;
		yy--;
	}
	return false;
}

int main() {
	int tc;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	scanf("%i", &tc);
	for(int tt=1; tt<=tc; ++tt) {
		memset(s, '.', sizeof(s));
		scanf("%i%i", &y, &x);
		for(int i=1; i<=y; ++i) {
			scanf("%s", &s[i][1]);
		}

		ok = true;
		ans = 0;

		for(int i=1; i<=y; ++i)
			for(int j=1; j<=x; ++j) if (s[i][j] != '.') {
				
				if (s[i][j] == '<' && good_left(i, j)) continue;
				if (s[i][j] == '>' && good_right(i, j)) continue;
				if (s[i][j] == '^' && good_up(i, j)) continue;
				if (s[i][j] == 'v' && good_down(i, j)) continue;

				if (good_left(i, j) || good_right(i, j) || good_up(i, j) || good_down(i, j)) {
					ans++;
					continue;
				}

				ok = false;
				break;
			}
		printf("Case #%i: ", tt);
		if (!ok) 
			printf("IMPOSSIBLE\n");
		else
			printf("%i\n", ans);
	}
    return 0;
}