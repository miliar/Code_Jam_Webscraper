#include <iostream>
#include <cstdio>
#include <fstream>

using namespace std;

int n;
int number = 1;
int grid[100][100];
int finalGrid[100][100];
ofstream fout("output.out");

void check(int N, int M)
{
	for(int i = 0; i < N; i++){
		for(int j = 0; j < M; j++){
			if(grid[i][j] != finalGrid[i][j]){
				fout << "NO\n";
				return;
			}
		}
	}
	fout << "YES\n";
}

int function(int N, int M, int row, int col)
{
	//0: none
	//1: check up-down
	//2: check left-right
	//3: both
	int num = 0;
	int check = 0;
	for(int i = 0; i < N; i++){
		if(grid[row][col] < grid[i][col]){
			check = 1;
			break;
		}
	}
	if(check == 0){
		num += 1;
		for(int i = 0; i < N; i++){
			finalGrid[i][col] = grid[row][col];
		}
	}
	check = 0;
	for(int i = 0; i < M; i++){
		if(grid[row][col] < grid[row][i]){
			check = 1;
			break;
		}
	}
	if(check == 0){
		num += 2;
		for(int i = 0; i < M; i++){
			finalGrid[row][i] = grid[row][col];
		}
	}
	return num;
}

void answer()
{
	fout << "Case #" << number << ": ";
	number++;
	int N, M;
	cin >> N >> M;
	int maximum = 0;
	int arr[101] = { 0 };
	for(int i = 0; i < N; i++){
		for(int j = 0; j < M; j++){
			cin >> grid[i][j];
			arr[grid[i][j]] = 1;
			if(grid[i][j] > maximum){
				maximum = grid[i][j];
			}
		}
	}
	for(int i = 0; i < N; i++){
		for(int j = 0; j < M; j++){
			finalGrid[i][j] = maximum;
		}
	}
	int possNums[100] = { 0 };
	int index = 0;
	for(int i = 1; i <= 100; i++){
		if(arr[i] == 1){
			possNums[index] = i;
			index++;
		}
	}
	for(int k = index - 1; k >= 0; k--){
		for(int i = 0; i < N; i++){
			for(int j = 0; j < M; j++){
				if(grid[i][j] == k){
					function(N, M, i, j);
				}
			}
		}
	}
	check(N, M);
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
