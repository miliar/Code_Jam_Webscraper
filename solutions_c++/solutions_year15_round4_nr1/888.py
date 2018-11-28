#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
	int T;
	cin >> T;
	for(int t = 0; t < T; t++) {
		int R, C;
		cin >> R >> C;
		vector<string> v;
		for(int i = 0; i < R; i++) {
			string s;
			cin >> s;
			v.push_back(s);
		}
		vector<int> Rcnt, Ccnt;
		Rcnt.resize(R);
		Ccnt.resize(C);
		for(int i = 0; i < Rcnt.size(); i++) Rcnt[i] = 0;
		for(int i = 0; i < Ccnt.size(); i++) Ccnt[i] = 0;

		for(int i = 0; i < v.size(); i++) {
			for(int j = 0; j < v[i].size(); j++) {
				Rcnt[i] += (v[i][j] != '.');
				Ccnt[j] += (v[i][j] != '.');
			}
		}
		bool possible = true;
		for(int i = 0; i < v.size(); i++) {
			for(int j = 0; j < v[i].size(); j++) {
				if(v[i][j] != '.' && Rcnt[i] == 1 && Ccnt[j] == 1) {
//					cout << i << "," << j << endl;
					possible = false;
				}
			}
		}

		int res = 0;
		int dxy[] = {1,0,-1,0,1};
		for(int i = 0; i < v.size(); i++) {
			for(int j = 0; j < v[i].size(); j++) {
				if(v[i][j] != '.') {
					int d;
					if(v[i][j] == 'v')
						d = 0;
					else if(v[i][j] == '<')
						d = 1;
					else if(v[i][j] == '^')
						d = 2;
					else
						d = 3;
					int nx, ny;
					bool flg = true;
					ny = i + dxy[d];
					nx = j + dxy[d+1];

					while(0 <= nx && nx < C && 0 <= ny && ny < R) {
						if(v[ny][nx] != '.')
							flg = false;
						ny += dxy[d];
						nx += dxy[d+1];
					}
					if(flg) {
						res++;
					}
				}
			}
		}

		if(possible)
			cout << "Case #" << t + 1 << ": " << res << endl;
		else
			cout << "Case #" << t + 1 << ": " << "IMPOSSIBLE" << endl;;
	}
}
