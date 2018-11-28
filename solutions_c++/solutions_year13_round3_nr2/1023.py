#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <fstream>
#include <list>
#include <set>
#include <climits>
#include <map>
#include <stack>
#include <queue>
#include <complex>
#include <cmath>
#include <sstream>
#include <deque>
#include <utility>
#include <bitset>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REV(i,b,a) for(int i=(a);i>=(b);i--)
#define mp make_pair
#define pb push_back
#define oo 1e9
#define MAX 2001
#define sz(v) (int)v.size()
#define all(c) (c).begin(),(c).end()
#define rall(c) (c).rbegin(),(c).rend()
#define iter(it,s) for(it=s.begin();it!=s.end();it++)
#define show(x) cerr<<#x<<" = "<<x<<endl;
#define mem(s,v) memset(s,v,sizeof(s))

typedef long long ll;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<string> vs;
typedef pair<int, int> pi;
typedef vector<pi> vpi;

int x, y;
bool vis[1000][1000];
int dx[] = { 0, 0, 1, -1 };
int dy[] = { 1, -1, 0, 0 };
string ds = "NSEW";

string BFS() {
	mem(vis , 0);
	queue<pair<pair<int, int> , string> > q;
	q.push(mp(mp(500, 500), ""));
	vis[500][500] = 1;
	int jmp = 1;
	while (!q.empty()) {
		int si = sz(q);
		while (si--) {
			int xx = q.front().first.first, yy = q.front().first.second;
			string s = q.front().second;
			q.pop();
			if (x == xx && y == yy)
				return s;
			FOR(i , 0 , 4) {
				int nx = xx + jmp * dx[i], ny = yy + jmp * dy[i];
				string ns = s + ds[i];
				if (!vis[nx][ny]) {
					vis[nx][ny] = 1;
					q.push(mp(mp(nx, ny), ns));
				}
			}
		}
		jmp++;
	}
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("B-small-attempt0.in", "rt", stdin);
		freopen("o.txt", "wt", stdout);
#endif
	int t, cs = 1;
	cin >> t;
	while (t--) {
		cin >> x >> y;
		x += 500, y += 500;
		cout << "Case #" << cs++ << ": " << BFS() << endl;
	}
	return 0;
}
