#include <iostream>
#include <cstdio>
#include <fstream>
#include <string>

using namespace std;

int n;
int arr[4][4];
int counter = 1;
int done = 0;
ofstream fout("output.out");

void reset()
{
	for(int i = 0; i < 4; i++){
		for(int j = 0; j < 4; j++){
			arr[i][j] = 0;
		}
	}
}

int win(int a, int b, int c, int d)
{
	if(a == 1 && b == 1 && c == 1 && d == 1)
		return 1;
	if(a == 3 && b == 1 && c == 1 && d == 1)
		return 1;
	if(a == 1 && b == 3 && c == 1 && d == 1)
		return 1;
	if(a == 1 && b == 1 && c == 3 && d == 1)
		return 1;
	if(a == 1 && b == 1 && c == 1 && d == 3)
		return 1;
	if(a == 2 && b == 2 && c == 2 && d == 2)
		return 2;
	if(a == 3 && b == 2 && c == 2 && d == 2)
		return 2;
	if(a == 2 && b == 3 && c == 2 && d == 2)
		return 2;
	if(a == 2 && b == 2 && c == 3 && d == 2)
		return 2;
	if(a == 2 && b == 2 && c == 2 && d == 3)
		return 2;
	return 0;
}

void answer()
{
	fout << "Case #" << counter << ": ";
	counter++;
	for(int i = 0; i < 4; i++){
		string s;
		cin >> s;
		for(int j = 0; j < 4; j++){
			if(s[j] == 'X'){
				arr[i][j] = 1;
			}
			else if(s[j] == 'O'){
				arr[i][j] = 2;
			}
			else if(s[j] == 'T'){
				arr[i][j] = 3;
			}
		}
	}
	for(int i = 0; i < 4; i++){
		int num = win(arr[i][0], arr[i][1], arr[i][2], arr[i][3]);
		if(num == 1){
			fout << "X won\n";
			done = 1;
			break;
		}
		if(num == 2){
			fout << "O won\n";
			done = 1;
			break;
		}
		num = win(arr[0][i], arr[1][i], arr[2][i], arr[3][i]);
		if(num == 1){
			fout << "X won\n";
			done = 1;
			break;
		}
		if(num == 2){
			fout << "O won\n";
			done = 1;
			break;
		}
	}
	if(done == 0){
		int num = win(arr[0][0], arr[1][1], arr[2][2], arr[3][3]);
		if(num == 1){
			fout << "X won\n";
			done = 1;
		}
		if(num == 2){
			fout << "O won\n";
			done = 1;
		}
	}
	if(done == 0){
		int num = win(arr[0][3], arr[1][2], arr[2][1], arr[3][0]);
		if(num == 1){
			fout << "X won\n";
			done = 1;
		}
		if(num == 2){
			fout << "O won\n";
			done = 1;
		}
	}
	if(done == 0){
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				if(arr[i][j] == 0){
					fout << "Game has not completed\n";
					done = 1;
					break;
				}
			}
			if(done == 1){
				break;
			}
		}
		if(done == 0){
			fout << "Draw\n";
		}
	}
	reset();
	done = 0;
}

int main()
{
	freopen("file.in", "r", stdin);
	cin >> n;
	for(int i = 0; i < n; i++){
		answer();
	}
	return 0;
}