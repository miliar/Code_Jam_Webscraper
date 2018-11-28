#include <bits/stdc++.h>
using namespace std;

#define size(v) int(v.size())
#define MOD 1000003
#define INF 1e9
#define ulint unsigned long long int
#define lint long long int
#define mp make_pair
#define pb push_back
#define pop pop_back
#define st first
#define nd second
#define all(X) (X).begin(),(X).end()
#define E12 1000000000000

struct min_heap_comparator{
	bool operator()(const long& a,const long& b) const{
		return a>b;
	}
};
#define mh_min(X) make_heap(all(X), min_heap_comparator());
#define poph_min(X) {pop_heap(all(X), min_heap_comparator()); (X).pop();}
#define pushh_min(X, Y) {(X).pb(Y); push_heap(all(X), min_heap_comparator());}
#define sorth_min(X) sort_heap(all(X), min_heap_comparator());

#define mh_max(X) make_heap(all(X));
#define poph_max(X) {pop_heap(all(X)); (X).pop();}
#define pushh_max(X, Y) {(X).pb(Y); push_heap(all(X));}
#define sorth_max(X) sort_heap(all(X));

int x[] = {0, 1, 0, -1};
int y[] = {1, 0, -1, 0};

int main(void){
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t){
		int R, C;
		cin >> R >> C;
		vector<string> mapa(R);
		for (int i = 0; i < R; ++i){
			cin >> mapa[i];
		}
		bool possivel = true;
		int cont = 0;
		for (int i = 0; i < R; ++i){
			for (int j = 0; j < C; ++j){
				int aux = -1;
				switch (mapa[i][j]) {
					case '>': aux = 0; break;
					case 'v': aux = 1; break;
					case '<': aux = 2; break;
					case '^': aux = 3; break;
				}
				if (aux == -1) continue;
				int x1 = i + x[aux];
				int y1 = j + y[aux];
				bool ok = false;
				while (x1 >= 0 && x1 < R && y1 >= 0 && y1 < C){
					if (mapa[x1][y1] != '.'){
						ok = true;
						break;
					}
					x1 += x[aux];
					y1 += y[aux];
				}
				if (!ok) {
					possivel = false;
					for (int l = 0; l < 4; ++l){
						if (l == aux) continue;
						int x2 = i + x[l];
						int y2 = j + y[l];
						bool ok2 = false;
						while (x2 >= 0 && x2 < R && y2 >= 0 && y2 < C){
							if (mapa[x2][y2] != '.'){
								ok2 = true;
								break;
							}
							x2 += x[l];
							y2 += y[l];
						}
						if (ok2){
							cont ++;
							possivel = true;
							break;
						}
					}
					if (!possivel) break;
				}
			}
			if (!possivel) break;
		}
		if (possivel){
			cout << "Case #" << t+1 << ": " << cont << endl;
		} else 
			cout << "Case #" << t+1 << ": IMPOSSIBLE" << endl;
	}
	return 0;
}
