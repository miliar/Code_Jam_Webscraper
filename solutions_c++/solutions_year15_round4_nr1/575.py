#include <iostream>
using namespace std;

int r, c;
char g[100][100];

void solve(){
	cin >> r >> c;
	for(int i=0; i<r; i++) for(int j=0; j<c; j++) cin >> g[i][j];
	int ans = 0;
	for(int i=0; i<r; i++) for(int j=0; j<c; j++){
		if(g[i][j] == '.') continue;
		if(g[i][j] == '^'){
			int q;
			q = 0; for(int x=0; x<i; x++) if(g[x][j] != '.') q++;
			if(q > 0) continue;
			q = 0;
			for(int x=i+1; x<r; x++) if(g[x][j] != '.') q++;
			for(int x=0; x<j; x++) if(g[i][x] != '.') q++;
			for(int x=j+1; x<c; x++) if(g[i][x] != '.') q++;
			if(q == 0) {cout << "IMPOSSIBLE"; return;}
			ans++;
			continue;
		}
		if(g[i][j] == '>'){
			int q;
			q = 0; for(int x=j+1; x<c; x++) if(g[i][x] != '.') q++;
			if(q > 0) continue;
			q = 0;
			for(int x=i+1; x<r; x++) if(g[x][j] != '.') q++;
			for(int x=0; x<j; x++) if(g[i][x] != '.') q++;
			for(int x=0; x<i; x++) if(g[x][j] != '.') q++;
			if(q == 0) {cout << "IMPOSSIBLE"; return;}
			ans++;
			continue;
		}
		if(g[i][j] == 'v'){
			int q;
			q = 0; for(int x=i+1; x<r; x++) if(g[x][j] != '.') q++;
			if(q > 0) continue;
			q = 0;
			for(int x=0; x<i; x++) if(g[x][j] != '.') q++;
			for(int x=0; x<j; x++) if(g[i][x] != '.') q++;
			for(int x=j+1; x<c; x++) if(g[i][x] != '.') q++;
			if(q == 0) {cout << "IMPOSSIBLE"; return;}
			ans++;
			continue;
		}
		if(g[i][j] == '<'){
			int q;
			q = 0; for(int x=0; x<j; x++) if(g[i][x] != '.') q++;
			if(q > 0) continue;
			q = 0;
			for(int x=i+1; x<r; x++) if(g[x][j] != '.') q++;
			for(int x=0; x<i; x++) if(g[x][j] != '.') q++;
			for(int x=j+1; x<c; x++) if(g[i][x] != '.') q++;
			if(q == 0) {cout << "IMPOSSIBLE"; return;}
			ans++;
			continue;
		}
	}
	cout << ans;
}

int main(){
	int t; cin >> t;
	for(int i=1; i<=t; i++){
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
	
	return 0;
}
