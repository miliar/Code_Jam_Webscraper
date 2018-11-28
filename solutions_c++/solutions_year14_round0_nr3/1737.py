#include <set>
#include <queue>
#include <vector>
#include <string>
#include <iomanip> 
#include <iostream>
#include <iterator>
#include <algorithm>
using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;

struct GG{
	int R, C;
	VS mm;
	VS mc;

	GG(int R, int C) : R(R), C(C), mm(R, string(C, '.')), mc(R, string(C, 'x')) {

	}

	void fillMinesCount(){
		for (int r = 0; r < R; r++){
			for (int c = 0; c < C; c++){
				mc[r][c] = minesCount(r, c);				
			}
		}
	}
	bool inside(int r, int c) const {
		return 0 <= r && r < R && 0 <= c && c < C;
	}
	int minesCount(int r, int c){
		int res = 0;
		for (int nr = max(0, r - 1); nr < min(R, r + 2); nr++){
			for (int nc = max(0, c - 1); nc < min(C, c + 2); nc++){
				if (mineAt(nr, nc)){
					res++;
				}
			}
		}
		return res;		
	}
	bool mineAt(int r, int c) const{
		return mm[r][c] == '*';
	}
	void setMine(int r, int c){
		mm[r][c] = '*';
	}
	void setNotMine(int r, int c){
		mm[r][c] = '.';
	}
	bool tryClick(int sr, int sc, int expectedOpened){
		if (mineAt(sr, sc)){
			return false;
		}
		if (mc[sr][sc] != 0){
			return expectedOpened == 1;
		}
		queue<int> Q;
		VS was(R, string(C, '\0'));
		Q.push(sr);
		Q.push(sc);
		was[sr][sc] = 1;
		int opened = 1;
		while (!Q.empty()){
			int r = Q.front(); Q.pop();
			int c = Q.front(); Q.pop();
			for (int nr = max(0, r - 1); nr < min(R, r + 2); nr++){
				for (int nc = max(0, c - 1); nc < min(C, c + 2); nc++){
					if (nr == r && nc == c){
						continue;
					}
					if (was[nr][nc]){
						continue;
					}
					if (mineAt(nr, nc)){
						throw 42;
					}
					opened += 1;
					was[nr][nc] = 1;
					if (mc[nr][nc] != 0){
						continue;
					}
					Q.push(nr);
					Q.push(nc);					
				}
			}
		}
		return opened == expectedOpened;
	}	
	void print(int sr, int sc, int M){
		//cout << R << ' ' << C << ' ' << M << ' ' << R * C - M << endl;
		for (int r = 0; r < R; r++){
			for (int c = 0; c < C; c++){
				if (r == sr && c == sc){
					cout << 'c';
				}
				else{
					cout << mm[r][c];
				}
			}
			cout << endl;
		}
		cout << endl;
	}
};


bool gg(int R, int C, int M){
	LL sz = R * C;
	GG gg(R, C);
	for (LL m = 0; m < ((LL)1 << sz); m++){
		int mines = 0;
		for (LL r = 0, k = 0; r < R; r++){
			for (LL c = 0; c < C; c++){
				bool mine = m & ((LL)1 << (k++));
				if (mine){
					mines++;
					gg.setMine(r, c);
				}
				else{
					gg.setNotMine(r, c);
				}
			}
		}		
		if (mines != M){
			continue;
		}
		gg.fillMinesCount();

		for (int r = R - 1; r >= 0; r--){
			for (int c = C - 1; c >= 0; c--){
				if (gg.mineAt(r, c)){
					continue;
				}
				if (gg.tryClick(r, c, sz - mines)){
					gg.print(r, c, M);
					return true;
				}
			}
		}
	}
	return false;
}
void dbg(){	
	for (int R = 1; R <= 30; R++){
		for (int C = 1; C <= 30; C++){
			if (R * C <= 20){
				for (int M = 0; M < (R * C); M++){
					if (!gg(R, C, M)){
						//cout << "!" << R << ' ' << C << ' ' << M << ' ' << R * C - M <<endl;
					}
				}
			}
		}
	}
}
void solve(){
	int R, C, M;
	cin >> R >> C >> M;
	if (!gg(R, C, M)){
		cout << "Impossible" << endl;
	}	
}
int main(){
#if 1
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif	
	//dbg();
	//return 0;
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++){
		cout << "Case #" << i << ": " << endl;
		solve();
	}
	return 0;
}