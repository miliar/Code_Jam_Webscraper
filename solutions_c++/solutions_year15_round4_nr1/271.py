#include<iostream>
#include<algorithm>
#include<map>
#include<vector>
#include<set>
#include<cmath>
#include<cstring>

using namespace std;
typedef long long Int;

#define INF (1LL<<60)
int T;

int xs[] = {0, 1, 0, -1}, ys[] = {1, 0, -1, 0};
char field[108][108];
bool ok[108][108][4];

void solve(){
	int res = 0, r, c;
	cin >> r >> c;
	for(int i = 0;i < r;i++){
		for(int j = 0;j < c;j++){
			cin >> field[i][j];
		}
	}
	for(int i = 0;i < r;i++){
		for(int j = 0;j < c;j++){
			if(field[i][j] == '.')continue;
			for(int k = 0;k < 4;k++){
				int dx = xs[k], dy = ys[k];
				int ti = i, tj = j;
				ti += dx;
				tj += dy;
				ok[i][j][k] = false;
				while(0 <= ti && ti < r && 0 <= tj && tj < c){
					if(field[ti][tj] != '.')ok[i][j][k] = true;
					ti += dx;
					tj += dy;
				}
			}
			if(!ok[i][j][0] && !ok[i][j][1] && !ok[i][j][2] && !ok[i][j][3]){
				cout << "IMPOSSIBLE" << endl;
				return;
			}
			if(field[i][j] == '>' && !ok[i][j][0])res++;
			if(field[i][j] == 'v' && !ok[i][j][1])res++;
			if(field[i][j] == '<' && !ok[i][j][2])res++;
			if(field[i][j] == '^' && !ok[i][j][3])res++;
		}
	}
	cout << res << endl;
	return;
}

int main(){
	cin >> T;
	for(int i = 1;i <= T;i++){
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;	
}