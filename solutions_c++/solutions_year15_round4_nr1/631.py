#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int solve() {
	int r,c;
	cin >> r >> c;
	vector<string> v(r);
	for(auto &s: v) cin >> s;

	//cerr << r << " " << c << endl;
	vector<int> R(r,false),C(c,false);
	for(int i=0; i < r; i++) {
		for(int j=0; j < c; j++) {
			char c = v[i][j];
			if(c == '.') continue;
			R[i]++;
			C[j]++;
		}
	}
	int res = 0;
	for(int i=0; i < r; i++) {
		for(int j=0; j < c; j++) {
			int dx,dy;
			char ch = v[i][j];
			if(ch == '.') continue;
			if(ch == '>') { dx = 0; dy= 1;}
			if(ch == 'v') { dx = 1; dy= 0;}
			if(ch == '^') { dx =-1; dy= 0;}
			if(ch == '<') { dx = 0; dy=-1;}

			//cerr << i << " " << j << " " << dx << " " << dy << endl;
			int x=i, y=j;
			x+=dx; y+=dy;
			while(x < r && x >= 0 && y < c && y >= 0) {
				if(v[x][y] != '.') break;
				x+=dx; y+=dy;
			}
			if(x < r && x >= 0 && y < c && y >= 0) {}
			else {
				if(R[i] == 1 && C[j] == 1) {
					cout << "IMPOSSIBLE" << endl; 
					return 0;
				}
				res++;
			}
		}
	}
	cout << res << endl;
}

int main(void) {
	ios::sync_with_stdio(false);

	int T;
	cin >> T;
	for(int t=1; t <= T; t++) {
		cout << "Case #"<< t << ": "; 
		solve();
	}
	return 0;
}