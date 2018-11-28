#include <iostream>
#include <string>
#include <set>
using namespace std;

#define MAXM 8
#define MAXS 16
#define MAXN 4

int p[MAXM], M, N, RES, CANT;
string m[MAXM];
set<string> s[MAXN];

void dfs(int cur) {
	if (cur == M) {
		for (int i=0; i<N; i++) s[i].clear();
		for (int i=0; i<M; i++) {
			for (int j=0; j<=m[i].size(); j++) s[p[i]].insert(m[i].substr(0,j));
		}
		int tmp = 0;
		for (int i=0; i<N; i++) tmp += s[i].size();
		if (tmp > RES) {RES = tmp; CANT = 1;}
		else if (tmp == RES) CANT++;
	} else {
		for (int i=0; i<N; i++) {
			p[cur] = i;
			dfs(cur+1);
		}
	}
}

int main() {
	int t, T, i;
	
	cin >> T;
	for (t=1; t<=T; t++) {
		cin >> M >> N;
		
		for (i=0; i<M; i++) cin >> m[i];
		
		RES = -1;
		dfs(0);
		cout << "Case #" << t << ": " << RES << ' ' << CANT << endl;
	}

	return 0;
}
