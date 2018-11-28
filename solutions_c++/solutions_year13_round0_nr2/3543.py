#include <iostream>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <iterator>
using namespace std;

#define PW2(n) (n)*(n)
#define RPT(var, n) for(int var = 0; var < (n); var++)
#define RVT(var, n) for(int var = (n - 1); var >= 0; var--)
#define PRN(var) cout << #var << "=" << (var) << endl
#define vint vector<int>

int n, w, h, cnt;
int bd[102][102];

bool j(){
	RPT(x, w){
		RPT(y, h){
			if(bd[y+1][x+1] > 100){
				return true;
			}
		}
	}
	return false;
}

bool s(){
	int t = bd[1][1];
	RPT(x, w){
		RPT(y, h){
			if(t != bd[x + 1][y + 1]){
				return false;
			}
		}
	}
	return true;
}

bool z(){
	if(j()){
		cout << "Case #" << cnt+1 << ": NO" << endl;
		return false;
	}else if(s()){
		cout << "Case #" << cnt+1 << ": YES" << endl;
		return false;
	}
	return true;
}

bool q(int x, int y, int ax, int ay, int t){
	if(bd[x][y] > t){
		return false;
	}else if(bd[x][y] == 0){
		return true;
	}else{
		return q(x + ax, y + ay, ax, ay, t);
	}
}

int main(){
	cin >> n;
	
	for(; cnt<n; cnt++){
		cin >> h >> w;
		
		RPT(i, w + 2){
			bd[i][0] = 0;
			bd[i][h+1] = 0;
		}

		RPT(i, h + 2){
			bd[0][i] = 0;
			bd[w+1][i] = 0;
		}
		
		RPT(y, h){		
			RPT(x, w){
				cin >> bd[x+1][y+1];
			}
		}

		while(z()){
			int	min = 10000, xr, yr;


			RPT(y, h){
				RPT(x, w){
					if(bd[x+1][y+1] < min){
						min = bd[x+1][y+1];
					}
				}
			}
			
			bool e = false;
			RPT(x, w){
				RPT(y, h){			
					if(bd[x+1][y+1] == min 
					 && !( q(x+1, y+1, 1, 0, min) && q(x+1, y+1, -1, 0, min) )
					  && !( q(x+1, y+1, 0, 1, min) && q(x+1, y+1, 0, -1, min) ) ){
						cout << "Case #" << cnt+1 << ": NO" << endl;
						e = true;
						break;
					}
				}
				if(e) break;
			}
			if(e) break;
			
			RPT(x, w){
				RPT(y, h){
					if(bd[x+1][y+1] == min){
						bd[x+1][y+1]++;
					}
				}
			}		
		}
	}

} 
