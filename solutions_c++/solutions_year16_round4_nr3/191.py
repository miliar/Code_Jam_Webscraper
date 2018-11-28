#include <bits/stdc++.h>
using namespace std;
#if defined(ILIKEGENTOO)
void E(){}template<class A,class...B>void E(A _,B...$){cerr<<' '<<_;E($...);}
#define E($...) E(#$,'=',$,'\n')
#else
#define E($...) ;
#endif
#define all(x) begin(x), end(x)
struct ${$(){ios_base::sync_with_stdio(false);cin.tie(nullptr);}}$;

const int R = 100;
char field[R+1][R+1];
vector<int> love;
int r, c;

bool vis[2][R + 1][R + 1];

bool dfs(int dir, int ri, int ci, int v) {
	//E(dir, ri, ci, v, "dfs");
	if (vis[dir][ri][ci])
		return true;
	vis[dir][ri][ci] = true;
	//E(dir, ri, ci, v, "before");
	if (dir == 0 && ri == 0 && v != ci && love[v] != ci)
		return false;
	if (dir == 0 && ri == r && v != 2 * c + r - 1 - ci && love[v] != 2 * c + r - 1 - ci)
		return false;
	if (dir == 1 && ci == 0 && v != 2 * (c + r) - 1 - ri && love[v] != 2 * (c + r) - 1 - ri)
		return false;
	if (dir == 1 && ci == c && v != c + ri && love[v] != c + ri)
		return false;
	//E(dir, ri, ci, v, "after");
	if (dir == 0 && ri > 0) {
		if (!dfs(1, ri - 1, ci + (field[ri - 1][ci] == '/'), v)) return false;
	}
	if (dir == 0 && ri < r) {
		if (!dfs(1, ri, ci + (field[ri][ci] == '\\'), v)) return false;
	}
	if (dir == 1 && ci > 0) {
		if (!dfs(0, ri + (field[ri][ci - 1] == '/'), ci - 1, v)) return false;
	}
	if (dir == 1 && ci < c) {
		if (!dfs(0, ri + (field[ri][ci] == '\\'), ci, v)) return false;
	}
	//E(dir, ri, ci, v, "ok");
	return true;
}

bool goodfield() {
		//if (!strcmp(field[0], "//\\")) return false;
	/*
		E(field[0]);
		E(dfs(0, 0, 1, 1));
		//E(dfs(0, 0, 2, 2));
		return true;
	*/
	memset(vis, 0, sizeof(vis));
	for (int i = 0; i < c; ++i) {
		if (!dfs(0, 0, i, i))
			return false;
		if (!dfs(0, r, c - 1 - i, c + r + i))
			return false;
	}
	for (int i = 0; i < r; ++i) {
		if (!dfs(1, i, c, c + i))
			return false;
		if (!dfs(1, r - 1 - i, 0, 2 * c + r + i))
			return false;
	}
	//E("gf", true);
	return true;
}

bool rec(int ri, int ci) {
	for (int slai = 0; slai < 2; ++slai) {
		field[ri][ci] = slai ? '\\' : '/';
		bool ok;
		if (ci + 1 < c)
			ok = rec(ri, ci + 1);
		else if (ri + 1 < r)
			ok = rec(ri + 1, 0);
		else
			ok = goodfield();
		if (ok)
			return true;
	}
	return false;
}

void solve() {
	memset(field, 0, sizeof(field));
	cin >> r >> c;
	love.resize(2 * (r + c));
	for (int i = 0; i < r + c; ++i) {
		int a, b;
		cin >> a >> b;
		--a;
		--b;
		love[a] = b;
		love[b] = a;
	}
	if (rec(0, 0)) {
		for (int i = 0; i < r; ++i)
			cout << field[i] << '\n';
	} else {
		cout << "IMPOSSIBLE\n";
	}
}

int main() {
	int tc;
	cin >> tc;
	for (int ti = 1; ti <= tc; ++ti) {
		cout << "Case #" << ti << ":\n";
		solve();
	}
	return 0;
}

