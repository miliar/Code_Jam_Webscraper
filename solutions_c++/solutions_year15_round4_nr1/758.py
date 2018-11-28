#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef pair <LL, LL> PII;
const int MAXN = 1e3, INF = 1e9 + 7;
const int e[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

char mp[MAXN][MAXN];
int n, m; 

int check(int r, int c){
	for (int k = 0; k < 4; k++){
		int u = r, v = c;
		for (;;){
			u+=e[k][0]; v+=e[k][1];
			if (u < 0 || u >= n || v < 0 || v >= m) break;
			if (mp[u][v] != '.') return true;			
		}
	}
	return false;
}

int solve(){	
	set <PII> u;
	for (int i=0; i<n; i++){
		int j = 0;
		while (j < m && mp[i][j] == '.') j++;
		if (j == m) continue;
		
		if (!check(i, j)) return -1;	// only one			
		if (mp[i][j] == '<') u.insert(PII(i, j));
		
		j = m-1;
		while (j > 0 && mp[i][j] == '.') j--;
		if (mp[i][j] == '>') u.insert(PII(i, j));	
	}
	for (int j=0; j<m; j++){
		int i = 0;
		while (i < n  && mp[i][j] == '.') i++;
		if (i == n) continue;
		
		if (!check(i, j)) return -1;
		if (mp[i][j] == '^') u.insert(PII(i, j));
		
		i = n-1;
		while (i > 0 && mp[i][j] == '.') i--;
		if (mp[i][j] == 'v') u.insert(PII(i, j));		
	}
	/*
	for (auto &x : u){
		cout << x.first << ' ' << x.second << endl;
	}
	cout << endl;
	*/
	return u.size();
}

int main(){
	int t; scanf("%d", &t);
	for (int cas = 1; cas <= t; cas++){
		printf("Case #%d: ", cas);
		scanf("%d%d", &n, &m);
		for (int i=0; i<n; i++) scanf("%s", mp[i]);
		int rst = solve();
		if (rst == -1) puts("IMPOSSIBLE");		
		else printf("%d\n", rst);		
	}
	return 0;
}