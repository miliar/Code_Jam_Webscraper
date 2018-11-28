#include <bits/stdc++.h>

using namespace std;

#define mod 1000000007

char ss[10][30];
int m, n;
int key, res;
int col[10];
int ch[100][26];
int it;

int Map[256];

void init() {
	for (int i = 0; i < 26; i++) {
		Map[i + 'A'] = i;
	}
}

int solve(int flag) {

	it = 1;
	memset(ch[it], 0, sizeof(ch[it]));
	it++;

	for (int i = 0; i < m; i++) {
		if (col[i] != flag) continue;

		//cout << i << ' ';
		
		int cur = 1;

		for (int j = 0; ss[i][j]; j++) {
			int c = Map[ss[i][j]];

			if (!ch[cur][c]) {
				ch[cur][c] = it;
				memset(ch[it], 0, sizeof(ch[it]));
				it++;
			}
			
			cur = ch[cur][c];
		}		
	}	

	//cout << endl;

	//cout << it - 1 << endl;

	return it - 1;
}

void dfs(int id, int sta) {
	if (id == m) {
		if (sta == (1 << n) - 1) {
			int cnt = 0;
			for (int i = 0; i < n; i++) {
				cnt += solve(i);		
			}		

			if (cnt > key) {
				key = cnt;
				res = 1;
			}
			else if (cnt == key) {
				res++;
			}
		}

		return;
	}	

	for (int i = 0; i < n; i++) {
		col[id] = i;
		dfs(id + 1, sta | (1 << i));
	}
}

int main() {
	int test;
	init();
	scanf("%d", &test);

	for (int cas = 1; cas <= test; cas++) {
		scanf("%d%d", &m, &n);

		for (int i = 0; i < m; i++) {
			scanf("%s", ss[i]);
		}		

		key = 0;		
		memset(col, -1, sizeof(col));
	
		dfs(0, 0);

		printf("Case #%d: %d %d\n", cas, key, res);			
	}
	return 0;
}
