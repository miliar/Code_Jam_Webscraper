#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <numeric>
#include <cctype>
#include <tuple>
#include <array>
#include <climits>
#include <bitset>
#include <cassert>


#define FOR(i, a, b) for(int i = (a); i < (int)(b); ++i)
#define rep(i, n) FOR(i, 0, n)
#define ALL(v) v.begin(), v.end()
#define REV(v) v.rbegin(), v.rend()
#define MEMSET(v, s) memset(v, s, sizeof(v))
#define UNIQUE(v) (v).erase(unique(ALL(v)), (v).end())
#define MP make_pair
#define MT make_tuple

using namespace std;

typedef long long ll;
typedef pair<ll, ll> P;

const string dir = "^>v<";
int dx[] = { 0, 1, 0, -1 };
int dy[] = { -1, 0, 1, 0};

const int N = 110;
int dp[N][N][4];

string board[N];

int h, w;
int dfs(int r, int c, int d){
	if (r < 0 || r >= h || c < 0 || c >= w) return 0;
	int &res = dp[r][c][d];
	if (res + 1) return res;
	if (board[r][c] != '.') return 1;
	res = dfs(r + dy[d], c + dx[d], d);
	return res;
}

int main(){
	int T;
	cin >> T;
	for (int CASE = 1; CASE <= T; ++CASE){
		MEMSET(dp, -1);
		cin >> h >> w;
		rep(i, h) cin >> board[i];

		int ans = 0, ok = 1;
		rep(i, h) rep(j, w){
			if (board[i][j] == '.') continue;
			int cost = 1000;
			rep(d, 4){
				int x = dfs(i + dy[d], j + dx[d], d);
				if (x) cost = min(cost, int(dir[d] != board[i][j]));
			}
			if (cost > 1) ok = 0;
			ans += cost;
		}

		cout << "Case #" << CASE << ": ";
		if (ok) cout << ans << endl;
		else cout << "IMPOSSIBLE" << endl;
	}


}