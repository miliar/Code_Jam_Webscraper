#include <iostream>
#include <cmath>
using namespace std;

int main (){
	int ncases;
	cin >> ncases;
	for(int i = 1; i <= ncases; i++){
		int n,r,p,s;
		cin >> n >> r >> p >> s;
		string c[3],old[3];
		int nold[3][3];
		int nc[3][3];
		nold[0][0] = 1;
		nold[0][1] = 1;
		nold[0][2] = 0;

		nold[1][0] = 0;
		nold[1][1] = 1;
		nold[1][2] = 1;

		nold[2][0] = 1;
		nold[2][1] = 0;
		nold[2][2] = 1;
		for(int x = 0; x < 3; x++)
			for(int y = 0; y < 3; y++)
				nc[x][y] = 0;

		old[0] = "PR";
		old[1] = "PS";
		old[2] = "RS";
		for(int j = 1; j < n; j++){
			c[0] = old[0] + old[1];
			c[1] = old[0] + old[2];
			c[2] = old[1] + old[2];
			for(int x = 0; x < 3; x++){
				nc[0][x] = nold[0][x] + nold[1][x];
				nc[1][x] = nold[0][x] + nold[2][x];
				nc[2][x] = nold[1][x] + nold[2][x];
			}
			for(int x = 0; x < 3; x++){
				old[x] = c[x];
				for(int y = 0; y < 3; y++){
					nold[x][y] = nc[x][y];
				}
			}
			
		}
		bool possible = false;
		for(int x = 0; x < 3; x++){
//			cout << nold[x][0] << " " << nold[x][1] << " " << nold[x][2] << endl;
			if(nold[x][0] == r && nold[x][1] == p && nold[x][2] == s){
				cout << "Case #" << i << ": " << old[x] << endl;
				possible = true;
				break;
			}
		}
		if(!possible) cout << "Case #" << i << ": IMPOSSIBLE" << endl;
	}

			  
	return 0;
}


