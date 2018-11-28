#include <iostream>
#include <vector>
#include <cstdio>
#include <sstream>
#include <map>
#include <string>
#include <algorithm>
#include <queue>
#include <cmath>
#include <set>
using namespace std;

int solve(){
	int r,c;
	cin >> r >> c;
	vector<string> s(r);
	for(int i=0; i<r; i++){
		cin >> s[i];
	}

	vector<pair<int,int>> p;

	vector<set<int>> h(r), v(c);
	for(int i=0; i<r; i++){
		h[i].insert(-1);
		h[i].insert(c);
	}
	for(int i=0; i<c; i++){
		v[i].insert(-1);
		v[i].insert(r);
	}

	for(int i=0; i<r; i++){
		for(int j=0; j<c; j++){
			if(s[i][j] == '.') continue;
			else{
				p.push_back({i,j});
				h[i].insert(j);
				v[j].insert(i);
			}
		}
	}

	if(p.size() == 0) return 0;

	int ans = 0;
	map<pair<int,int>, bool> visit;
	for(int i=0; i<p.size(); i++){
		int pos_y = p[i].first;
		int pos_x = p[i].second;

		while(1){
			if(visit.find({pos_y, pos_x}) != visit.end()) break;
			visit[{pos_y, pos_x}] = true;

			int next_y, next_x;
			next_y = next_x = -1;

			int dir = -1;

			if(s[pos_y][pos_x] == '^'){
				dir = 0;
				auto itr = v[pos_x].lower_bound(pos_y);
				itr--;
				if(*itr >= 0){
					next_y = *itr;
					next_x = pos_x;
				}
			}else if(s[pos_y][pos_x] == '>'){
				dir = 1;
				auto itr = h[pos_y].lower_bound(pos_x);
				itr++;
				if(*itr < c){
					next_y = pos_y;
					next_x = *itr;
				}

			}else if(s[pos_y][pos_x] == 'v'){
				dir = 2;
				auto itr = v[pos_x].lower_bound(pos_y);
				itr++;
				if(*itr < r){
					next_y = *itr;
					next_x = pos_x;
				}

			}else if(s[pos_y][pos_x] == '<'){
				dir = 3;
				auto itr = h[pos_y].lower_bound(pos_x);
				itr--;
				if(*itr >= 0){
					next_y = pos_y;
					next_x = *itr;
				}
			}

			if(next_y < 0 || next_x < 0){
				ans++;
				for(int k=1; k<4; k++){
					int dir__ = (dir + k)%4;

					if(dir__ == 0){
						auto itr = v[pos_x].lower_bound(pos_y);
						itr--;
						if(*itr >= 0){
							next_y = *itr;
							next_x = pos_x;
							break;
						}
					}else if(dir__ == 1){
						auto itr = h[pos_y].lower_bound(pos_x);
						itr++;
						if(*itr < c){
							next_y = pos_y;
							next_x = *itr;
							break;
						}

					}else if(dir__ == 2){
						auto itr = v[pos_x].lower_bound(pos_y);
						itr++;
						if(*itr < r){
							next_y = *itr;
							next_x = pos_x;
							break;
						}

					}else if(dir__ == 3){
						auto itr = h[pos_y].lower_bound(pos_x);
						itr--;
						if(*itr >= 0){
							next_y = pos_y;
							next_x = *itr;
							break;
						}
					}
				}
			}

			if(next_y < 0 || next_x < 0) return -1;
		}
	}
	return ans;
}

int main(){
	int T;
	cin >> T;
	for(int t=1; t<=T; t++){
		cout << "Case #" << t << ": " ;
		int ans = solve();
		if(ans >= 0){
			cout << ans << endl;
		}else{
			cout << "IMPOSSIBLE" << endl;
		}
	}
	return 0;
}