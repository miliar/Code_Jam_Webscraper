#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <cstring>
using namespace std;

int req[500];
int add[500][222];

int trail[500];
bool wrong[1 << 22];
void dfs(int n, int i, int msk, vector<int> & cap) {
	if (i == n) {
		throw 0;
	}
	if (wrong[msk]) return; wrong[msk] = true;
	for (int nxt = 1; nxt <= n; nxt ++) {
		if (count(trail, trail + i, nxt) != 0) continue;
		if (cap[req[nxt]] == 0) continue;
		
		cap[req[nxt]] --;
		for (int id=1;id<=200;id++) {
			cap[id] += add[nxt][id];
		}
		
		trail[i] = nxt;
		dfs(n, i + 1, msk | (1<<nxt), cap);
		
		for (int id=1;id<=200;id++) {
			cap[id] -= add[nxt][id];
		}
		cap[req[nxt]] ++;
	}
}

int main() {
	int tc;
	cin >> tc;
	for (int casenr = 1; casenr <= tc; casenr ++) {
		memset(req,0,sizeof req);
		memset(add,0,sizeof add);
		memset(wrong,0,sizeof wrong);
		int nStart, n;
		cin >> nStart >> n;
		vector<int> cap (222, 0);
		for (; nStart > 0; nStart --) {
			int x;
			cin >> x;
			cap[x] ++;
		}
		for (int i = 1; i <= n; i ++) {
			cin >> req[i];
			int n_i;
			cin >> n_i;
			for (; n_i > 0; n_i --) {
				int x;
				cin >> x;
				add[i][x] ++;
			}
		}
		bool ok = false;
		try {
			dfs(n, 0, 0, cap);
		}
		catch (int e) {
			ok = true;
		}
		printf("Case #%d:", casenr);
		if (ok) {
			for (int i=0;i<n;i++)printf(" %d", trail[i]);
		}
		else {
			printf(" IMPOSSIBLE");
		}
		puts("");
	}
}
