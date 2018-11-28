#include <iostream>
#include <map>
using namespace std;

char solve(char field[4][4]){
	char w[2] = {'X', 'O'};
	for(int i = 0; i < 2; i++){
		if ((field[0][0] == w[i] || field[0][0] == 'T') &&
			(field[0][1] == w[i] || field[0][1] == 'T') &&
			(field[0][2] == w[i] || field[0][2] == 'T') &&
			(field[0][3] == w[i] || field[0][3] == 'T')) return w[i];
		if ((field[1][0] == w[i] || field[1][0] == 'T') &&
			(field[1][1] == w[i] || field[1][1] == 'T') &&
			(field[1][2] == w[i] || field[1][2] == 'T') &&
			(field[1][3] == w[i] || field[1][3] == 'T')) return w[i];
		if ((field[2][0] == w[i] || field[2][0] == 'T') &&
			(field[2][1] == w[i] || field[2][1] == 'T') &&
			(field[2][2] == w[i] || field[2][2] == 'T') &&
			(field[2][3] == w[i] || field[2][3] == 'T')) return w[i];
		if ((field[3][0] == w[i] || field[3][0] == 'T') &&
			(field[3][1] == w[i] || field[3][1] == 'T') &&
			(field[3][2] == w[i] || field[3][2] == 'T') &&
			(field[3][3] == w[i] || field[3][3] == 'T')) return w[i];
		if ((field[0][0] == w[i] || field[0][0] == 'T') &&
			(field[1][0] == w[i] || field[1][0] == 'T') &&
			(field[2][0] == w[i] || field[2][0] == 'T') &&
			(field[3][0] == w[i] || field[3][0] == 'T')) return w[i];
		if ((field[0][1] == w[i] || field[0][1] == 'T') &&
			(field[1][1] == w[i] || field[1][1] == 'T') &&
			(field[2][1] == w[i] || field[2][1] == 'T') &&
			(field[3][1] == w[i] || field[3][1] == 'T')) return w[i];
		if ((field[0][2] == w[i] || field[0][2] == 'T') &&
			(field[1][2] == w[i] || field[1][2] == 'T') &&
			(field[2][2] == w[i] || field[2][2] == 'T') &&
			(field[3][2] == w[i] || field[3][2] == 'T')) return w[i];
		if ((field[0][3] == w[i] || field[0][3] == 'T') &&
			(field[1][3] == w[i] || field[1][3] == 'T') &&
			(field[2][3] == w[i] || field[2][3] == 'T') &&
			(field[3][3] == w[i] || field[3][3] == 'T')) return w[i];
		if ((field[0][0] == w[i] || field[0][0] == 'T') &&
			(field[1][1] == w[i] || field[1][1] == 'T') &&
			(field[2][2] == w[i] || field[2][2] == 'T') &&
			(field[3][3] == w[i] || field[3][3] == 'T')) return w[i];
		if ((field[3][0] == w[i] || field[3][0] == 'T') &&
			(field[2][1] == w[i] || field[2][1] == 'T') &&
			(field[1][2] == w[i] || field[1][2] == 'T') &&
			(field[0][3] == w[i] || field[0][3] == 'T')) return w[i];
	}
	for(int i = 0; i < 4; i++){
		for(int j = 0; j < 4; j++){
			if (field[i][j] == '.') return 'G';
		}
	}
	return 'D';
}

int main(){
	freopen("ans.txt", "w", stdout);
	int n;
	cin>>n;
	char field[4][4];
	for(int i = 1; i <= n; i++){
		for(int y = 0; y < 4; y++)
			for(int x = 0; x < 4; x++)
				cin>>field[y][x];
		char res = solve(field);
		if (res == 'X') cout<<"Case #"<<i<<": X won\n";
		if (res == 'O') cout<<"Case #"<<i<<": O won\n";
		if (res == 'D') cout<<"Case #"<<i<<": Draw\n";
		if (res == 'G') cout<<"Case #"<<i<<": Game has not completed\n";
	}
}