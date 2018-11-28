#include <cstdio>
#include <string>
#include <iostream>
using namespace std;

int test, i, j;
string s[5];
bool Check(int x, int y, int v, int u, char c){
	while (x < 4 && y < 4){
		if (s[x][y] != c && s[x][y] != 'T')
			return false;
		x += v;
		y += u;
	}
	return true;
}

void find(){
	if (Check(0, 0, 1, 1, 'X') || Check(3, 0, -1, 1, 'X')){
		cout << "X won" << endl;
		return;
	}
	if (Check(0, 0, 1, 1, 'O') || Check(3, 0, -1, 1, 'O')){
		cout << "O won" << endl;
		return;
	}
		
	for (int i = 0; i < 4; i++){
		if (Check(i, 0, 0, 1, 'X') || Check(0, i, 1, 0, 'X')){
			cout << "X won" << endl;
			return;
		}
		if (Check(i, 0, 0, 1, 'O') || Check(0, i, 1, 0, 'O')){
			cout << "O won" << endl;
			return;
		}
	}
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			if (s[i][j] == '.'){
				cout << "Game has not completed" << endl;
				return;
			}
	cout << "Draw" << endl;
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w", stdout);
	scanf("%d",&test);
	for (int testCase = 1; testCase <= test; testCase ++){
		for (int i = 0; i < 4; i++)
			cin >> s[i];
		cout << "Case #" << testCase << ": ";
		find();
	}
    return 0;
}
