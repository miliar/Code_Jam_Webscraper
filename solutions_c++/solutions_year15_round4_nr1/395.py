#include<iostream>
using namespace std;

char cc[4] = {'v', '^', '<', '>'};

string s[200];
int n, m;

int inb(int x, int y){
	return x>=0 && y>=0 && x<n && y<m;
}	

int dx(char c){
	if (c=='^') return -1;
	if (c=='v') return 1;
	return 0;
}

int dy(char c){
	if (c=='>') return 1;
	if (c=='<') return -1;
	return 0;
}	

int ok(int x, int y){
	int ddx = dx(s[x][y]);
	int ddy = dy(s[x][y]);
	while(1){
		x += ddx;
		y += ddy;
		if (!inb(x, y)) return 0;
		if (s[x][y] != '.') return 1;
	}
	return 1;
}	

int main(){
	ios::sync_with_stdio(0); cin.tie(0);
	int tt;
	cin >> tt;
	for (int _tt=0 ; _tt < tt ; _tt++){
		int J = 0, B = 0;
		cin >> n >> m;
		for (int i=0 ; i<n ; i++)
			cin >> s[i];
		for (int i=0 ; i<n ; i++)
		for (int j=0 ; j<m ; j++){
			if (s[i][j]=='.') continue;
			if (ok(i, j)) continue;
			for (int k=0 ; k<4 ; k++){
				s[i][j] = cc[k];
				if (ok(i, j)) break;
			}
			if (!ok(i, j)) B = 1;
			J++;
		}
		cout << "Case #" << _tt+1 << ": ";
		if (B) cout << "IMPOSSIBLE" << endl;
		else cout << J << endl;
	}
}
