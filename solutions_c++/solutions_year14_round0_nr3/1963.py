#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<fstream>
#include<queue>

using namespace std;

#define is_good(x, y, R, C) (x >= 0 && x < R && y >= 0 && y < C)

int mine(vector<string> &maze, int x, int y){
	if (maze[x][y] == '*')
		return -1;
	int R = maze.size(), C = maze[0].size();
	int ret = 0;
	for (int i = -1; i < 2; i++)
	for (int j = -1; j < 2; j++)
	if (i != 0 || j != 0)
	if (is_good(x + i, y + j, R, C))
	if (maze[x + i][y + j] == '*')
		ret++;
	return ret;
}

int DFS(vector<string> maze, int x, int y){
	int R = maze.size(), C = maze[0].size();
	queue<pair<int, int> > que;
	pair<int, int> sand;
	int ret = 0;
	if (maze[x][y] == '.'){
		sand.first = x;
		sand.second = y;
		if (mine(maze, x, y) == 0){
			que.push(sand);
		}
		else ret++;
		maze[x][y] = 'c';
	}
	while (!que.empty()){
		ret++;
		sand = que.front();
		que.pop();
		int xx = sand.first, yy = sand.second;
		for (int i = -1; i < 2; i++)
		for (int j = -1; j < 2; j++)
		if (i != 0 || j != 0)
		if (is_good(xx + i, yy + j, R, C))
		if (maze[xx + i][yy + j] == '.'){
			int mn = mine(maze, xx + i, yy + j);
			if (mn == 0){
				sand.first = xx + i;
				sand.second = yy + j;
				que.push(sand);
				maze[xx + i][yy + j] = '0';
			}
			else if (mn > 0){
				maze[xx + i][yy + j] = '0' + mn;
				ret++;
			}
		}
	}
	return ret;
}



int main(){
	ifstream cin("C-small-attempt0.in");
	ofstream cout("C-small-attempt0.out");

	int T;
	cin >> T;
	for (int t = 0; t < T; t++){
		cout << "Case #" << (t + 1) << ":\n";
		int R, C, M, L;
		cin >> R >> C >> M;
		L = R*C - M;
		vector<string> maze(R);
		string mine(M, '*'), hide(L, '.'), str = mine + hide;
		bool found = false;
		do{
			for (int i = 0; i < R; i++)
				maze[i] = str.substr(i*C, C);
			for (int i = 0; i < R && !found; i++)
			for (int j = 0; j < C && !found; j++)
			if (maze[i][j] == '.')
			if (DFS(maze, i, j) == L){
				found = true;
				maze[i][j] = 'c';
				break;
			}
		} while (next_permutation(str.begin(), str.end()) && !found);
		if (found){
			for (int i = 0; i < R; i++)
				cout << maze[i] << "\n";
		}
		else cout << "Impossible\n";
	}
}