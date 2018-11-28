#include <bits/stdc++.h>
using namespace std;
int n, m;

string s[105];

void makeGrid(int msk) {
	int ind = 0;
	for (int i = 0; i < n; i++) {
		s[i] = "";
		for (int j = 0; j < m; j++)
			if (msk & (1 << (ind++)))
				s[i] += "/";
			else
				s[i] += "\\";
	}

}

vector<int> g[2][100000];
map<int, int> love;
void addEdge(int hor, int ver) {
	g[0][ver].push_back(hor);
	g[1][hor].push_back(ver);
}

vector<pair<int, int> > component;
int vis[2][100005];
int vis_id;

bool isEdge(int node, int type) {
	// ver
	if (type == 0)
		return node < n || (node >= m * n);
	else
		return node < m || (node >= m * n);
}

void dfs(int node, int type) {
	if (vis[type][node] == vis_id)
		return;
	if (isEdge(node, type))
		component.push_back(make_pair(node, type));
	vis[type][node] = vis_id;
	for (int i = 0; i < int(g[type][node].size()); i++) {
		int child = g[type][node][i];
		dfs(child, 1 - type);
	}
}

string print() {
	string ret = "";
	for (int i = 0; i < n; i++)
		ret += s[i] + "\n";
	return ret;
}

int get(pair<int, int> node) {
	if (node.second == 0) {
		if (node.first < n)
			return n - node.first - 1 + m + m + n + 1;
		else
			return node.first % n + m + 1;
	}
	else {
		if (node.first < m)
			return node.first + 1;
		else
			return m - node.first % m + n + m;
	}
}


bool ok(int msk) {
	makeGrid(msk);
	int numVer = n * (m + 1);
	int numHor = m * (n + 1);
	for (int i = 0; i < int(numVer); i++)
		g[0][i].clear();
	for (int i = 0; i < int(numHor); i++)
		g[1][i].clear();

	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			if (s[i][j] == '/') {
				addEdge(i * m + j, j * n + i);
				addEdge((i + 1) * m + j, (j + 1) * n + i);
			}
			else {
				addEdge(i * m + j, (j + 1) * n + i);
				addEdge((i + 1) * m + j, j * n + i);
			}

	for (int i = 0; i < n; i++) {
		component.clear();
		vis_id++;
		dfs(i, 0);
		if (component.size() != 2)
			return false;
		if (love[get(component[0])] != get(component[1]))
			return false;
	}
	for (int i = n * m; i < n * (m + 1); i++) {
		component.clear();
		vis_id++;
		dfs(i, 0);
		if (component.size() != 2)
			return false;
		if (love[get(component[0])] != get(component[1]))
			return false;
	}



	for (int i = 0; i < m; i++) {
		component.clear();
		vis_id++;
		dfs(i, 1);
		if (component.size() != 2)
			return false;
		if (love[get(component[0])] != get(component[1]))
			return false;
	}
	for (int i = n * m; i < m * (n + 1); i++) {
		component.clear();
		vis_id++;
		dfs(i, 1);
		if (component.size() != 2)
			return false;
		if (love[get(component[0])] != get(component[1]))
			return false;
	}

	return true;
}


int main() {
	ios::sync_with_stdio(false);
		freopen("/home/ahmed/Desktop/Round 2/C/C-small-attempt0.in", "r", stdin);
		freopen("/home/ahmed/Desktop/Round 2/C/C-small-attempt0.out", "w", stdout);

	int t; scanf("%d", &t);
	int id = 1;
	while (t--) {
		scanf("%d%d", &n, &m);
		vector<int> v;
		for (int i = 0; i < 2 * (n + m); i++) {
			int x; scanf("%d", &x);
			v.push_back(x);
		}
		love.clear();
		for (int i = 0; i < n + n + m + m; i += 2)
			love[v[i]] = v[i + 1], love[v[i + 1]] = v[i];

		int tot = n * m;
		string ans = "IMPOSSIBLE\n";
		for (int msk = 0; msk < (1 << tot); msk++)
			if (ok(msk)) {
				ans = print();
				break;
			}
		cout << "Case #" << id++ << ":\n";
		cout << ans;
	}

	return 0;
}

