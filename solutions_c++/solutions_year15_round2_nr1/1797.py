#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cstring>
#include <queue>
using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REV(i,a,b) for(int i=(a);i>=(b);i--)
#define mp make_pair
#define pb push_back
#define oo 1e9
#define eps 1e-9
#define PI 3.14159265358979323846264338327950
#define MAX 2001
#define sz(v) (int)v.size()
#define all(c) (c).begin(),(c).end()
#define rall(c) (c).rbegin(),(c).rend()
#define show(x) cerr<<#x<<" = "<<x<<endl;
#define mem(s,v) memset(s,v,sizeof(s))
#define ppc(x) __builtin_popcount((x))
#define iter(it,s) for (__typeof(s.begin()) it = s.begin(); it != s.end(); it++)

typedef long long ll;
typedef vector<int> vi;
typedef vector<bool> vb;
typedef vector<double> vd;
typedef vector<string> vs;
typedef pair<int, int> pi;
typedef vector<pi> vpi;

int dx[] = { 0, 0, 1, -1 };
int dy[] = { 1, -1, 0, 0 };

int a;
int rv(int x) {
	ll r = 0;
	while (x)
		r *= 10, r += x % 10, x /= 10;
	return r;
}


bool vis[1000007];
int bfs() {
	mem(vis, 0);
	queue<int> q;
	q.push(0);
	vis[0] = 1;
	int c, lvl = 0 , r;

	while (!q.empty()) {
		int si = sz(q);
		while (si--) {
			c = q.front();
			q.pop();
			if (c == a)
				return lvl;
			r = rv(c);
			if(!vis[r] && r > c && r <= a)
				q.push(r) , vis[r] = 1;
			if(!vis[c + 1])
				q.push(c + 1) , vis[c + 1] = 1;
		}
		lvl++;
	}
	return 0;
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("A-small-attempt0 (1).in", "rt", stdin);
	freopen("o.txt", "wt", stdout);
#endif
	ios::sync_with_stdio(false);
	int t, cs = 1;
	cin >> t;
	while (t--) {
		cin >> a;
		cout << "Case #" << cs++ << ": " << bfs() << endl;
	}
	return 0;
}
