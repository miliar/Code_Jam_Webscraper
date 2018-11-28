#pragma comment(linker, "/STACK:16777216")
#include <vector>
#include <string>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <map>
#include <queue>
#include <set>
#include <memory.h>
#include <string.h>
#include <deque>
#include <assert.h>
#include <stack>
using namespace std;

#define FOR(i,a,b) for(int (i) = (a); (i) <= (b); ++(i))
#define inf 2000000000
#define pb push_back
#define all(c) (c).begin(), (c).end()
#define pi 2*acos(0.0)
#define mp(a,b) make_pair((a), (b))
#define X first
#define Y second

typedef vector<int> vint;
typedef long long ll;
typedef pair<int, int> pii;

int t;
int r,c;
int m;
char g[55][55];
int used[55][55];

int bitcnt(int mask){
	int res = 0;
	for(int i = 0; i < 27; i++){
		if((mask&(1 << i)) != 0)
			res++;
	}
	return res;
}

int dx[] = {0,1,0,-1,1,1,-1,-1};
int dy[] = {1,0,-1,0,1,-1,-1,1};

void flood(int x, int y){
	if(used[x][y] == -1){
		int mines = 0;
		FOR(k,0,7){
			if(x + dx[k] < r && x + dx[k] >= 0 && y+dy[k] >= 0 && y+dy[k] < c){
				if(g[x+dx[k]][y+dy[k]] == '*'){
					mines++;
				}
			}
		}
		if(mines == 0){
			used[x][y] = 0;
			FOR(k,0,7){
				if(x + dx[k] < r && x + dx[k] >= 0 && y+dy[k] >= 0 && y+dy[k] < c){
					flood(x+dx[k], y+dy[k]);
				}
			}
		}else{
			used[x][y] = mines;
		}
	}
}

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> t;
	FOR(tt, 1, t){
		memset(g,'.',sizeof(g));
		cin >> r >> c >> m;
		bool good = 1;
		cout << "Case #" << tt << ":" << endl;
		FOR(mask, 0, (1 << (r*c))-1 ){
			if(bitcnt(mask) == m){
				good = 1;
				memset(g, '.', sizeof(g));
				memset(used,0, sizeof(used));
				FOR(i,0,r-1)
					FOR(j,0,c-1){
						if( (mask&(1<<(i*c+j))) != 0){
							g[i][j] = '*';
							used[i][j] = 1;
						}
					}

	

				memset(used,-1, sizeof(used));
				bool step = 0;
				

				int si = -1;
				int sj = -1;
				FOR(i,0,r-1){
					FOR(j,0,c-1){
						if(used[i][j] == -1 && g[i][j] != '*'){
							int mines = 0;
							FOR(k,0,7){
								if(i + dx[k] < r && i + dx[k] >= 0 && j+dy[k] >= 0 && j+dy[k] < c){
									if(g[i+dx[k]][j+dy[k]] == '*'){
										mines++;
									}
								}
							}
							if(mines == 0){
								si = i;
								sj = j;
							}
						}
					}
				}
						
				if(si != -1 && sj != -1){
					flood(si,sj);
					step = 1;
				}
				FOR(i,0,r-1){
					FOR(j,0,c-1){
						if(used[i][j] == -1 && g[i][j] != '*'){
							if(step == 0){
								si = i; sj = j;
								flood(i,j);
								step = 1;							
							}else{
								good = 0;
							}
						}
					}
				}
				/*cout << "----------";
				FOR(i,0,r-1){
					FOR(j,0,c-1){
						cout << g[i][j];
					}
					cout << endl;
				}
				FOR(i,0,r-1){
					FOR(j,0,c-1){
						cout << used[i][j];
					}
					cout << endl;
				}*/

				if(good) {
					g[si][sj] = 'c';
					break;
				}

			}
		}

		if(good){
			FOR(i,0,r-1){
				FOR(j,0,c-1){
					cout << g[i][j];
				}
				cout << endl;
			}
		}else{
			cout << "Impossible" << endl;
		}

	}
	
	
	
	
    return 0;
}