#include<iostream>
#include<fstream>
using namespace std;
int a[20][20];
int r, c, n;
inline int getScore(){
	int d[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}}, x, y;
	int res = 0;
	for(int i = 0; i < r; i++){
		for(int j = 0; j < c; j++){
			if(!a[i][j])
				continue;
			for(int k = 0; k < 4; k++){
				x = i + d[k][0], y = j + d[k][1];
				if(a[x][y])
					res++;
			}
		}
	}
	return res / 2;
}

int fill(int rc, int k){
	if(rc == r * c){
		if(k != n)
			return 100000;
		return getScore();
	}
	int res = fill(rc + 1, k);
	if(k < n){
		a[rc / c][rc % c] = 1;
		res = min(res, fill(rc + 1, k + 1));
		a[rc / c][rc % c] = 0;
	}
	return res;
}

int main(){
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);
	int t;
	cin >> t;
	for(int i = 0; i < t; i++){
		memset(a, 0, sizeof a);
		cin >> r >> c >> n;
		cout << "Case #" << i + 1 << ": " << fill(0, 0) << endl;
	}
	return 0;
}