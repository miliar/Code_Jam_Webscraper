#include <iostream>
#include <algorithm>
#include <vector>
#include <stdio.h>
#include <stdlib.h>
#include <queue>

using namespace std;

int R, C, M;
bool vis[125];
bool onBit[125];
int accum;
int testCase;

int dr[8] = {-1, -1, 0, 1, 1, 1, 0, -1};
int dc[8] = {0, 1, 1, 1, 0, -1, -1, -1};

void bfs(int x, int y){
	queue<pair<int,int> > q;
	q.push(make_pair(x, y));

	vis[x*C+y] = true;
	accum = 0;
	
	while(!q.empty()){
		pair<int, int> p = q.front();
		q.pop();
		int r = p.first;
		int c = p.second;

		bool mineFound = false;
		for(int dir = 0; dir < 8; dir++){
			int newR = r + dr[dir];
			int newC = c + dc[dir];

			if(newR >= 0 && newR < R && newC >= 0 && newC < C){
				if(onBit[newR*C+newC]){
					mineFound = true;
					break;
				}
			}
		}

		if(!mineFound){
			for(int dir = 0; dir < 8; dir++){
				int newR = r + dr[dir];
				int newC = c + dc[dir];

				if(newR >= 0 && newR < R && newC >= 0 && newC < C && !vis[newR*C+newC]){
					vis[newR*C+newC] = true;
					accum++;
					q.push(make_pair(newR, newC));
				}
			}
		}
	}
}

bool dfs(void){

	int emptyCells = R*C-M;
	for(int mask = (1 << M)-1; mask >= 0; mask--){
		memset(onBit, false, sizeof(onBit));
		for(int j = 0; j < M; j++){
			if(mask & (1 << j)){
				onBit[j] = true;	// contains mine
			}
		}
		
		for(int r = 0; r < R; r++){
			for(int c = 0; c < C; c++){
				if(!onBit[r*C + c]){
					accum = 0;
					memset(vis, false, sizeof(vis));
					bfs(r, c);
					if(accum == emptyCells){
						cout << "Case #" << testCase << ": " << endl;
						for(int x = 0; x < R; x++){
							for(int y = 0; y < C; y++){
								if(x == r && y == c){
									cout << "c";
								}
								else if(onBit[x*C+y]){
									cout << "*";
								}
								else{
									cout << ".";
								}
							}
							cout << endl;
						}
						return true;
					}

				}
			}
		}
	}
	return false;
}

int main(void){
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int T;
	scanf("%d", &T);

	for(testCase = 0; testCase <= T; testCase++){
		scanf("%d %d %d", &R, &C, &M);
		bool isPossible = dfs();
		if(!isPossible){
			cout<<"Case #"<<testCase<<": "<<"Impossible"<<endl;
		}
	}

	return 0;
}