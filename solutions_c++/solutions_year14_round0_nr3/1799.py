
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include<cassert>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include<bitset>

#define REP(i,b,n) for(int i=b;i<(int)n;i++)
#define rep(i,n)   REP(i,0,n)
#define ALL(C)     (C).begin(),(C).end()
#define FOR(it,o)  for(__typeof((o).begin()) it=(o).begin(); it!=(o).end(); ++it)
#define dbg(x) cout << __LINE__ << ' ' << #x << " = " << (x) << endl


typedef long long ll;

using namespace std;

//ハマったらチェックリスト見ろ!!

const int N = 10;
int t[N][N];
int cnt[N][N];
bool clicked[N][N];
const int dy[] = {-1, 0, 1, 0, -1, 1, 1, -1};
const int dx[] = {0, 1, 0, -1, 1, 1, -1, -1};
int H, W;

void makeCnt(){
	rep(i, H){
		rep(j, W){
			cnt[i][j] = 0;
			rep(d, 8){
				int ny = i+dy[d], nx = j + dx[d];
				if(min(ny, nx) < 0)continue;
				if(ny >= H)continue;
				if(nx >= W)continue;
				cnt[i][j] += t[ny][nx];
			}
		}
	}
}

void click(int y, int x, int &res){
	if(clicked[y][x])return;
	res++;
	clicked[y][x] = true;
	if(cnt[y][x])return;
	rep(d, 8){
		int ny = y+dy[d], nx = x + dx[d];
		if(min(ny, nx) < 0)continue;
		if(ny >= H)continue;
		if(nx >= W)continue;
		click(ny, nx, res);
	}
}

int main(){
	int T;
	cin >> T;
	rep(tc, T){
		cout << "Case #"<<tc+1<<": "<<endl;
		int M;
		cin >> H >> W >> M;
		rep(i, (1<<(H*W))){
			if(__builtin_popcount(i) != M)continue;
			rep(j, H){
				rep(k, W){
					t[j][k] = bool((1<<(j*W+k))&i);
				}
			}
			makeCnt();
			rep(i, H){
				rep(j, W){
					rep(ii, H){
						rep(jj, W){
							clicked[ii][jj] = false;
						}
					}
					int res=0;
					if(t[i][j])continue;
					click(i, j, res);
					if(res + M == H*W){
						rep(ii, H){
							rep(jj, W){
								if(i == ii && j == jj){
									cout << "c";
								}
								else if(t[ii][jj]){
									cout << '*';
								}
								else cout <<".";
							}
						cout <<endl;
						
						}
					goto END;
					}
				}
			}
		}
		cout << "Impossible"<<endl;
		END:;
	}
  return 0;
}
