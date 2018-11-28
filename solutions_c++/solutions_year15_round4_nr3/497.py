#pragma comment(linker, "/STACK:640000000")
#include<iostream>
#include<cstdio>
#include<cassert>
#include<cstring>
#include<ctime>
#include<cstdlib>
#include<cmath>
#include<string>
#include<sstream>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<vector>
#include<bitset>
#include<algorithm>

#define pb push_back
#define ppb pop_back
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define sz(x) (int)(x).size()
#define ll long long
#define bit __builtin_popcountll
#define sqr(x) (x) * (x)
#define forit(it,S) for(__typeof((S).begin()) it = (S).begin(); it != (S).end(); it++)

using namespace std;

typedef pair<int, int> pii;

const double eps = 1e-9;
const double pi = acos(-1.0);

const int inf = (int)1e9;

struct edge {
	int c,f,to;
	edge() : c(0), f(0), to(0) {}
	edge(int c, int f, int to) : c(c), f(f), to(to) {}
};

map<string,int> words;
int ID;
int S = 0;
int T = 1;

int ptr[4444];
int lvl[4444];
int c[4444][4444];
int f[4444][4444];

bool bfs() {
	for (int i = 0; i < ID; i++) {
		lvl[i] = -1;
	}
	queue<int> q;
	q.push(S);
	lvl[S] = 0;
	while(!q.empty()) {
		int v = q.front(); q.pop();
		for (int i = 0; i < ID; i++) {
			if (c[v][i] - f[v][i] > 0 && lvl[i] == -1) {
				lvl[i] = lvl[v] + 1;
				q.push(i);
			}
		}
	}
	return lvl[T] != -1;
}

int dfs(int v, int flow) {
	if (flow == 0) return 0;
	if (v == T) return flow;
	for (int &i = ptr[v]; i < ID; i++) {
		if (lvl[i] != lvl[v] + 1) continue;
		if (int pushed = dfs(i,min(flow,c[v][i] - f[v][i]))) {
			f[v][i] += pushed;
			f[i][v] -= pushed;
			return pushed;
		}
	}
	return 0;
}

int mask[4444];
vector<int> id[22];
int ans;
int cur;

void dfs(int v) {
	if (v == 1) {
		ans = min(ans,cur);
		return;
	}
	vector<int> old;
	for (int i = 0; i < sz(id[v]); i++) {
		int pos = id[v][i];
		old.pb(mask[pos]);
		mask[pos] |= 1;
		if (mask[pos] == 3 && old[i] != 3) cur++;
	}
	dfs(v - 1);
	for (int i = 0; i < sz(id[v]); i++) {
		int pos = id[v][i];
		if (mask[pos] == 3 && old[i] != 3) cur--;
		mask[pos] = old[i];
	}
	for (int i = 0; i < sz(id[v]); i++) {
		int pos = id[v][i];
		mask[pos] |= 2;
		if (mask[pos] == 3 && old[i] != 3) cur++;
	}
	dfs(v - 1);
	for (int i = 0; i < sz(id[v]); i++) {
		int pos = id[v][i];
		if (mask[pos] == 3 && old[i] != 3) cur--;
		mask[pos] = old[i];
	}
}

void stupid() {	
	int n; scanf("%d\n",&n);
	words.clear();
	ans = inf;
	cur = 0;
	ID = 0;
	for (int i = 0; i < n; i++) {
		string s; getline(cin,s);
		stringstream ss(s);
		id[i].clear();
		while(ss >> s) {
			if (!words.count(s)) {
				mask[ID] = 0;
				words[s] = ID++;
			}
			if (i < 2) {
				mask[words[s]] |= (1 << i);
				if (mask[words[s]] == 3) cur++;
			} else {
				id[i].pb(words[s]);
			}
		}
		sort(all(id[i]));
		id[i].erase(unique(all(id[i])),id[i].end());
	}
	dfs(n - 1);
	cout << ans << endl;
}

/*void solve() {
	int n; scanf("%d\n",&n);
	ID = 2;	
	words.clear();	
	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < 2; j++) {
			c[i][j] = 0;
			f[i][j] = 0;
		}
	}
	for (int i = 0; i < n; i++) {
		string s; getline(cin,s);
		stringstream ss(s);
		vector<int> cur;
		while(ss >> s) {
			if (i < 2 || !words.count(s)) {
				words[s].pb(ID++);
				for (int i = 0; i <= ID; i++) {
					c[i][ID] = c[ID][i] = f[i][ID] = f[ID][i] = 0;
				}
			}
			if (i == 0) {
				c[S][words[s].back()] = 1;
			} else if (i == 1) {
				c[words[s].back()][T] = 1;
			} else if (sz(words[s]) == 1) {
				for (int j = 0; j < sz(words[s]); j++) {
					cur.pb(words[s][j]);
                    }
			}
		}
		for (int i = 0; i < sz(cur); i++) {
			for (int j = i + 1; j < sz(cur); j++) {
				c[cur[i]][cur[j]] = 1;
				c[cur[j]][cur[i]] = 1;
			}
		}
	}
	int flow = 0;
	forit(it,words) {
		if (sz(it -> second) == 2) {
			c[S][it -> second[0]] = 0;
			c[it -> second[1]][T] = 0;
			flow++;
		}
	}
	while(bfs()) {
		for (int i = 0; i < ID; i++) {
			ptr[i] = 0;
		}
		while(int pushed = dfs(S,inf)) {
			flow += pushed;
		}
	}
	cout << flow << endl;
}*/

int main() {
	#ifdef LOCAL
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	#endif

	int Cases; cin >> Cases;

	for (int Case = 1; Case <= Cases; Case++) {
		printf("Case #%d: ",Case);
		stupid();
	}
	
	return 0;
}
