#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
#define rep(i,s,e) for (int i=(s);i<(e);++i)
#define pb push_back
#define mk make_pair
#define fst first
#define snd second
#define all(x) (x).begin(),(x).end()
#define clr(x,y) memset(x,y,sizeof x)
#define contains(x,y) (x).find(y)!=(x).end()
#define endl "\n"

int dx[]={0,0,1,-1,1,-1,1,-1}, dy[]={-1,1,0,0,1,-1,-1,1};
const int mod = 1e9+7;

typedef complex<int> p;

string a[100];

int r, c;

bool free(int x, int y, int dx, int dy) {
  x += dx; y += dy;
  while (0 <= x && x < c && 0 <= y && y < r) {
    if (a[y][x] != '.') return false;
    x += dx; y += dy;
  }
  return true;
}

int main() {
	ios::sync_with_stdio(0);
	cout << fixed << setprecision(16);

	int t;
	cin >> t;
	for (int ti = 1; ti <= t; ti++) {
		cout << "Case #" << ti << ": ";
    cin >> r >> c;
    rep(y,0,r) cin >> a[y];
    bool impos = false; int change = 0;
    rep(y,0,r)
      rep(x,0,c)
        if (a[y][x] != '.') {
          int d = a[y][x] == '^' ? 0 : a[y][x] == 'v' ? 1 : a[y][x] == '>' ? 2 : 3;
          int freeCnt = 0;
          rep(i,0,4) freeCnt += free(x, y, dx[i], dy[i]);
          if (freeCnt == 4) impos = true;
          if (free(x, y, dx[d], dy[d])) change++;
        }
    if (impos)
      cout << "IMPOSSIBLE" << endl;
    else
      cout << change << endl;
	}
}
