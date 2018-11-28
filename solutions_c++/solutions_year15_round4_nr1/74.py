#include<stdio.h>
#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
#include<memory.h>
#include<map>
#include<set>
#include<queue>
#include<list>
#include<sstream>
#define mp make_pair
#define pb push_back      
#define F first
#define S second
#define SS stringstream
#define sqr(x) ((x)*(x))
#define m0(x) memset(x,0,sizeof(x))
#define m1(x) memset(x,63,sizeof(x))
#define CC(x) cout << (x) << endl
#define pw(x) (1ll<<(x))
#define M 1000000007
#define N 111111
using namespace std;
typedef pair<int,int> pt;

int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, 1, -1};

string dir = "^v><";

string s[111];

int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt++) {
		int n, m;
		cin >> n >> m;
		for (int i = 0; i < n; i++) cin >> s[i];

		int ans = 0;
		int bad = 0;

		for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) if (s[i][j] != '.') {
			int g = 0;
			int t = 0;

			for (int d = 0; d < 4; d++) {
				int x = i + dx[d];
				int y = j + dy[d];

				while (0 <= x && x < n && 0 <= y && y < m) {
					if (s[x][y] != '.') break;
					x += dx[d];
					y += dy[d];
				}
				if (0 <= x && x < n && 0 <= y && y < m) continue;

				g++;
				if (dir.find(s[i][j]) == d) t = 1;
			}	
			if (g == 4) bad = 1;
			ans += t;
		}

		cout << "Case #" << tt << ": ";
		if (bad) puts("IMPOSSIBLE"); else cout << ans << endl;

	}
	return 0;
}