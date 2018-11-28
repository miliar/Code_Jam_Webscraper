#include <iostream>
#include <sstream>
#include <ctime>
#include <cmath>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <vector>

using namespace std;

typedef long long LL;
typedef pair<int, int> PII;
typedef vector<int> VI;

#define REP(i, n) for(int i(0); (i)<(int)(n); i++)
#define FOR(i, a, b) for (int i(a); i <= int(b); i++)
#define ALL(x) x.begin(),x.end()
#define PB push_back
#define MP make_pair

const int N = 10005;
const int M = N * 10;
const int INF = 1000000009;
int n, m, S, T, d[N], f[N];
int t[M], p[M], c[M], o;
map<string, int> ID;

int getID(string s) {
	if (!ID.count(s))
		ID[s] = ID.size();
	return ID[s];
}

void addEdge(int i, int j, int cc) {
	p[++o] = j; c[o] = cc;
	t[o] = f[i]; f[i] = o;
	p[++o] = i; c[o] = 0;
	t[o] = f[j]; f[j] = o;
}

int Z;

int bfs() {
	for (int i = 1; i <= Z; i++) d[i] = 0;
	queue<int> Q;
	d[T] = 1;
	Q.push(T);
	while (!Q.empty()) {
		int i = Q.front();
		Q.pop();
		for (int j = f[i]; j; j = t[j])
		if (c[j ^ 1] && !d[p[j]]) {
			d[p[j]] = d[i] + 1;
			Q.push(p[j]);
		}
	}
	return d[S] > 0;
}

int dfs(int i, int flow) {
	if (i == T) return flow;
	int tmp, ans = 0;
	for (int j = f[i]; j; j = t[j])
	if (c[j] && d[p[j]] + 1 == d[i]) {
		tmp = dfs(p[j], min(flow, c[j]));
		flow -= tmp; ans += tmp;
		c[j] -= tmp; c[j^1] += tmp;
		if (!flow) break;
	}
	return ans;
}

void solve() {
	static int caseCnt = 0;
	printf("Case #%d: ", ++caseCnt);

	cin >> n;
	S = 1, T = 2;
	ID.clear();
	memset(f, 0, sizeof(f));
	o = 1;
	string s, t;
	getline(cin, s);
	for (int i = 1; i <= n; i++) {
		getline(cin, s);
		istringstream ssin(s);
		while (ssin >> t) {
			int x = getID(t);
			addEdge(i, n + x * 2 - 1, INF);
			addEdge(n + x * 2, i, INF);
		}
	}
	REP(i, ID.size()) addEdge(n + i + i + 1, n + i * 2 + 2, 1);
	int ans = 0;
	Z = (int)ID.size() * 2 + n;
	while (bfs()) ans += dfs(S, INF);
	cout << ans << endl;
}

int main() {
	int T = 1;
	scanf("%d", &T);
	while (T--) solve();
	return 0;
}

