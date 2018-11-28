#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <deque>
#include <complex>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstring>

#define REP(i,x) for(int i=0 ; i<(int)(x) ; i++)
#define ALL(x) (x).begin(),(x).end()
#define LL long long

using namespace std;

int check(const vector<string> &field,int x,int y){
	int res = 0;
	int R = field.size(), C = field[0].size();
	queue<pair<int, int> > que;
	vector<vector<int> > used(R, vector<int>(C, -1));
	const int DY[] = { -1, 0, 1, 0 , -1, -1, 1, 1};
	const int DX[] = { 0, 1, 0, -1 , -1, 1, 1, -1};
	que.push(make_pair(x, y));
	while (!que.empty()){
		pair<int, int> node = que.front(); que.pop();
		int x = node.first;
		int y = node.second;
		if (used[y][x] != -1)continue;
		int mine = 0;
		REP(i, 8){
			int nx = x + DX[i];
			int ny = y + DY[i];
			if (ny >= 0 && ny < R && nx >= 0 && nx < C){
				if (field[ny][nx] == '*')mine++;
			}
		}
		used[y][x] = mine;
		res++;
		if (mine == 0){
			REP(i, 8){
				int nx = x + DX[i];
				int ny = y + DY[i];
				if (ny >= 0 && ny < R && nx >= 0 && nx < C){
					if (field[ny][nx] != '*' && used[ny][nx] == -1){
						que.push(make_pair(nx, ny));
					}
				}
			}
		}
	}
	return res;
}

void fillField(vector<string> &field,int e){
	int res = 0;
	int R = field.size(), C = field[0].size();
	queue<pair<int, int> > que;
	vector<vector<int> > used(R, vector<int>(C, -1));
	const int DY[] = { -1, 0, 1, 0, -1, -1, 1, 1 };
	const int DX[] = { 0, 1, 0, -1, -1, 1, 1, -1 };
	que.push(make_pair(C-1, R-1));
	while (!que.empty()){
		pair<int, int> node = que.front(); que.pop();
		int x = node.first;
		int y = node.second;
		if (used[y][x] != -1)continue;
		if (e == 0)continue;
		used[y][x] = 0;
		e--;
		field[y][x] = '.';
		REP(i, 8){
			int nx = x + DX[i];
			int ny = y + DY[i];
			if (ny >= 0 && ny < R && nx >= 0 && nx < C){
				if (field[ny][nx] == '-' && used[ny][nx] == -1){
					que.push(make_pair(nx, ny));
				}
			}
		}
	}
}


int main(){
	int T;
	cin >> T;
	REP(testCase, T){
		int R, C, M;
		cin >> R >> C >> M;
		int E = R*C - M;

		bool hasAnswer = false;
		vector<string> ans(R, string(C, '.'));
		if (M > 0){
			for (int h = 0; h <= R; h++){
				vector<string> field(R, string(C, '.'));
				int mine = M;
				int e = R*C;
				REP(y, h){
					if (mine<C)continue;
					REP(x, C)if (mine > 1){
						field[y][x] = '*';
						mine--;
						e--;
					}
				}
				REP(x, C){
					REP(y, R){
						if (mine > 1 && field[y][x] == '.'){
							field[y][x] = '*';
							mine--;
							e--;
						}
					}
				}
				REP(y, R)REP(x, C){
					if (field[y][x] == '.'){
						field[y][x] = '*';
						REP(cy, R)REP(cx, C)if (field[cy][cx] == '.'){
							if (check(field, cx, cy) == E){
								field[cy][cx] = 'c';
								hasAnswer = true;
								ans = field;
								goto FINISH;
							}
						}
						field[y][x] = '.';
					}
				}
			}
		}
		else{
			hasAnswer = true;
			ans[0][0] = 'c';
		}
		




FINISH:
		cout << "Case #" <<  testCase+1 << ":" << endl;
		if (hasAnswer){
			REP(y, R)cout << ans[y] << endl;
		}
		else{
			//cout << R << " " << C << " " << M << endl;
			//REP(y, R)cout << ans[y] << endl;
			cout << "Impossible" << endl;
		}
	}
	return 0;
}