using namespace std;
#include <iostream>

#define ocu 1
#define lib 0

int main(){
	
	int T;
	cin >> T;
	for (int n = 1; n <= T; n++){
		int R, C, N;
		cin >> R >> C >> N;

		//cout << "CASO " << R << ' ' << C << ' ' << N << endl;
		
		//cout << "PONIENDO" << endl;
		int poniendo;
		
		int ** grid = new int * [R];
		for (int i = 0; i < R; i++){
			grid[i] = new int[C];
			for (int j = 0; j < C; j++) grid[i][j] = lib;
		}
		for (int i = 0; i < N; i++){
			int min = 999; int minx; int miny;
			for (int x = 0; x < R; x++){
				for (int y = 0; y < C; y++){
					if (grid[x][y] == ocu) continue;
					int vecinos = 0;
					if (x > 0) vecinos += grid[x-1][y];
					if (y > 0) vecinos += grid[x][y-1];
					if (y < C-1) vecinos += grid[x][y+1];
					if (x < R-1) vecinos += grid[x+1][y];
					if (vecinos < min){
						minx = x; miny = y; min = vecinos;
					}
				}
			}
			grid[minx][miny] = ocu;
		}
		

		/*for (int x = 0; x < R; x++){
			for (int y = 0; y < C; y++){
				if (grid[x][y] == lib) cout << 'O'; 
				else cout << 'X';
				cout << " | ";
			}
			cout << endl;
			for (int y = 0; y < C; y++){
				cout << "_   ";
			}
			cout << endl << endl;
		}*/

		int paredes = 0;
		for (int x = 0; x < R; x++){
			for (int y = 0; y < C; y++){
				if (grid[x][y] == lib) continue;
				if (x > 0) paredes += grid[x-1][y];
				if (y > 0) paredes += grid[x][y-1];
				if (y < C-1) paredes += grid[x][y+1];
				if (x < R-1) paredes += grid[x+1][y];
				grid[x][y] = lib;
			}
		}		
		
		poniendo = paredes;
		
		//cout << "SACANDO" << endl;
		int sacando;
		
		for (int i = 0; i < R; i++){
			for (int j = 0; j < C; j++) grid[i][j] = ocu;
		}
		for (int i = 0; i < R*C-N; i++){
			int max = 0; int maxx; int maxy;
			for (int x = 0; x < R; x++){
				for (int y = 0; y < C; y++){
					if (grid[x][y] == lib) continue;
					int vecinos = 0;
					if (x > 0) vecinos += grid[x-1][y];
					if (y > 0) vecinos += grid[x][y-1];
					if (y < C-1) vecinos += grid[x][y+1];
					if (x < R-1) vecinos += grid[x+1][y];
					if (vecinos >= max){
						maxx = x; maxy = y; max = vecinos;
					}
				}
			}
			grid[maxx][maxy] = lib;
		}
		
		
		/*for (int x = 0; x < R; x++){
			for (int y = 0; y < C; y++){
				if (grid[x][y] == lib) cout << 'O'; 
				else cout << 'X';
				cout << " | ";
			}
			cout << endl;
			for (int y = 0; y < C; y++){
				cout << "_   ";
			}
			cout << endl << endl;
		}*/
		
		paredes = 0;
		for (int x = 0; x < R; x++){
			for (int y = 0; y < C; y++){
				if (grid[x][y] == lib) continue;
				if (x > 0) paredes += grid[x-1][y];
				if (y > 0) paredes += grid[x][y-1];
				if (y < C-1) paredes += grid[x][y+1];
				if (x < R-1) paredes += grid[x+1][y];
				grid[x][y] = lib;
			}
		}	
		
		sacando = paredes;	
		
		if (poniendo < sacando) paredes = poniendo;
		
		cout << "Case #" << n << ": " << paredes << endl;
		//cout << endl << endl;

	}
	
}
