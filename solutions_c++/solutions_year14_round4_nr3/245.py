#include <functional>
#include <algorithm>
#include <stdexcept>
#include <iostream>
#include <sstream>
#include <fstream>
#include <complex>
#include <numeric>
#include <iomanip>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <cctype>
#include <vector>
#include <string>
#include <bitset>
#include <cmath>
#include <queue>
#include <stdio.h>
#include <stack>
#include <ctime>
#include <list>
#include <map>
#include <set>
#include <assert.h>
#define REP(i,n) for(int i=0;i<n;i++)
#define TR(i,x) for(typeof(x.begin()) i=x.begin();i!=x.end();i++)
#define ALL(x) x.begin(),x.end()
#define SORT(x) sort(ALL(x))
#define CLEAR(x) memset(x,0,sizeof(x))
#define FILL(x,c) memset(x,c,sizeof(x))

using namespace std;

const double eps = 1e-8;
const double pi = acos(-1);

#define PB push_back
#define MP make_pair

typedef map<int,int> MII;
typedef map<string,int> MSI;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<long double> VD;
typedef pair<int,int> PII;
typedef long long int64;
typedef long long ll;
typedef unsigned int UI;
typedef long double LD;
typedef unsigned long long ULL;

const int N = 600;
const int INF = 0x3F3F3F3F;

int img[N][N];
int dis[N][N];

bool vis[N][N];

int dx[8] = {0, 0, -1, 1, -1, -1, 1, 1};
int dy[8] = {-1, 1, 0, 0, 1, -1, 1, -1};

void solve(int nowCase) {
	int w, h, b;
	cin >> w >> h >> b;
	CLEAR(img);
	REP(ii, b) {
		int x0, x1, y0, y1;
		cin >> x0 >> y0 >> x1 >> y1;
		for (int i = x0; i <= x1; ++i) {
			for (int j = y0; j <= y1; ++j) {
				img[i][j] = 1;
			}
		}
	}
	REP(i, w) REP(j, h) img[i][j] ^= 1;
	REP(i, w) REP(j, h) { dis[i][j] = INF; vis[i][j] = false;}

	priority_queue< pair<int, PII> > q;
	REP(j, h) {
		dis[0][j] = img[0][j];
		q.push(MP(-img[0][j], MP(0, j)));
	}

	while (q.size()) {
		PII at = q.top().second;
		q.pop();
		if (vis[at.first][at.second]) continue;
		vis[at.first][at.second] = true;
		REP(dir, 8) {
			int nx = at.first + dx[dir];
			int ny = at.second + dy[dir];
			if (nx < 0 || ny < 0 || nx >= w || ny >= h) continue;
			if (dis[at.first][at.second] + img[nx][ny] < dis[nx][ny]) {
				dis[nx][ny] = dis[at.first][at.second] + img[nx][ny];
				q.push(MP(-dis[nx][ny], MP(nx, ny)));
			}
		}
	}

	int ans = INF;
	REP(j, h) ans = min(ans, dis[w - 1][j]);
	cout << "Case #" << nowCase << ": " << ans << endl;
}

int main() {
	int T;
	cin >> T;
	for (int nowCase = 1; nowCase <= T; ++nowCase) {
		solve(nowCase);
	}
	return 0;
}