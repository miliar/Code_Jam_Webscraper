#include<bits/stdc++.h>
using namespace std;
mt19937 gen;
vector<int> a[128];
int sz[128];
const int UU = 10000;
void dfs(int u) {
	sz[u] = 1;
	for(int v : a[u]) {
		dfs(v);
		sz[u] += sz[v];
	}
}
void sol() {
	int n, m;
	cin >> n;	
	string t;
	for(int i = 0; i <= n; ++i) a[i].clear();
	for(int i = 1, j; i <= n; ++i) {
		cin >> j;
		a[j].push_back(i);
	}
	cin >> t;
	cin >> m;
	vector<string> w(m);
	vector<int> c(m, 0);
	for(int i = 0; i < m; ++i) cin >> w[i];
	dfs(0);
	for(int tm = UU; tm--; ) {
		string s;
		int l = n;
		for(vector<int> now = a[0]; now.size(); --l) {
			int tt = uniform_int_distribution<int>(1, l)(gen), z = -1;
			for(int x : now) {
				tt -= sz[x];
				if(tt <= 0) {
					z = x;
					break;
				}
			}
			s += t[z-1];
			now.erase(find(now.begin(), now.end(), z));
			for(int x : a[z]) now.push_back(x);
			shuffle(now.begin(), now.end(), gen);
		}
		for(int j = 0; j < m; ++j)
			if(s.find(w[j]) != string::npos)
				++c[j];
	}
	for(int j = 0; j < m; ++j)
		cout << c[j] * 1.0 / UU << " \n"[j == m - 1];
}

int main() {
	int T;
	cin >> T;
	for(int i = 1; i <= T; ++i) {
		cout << "Case #" << i << ": ";
		sol();
	}
}
