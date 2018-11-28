#include <iostream>
#include <vector>

#define MAX 101

int R, C;
char map[MAX][MAX];
int tot[MAX][MAX];
std::pair<int, int> to[MAX][MAX];
bool vis[MAX][MAX];
bool tmp[MAX][MAX];

int rw[MAX];
int cl[MAX];

bool valid(int i, int j){
	return (0 <= i && i < R && 0 <= j && j < C);
}

void solve(int n){
	for(int i=0; i<MAX; ++i){
		cl[i] = false;
		rw[i] = false;
	}

	std::cin >> R >> C;
	for(int i=0; i<R; ++i){
		for(int j=0; j<C; ++j){
			std::cin >> map[i][j];
			if(map[i][j] != '.'){
				rw[i] += 1;
				cl[j] += 1;
			}
		}
	}
	
	for(int i=0; i<R; ++i){
		for(int j=0; j<C; ++j){
			vis[i][j] = false;
			tot[i][j] = 0;
			tmp[i][j] = false;
		}
	}
	
	for(int i=0; i<R; ++i){
		for(int j=0; j<C; ++j){
			if(vis[i][j] || map[i][j] == '.') continue;
			char c;
			
			int di, dj;
			int li = i, lj = i;
			int ni = i, nj = j;
			std::vector<std::pair<int, int> > v;
			int tcnt = 0;
			bool und = true;
			while(true){
				if(!valid(ni, nj)){
					tot[li][lj] += tcnt;
					break;
				}
				v.push_back(std::make_pair(ni, nj));
				if(vis[ni][nj]) {
					if(tmp[ni][nj]){
						und = false;
						break;
					}
					li = to[ni][nj].first;
					lj = to[ni][nj].second;
					tot[to[ni][nj].first][to[ni][nj].second] += tcnt;
					break;
				}
				if(map[ni][nj] != '.') vis[ni][nj] = true;
				tmp[ni][nj] = true;
				
				c = map[ni][nj];
			
				if(c == '^') di = -1, dj = 0, li = ni, lj = nj, ++tcnt;
				else if(c == '>') di = 0, dj = 1, li = ni, lj = nj, ++tcnt;
				else if(c == 'v') di = 1, dj = 0, li = ni, lj = nj, ++tcnt;
				else if(c == '<') di = 0, dj = -1, li = ni, lj = nj, ++tcnt;
				
				ni += di;
				nj += dj;
			}
			for(int i=0; i<v.size(); ++i){
				to[v[i].first][v[i].second] = std::make_pair(li, lj);
				if(und) tmp[v[i].first][v[i].second] = false;
			}
		}
	}
	int ans = 0;
	bool psb = true;
	for(int i=0; i<R; ++i){
		for(int j=0; j<C; ++j){
			if(tot[i][j] > 1) ++ans;
			if(tot[i][j] == 1){
				if(rw[i] < 2 && cl[j] < 2) {
					psb = false;
				}
				++ans;
			}
			//std::cout << tot[i][j] << " ";
		}
		//std::cout << std::endl;
	}
	if(!psb) std::cout << "Case #" << n << ": IMPOSSIBLE" << std::endl;
	else std::cout << "Case #" << n << ": " << ans << std::endl;
}

int main(){
	int T; 
	std::cin >> T;
	for(int i=0; i<T; ++i) solve(i+1);
}