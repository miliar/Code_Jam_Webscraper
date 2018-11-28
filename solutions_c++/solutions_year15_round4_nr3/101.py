//Template
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <climits>
#include <cmath>
#include <utility>
#include <set>
#include <map>
#include <queue>
#include <ios>
#include <iomanip>
#include <ctime>
#include <numeric>
#include <functional>
#include <fstream>
#include <string>
#include <vector>
#include <bitset>
#include <cstdarg>
#include <complex>
using namespace std;

typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef long double ld;
#define pair(x, y) make_pair(x, y)
#define runtime() ((double)clock() / CLOCKS_PER_SEC)

inline int read() {
	static int r, sign;
	static char c;
	r = 0, sign = 1;
	do c = getchar(); while (c != '-' && (c < '0' || c > '9'));
	if (c == '-') sign = -1, c = getchar();
	while (c >= '0' && c <= '9') r = r * 10 + (int)(c - '0'), c = getchar();
	return sign * r;
}

template <typename T>
inline void print(T *a, int n) {
	for (int i = 1; i < n; ++i) cout << a[i] << " ";
	cout << a[n] << endl;
}
#define PRINT(_l, _r, _s, _t) { cout << #_l #_s "~" #_t #_r ": "; for (int _i = _s; _i != _t; ++_i) cout << _l _i _r << " "; cout << endl; }

#define NODE 100000
#define EDGE 5000000
struct edge {
	int next, node;
	int w;
} e[EDGE << 1 | 1];
int head[NODE + 1], tot = 1;

inline void addedge(int a, int b, int w) {
	e[++tot].next = head[a];
	head[a] = tot, e[tot].node = b, e[tot].w = w;
	e[++tot].next = head[b];
	head[b] = tot, e[tot].node = a, e[tot].w = 0;
//	cout << a << " " << b << " " << w << endl;
}

const int INFI = 123456789;

int d[NODE + 1], q[NODE + 1], S, T;

inline bool bfs() {
	int h = 0, t = 0;
	for (int i = S; i <= T; ++i) d[i] = 0;
	q[t++] = S, d[S] = 1;
	while (h < t) {
		int cur = q[h++];
		for (int i = head[cur]; i; i = e[i].next) {
			if (!e[i].w) continue;
			int node = e[i].node;
			if (d[node]) continue;
			d[node] = d[cur] + 1;
			q[t++] = node;
		}
	}
	return d[T] != 0;
}

int dfs(int x, int inflow) {
	if (x == T) return inflow;
	int ret = inflow, flow;
	for (int i = head[x]; i; i = e[i].next) {
		if (!e[i].w) continue;
		int node = e[i].node;
		if (d[node] != d[x] + 1) continue;
		flow = dfs(node, min(ret, e[i].w));
		if (!flow) continue;
		ret -= flow, e[i].w -= flow, e[i ^ 1].w += flow;
		if (!ret) break;
	}
	if (ret == inflow) d[x] = -1;
	return inflow - ret;
}

inline int maxFlow() {
	int ret = 0;
	while (bfs())
		ret += dfs(S, INFI);
	return ret;
}

#define N 200
int Cases, n, m;
map<string, int> word;
map<uint, int> wordStat;
string sentence[N + 1];
vector<uint> sw[N + 1];

void parse(string &s, vector<uint> &a, int mode) {
	stringstream ss(s);
	string w;
	a.clear();
	while (ss >> w) {
		auto it = word.find(w);
		if (it != word.end()) {
			wordStat[it->second] |= mode;
			a.push_back(it->second);
		} else {
			uint num = word.size() + 1;
			word[w] = num;
			wordStat[num] = mode;
			a.push_back(num);
		}
	}
}

int main(int argc, char *argv[]) {
#ifdef KANARI
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	
	int Case = 0;
	cin >> Cases;
	while (Cases--) {
		cin >> n;
		getline(cin, sentence[0]);
		for (int i = 1; i <= n; ++i)
			getline(cin, sentence[i]);
		
		word.clear();
		wordStat.clear();
		parse(sentence[1], sw[1], 1);
		parse(sentence[2], sw[2], 2);
		for (int i = 3; i <= n; ++i)
			parse(sentence[i], sw[i], 0);
		
		S = 0, T = word.size() * 2 + n + 1;
		memset(head, 0, sizeof head);
		tot = 1;
		
		int ans = 0;
//		for (auto &x : word)
//			cout << x.first << " " << x.second << " " << wordStat[x.second] << endl;
		for (auto &x : word) {
			int stat = wordStat[x.second];
			if (stat == 0 || stat == 1) {
				addedge(n + x.second, T, 1);
//				cout << "n+" << x.second << " T : 1" << endl;
			}
			if (stat == 0 || stat == 2) {
				addedge(S, n + word.size() + x.second, 1);
//				cout << "S n+word+" << x.second << " : 1" << endl;
			}
			if (stat == 3) {
				++ans;
			}
			if (stat == 0) --ans;
		}
		for (int i = 3; i <= n; ++i) {
			for (auto &x : sw[i]) {
				int stat = wordStat[x];
				if (stat == 0 || stat == 1) {
					addedge(i, n + x, INFI);
//					cout << i << " n+" << x << " : INFI" << endl;
				}
				if (stat == 0 || stat == 2) {
					addedge(n + word.size() + x, i, INFI);
//					cout << "n+word+" << x << " " << i << " : INFI" << endl;
				}
			}
		}
		ans += maxFlow();
		
		printf("Case #%d: %d\n", ++Case, ans);
	}
	
	fclose(stdin);
	fclose(stdout);
	return 0;
}
