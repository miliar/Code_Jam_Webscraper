#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
int R, C, M;
char grid[5][5]; // the one to output
char grid2[5][5]; // to draw the 0s and ns recursively

bool out_of_bounds(int x, int y){
	return x < 0 || y < 0 || x >= R || y >= C;
}

void fill_nums(int ix, int jx){ // check grid 1 grid 2 stuff
	if (grid2[ix][jx] == '*' || (grid2[ix][jx] >= '0' && grid2[ix][jx] <= '9')) {
		return;
	}
	int dx[] = {-1,-1,-1, 0, 0, 1, 1, 1};
	int dy[] = {-1,0,1,-1, 1, -1, 0, 1};
	char c_cell = '0';
	for (int i = 0; i < 8; i++){
		if (out_of_bounds(ix+dx[i], jx+dy[i])){
			continue;
		}
		if (grid2[ix+dx[i]][jx+dy[i]]=='*'){
			c_cell += 1;
		}
	}
	grid2[ix][jx] = c_cell;
	
	if (c_cell == '0'){
		for (int i = 0; i < 8; i++){
			if (out_of_bounds(ix+dx[i], jx+dy[i])){
				continue;
			}
			fill_nums(ix+dx[i], jx + dy[i]);
		}
	}
}

// check if there is a dot in grid2 left
bool dot_left(){
	for (int i = 0; i < R; i++){
		for (int j = 0; j < C; j++){
			if (grid2[i][j] == '.') return true;
		}
	}
	return false;
}

// click a click at this location is valid and will recursively reveal entire grid
bool check_one_click(int ix, int jx){
	if (grid[ix][jx] == '*') return false;
	for (int i = 0; i < R; i++){
		for (int j = 0; j < C; j++){
			grid2[i][j] = grid[i][j];
		}
	}
	grid[ix][jx] = 'c';
	grid2[ix][jx] = 'c';
	fill_nums(ix,jx);
	if(dot_left()){
		grid[ix][jx] = '.';
		grid2[ix][jx] = '.';
		return false;
	} else return true;
}


void print_grid(){
	for (int i = 0; i < R; i++){
		for (int j = 0; j < C; j++){
			cout << grid[i][j];
		} cout << endl;
	}
}


bool dfs(int mines, int ind, int jind){
	if (mines <= 0){
		for (int i = 0; i < R; i++){
			for (int j = 0; j < C; j++){
				if (check_one_click(i, j)){
					return true;
				}
			}
		}
		return false;
	}
	for (int i = ind; i < R; i++){
		for (int j = jind; j < C; j++){
			//print_grid();
			//cout << endl;
			//cout << i << " " << j << endl;
			grid[i][j] = '*';
			//print_grid();
			//cout << endl;
			int next_i = i, next_j = j+1;
			if (j+1 == C){
				next_i = i+1;
				next_j = 0;
			}
			//cout << next_i << " x " << next_j << endl;
			if (dfs(mines-1, next_i, next_j)) return true;
			else grid[i][j] = '.';
		}
	}
	return false;
}

int main(){
	int T; cin >> T;
	for (int test = 1; test <= T; test++){
		printf("Case #%d:\n", test);
		cin >> R >> C >> M;
		for (int i = 0; i < R; i++){
			for (int j = 0; j < C; j++){
				grid[i][j] = '.';
				grid2[i][j] = '.';
			}
		}
		bool res = dfs(M, 0, 0);

		if (!res){
			cout << "Impossible" << endl;
		} else {
			for (int i = 0; i < R; i++){
				for (int j = 0; j < C; j++){
					cout << grid[i][j];
				} cout << endl;
			}
		}
	}

	return 0;
}
