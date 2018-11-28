#include <iostream>
#include <cstdio>
#include <cmath>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <memory.h>
#include <assert.h>

using namespace std;

#pragma comment(linker, "/STACK:100000000")

#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define ll long long
#define ull unsigned long long
#define sz(x) (int)(x).size()



int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int N;
	scanf("%d", &N);
	for(int test = 0; test < N; test++) {
		scanf("\n");
		int matrix[4][4];
		int cnt = 0;
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				char sym;
				scanf("%c", &sym);
				if(sym == 'X') matrix[i][j] = 1;
				else if(sym == 'O') matrix[i][j] = 2;
				else if(sym == '.') matrix[i][j] = 0, cnt++;
				else matrix[i][j] = 3;
			}
			scanf("\n");
		}
		if((matrix[0][0] == 1 || matrix[0][0] == 3) && (matrix[0][1] == 1 || matrix[0][1] == 3) && 
			(matrix[0][2] == 1 || matrix[0][2] == 3) && (matrix[0][3] == 1 || matrix[0][3] == 3)) {
				cout << "Case #" << test + 1 << ": X won" << endl;
				continue;
		}
		if((matrix[1][0] == 1 || matrix[1][0] == 3) && (matrix[1][1] == 1 || matrix[1][1] == 3) && 
			(matrix[1][2] == 1 || matrix[1][2] == 3) && (matrix[1][3] == 1 || matrix[1][3] == 3)) {
				cout << "Case #" << test + 1 << ": X won" << endl;
				continue;
		}
		if((matrix[2][0] == 1 || matrix[2][0] == 3) && (matrix[2][1] == 1 || matrix[2][1] == 3) && 
			(matrix[2][2] == 1 || matrix[2][2] == 3) && (matrix[2][3] == 1 || matrix[2][3] == 3)) {
				cout << "Case #" << test + 1 << ": X won" << endl;
				continue;
		}
		if((matrix[3][0] == 1 || matrix[3][0] == 3) && (matrix[3][1] == 1 || matrix[3][1] == 3) && 
			(matrix[3][2] == 1 || matrix[3][2] == 3) && (matrix[3][3] == 1 || matrix[3][3] == 3)) {
				cout << "Case #" << test + 1 << ": X won" << endl;
				continue;
		}
		
		if((matrix[0][0] == 1 || matrix[0][0] == 3) && (matrix[1][1] == 1 || matrix[1][1] == 3) && 
			(matrix[2][2] == 1 || matrix[2][2] == 3) && (matrix[3][3] == 1 || matrix[3][3] == 3)) {
				cout << "Case #" << test + 1 << ": X won" << endl;
				continue;
		}
		if((matrix[3][0] == 1 || matrix[3][0] == 3) && (matrix[2][1] == 1 || matrix[2][1] == 3) && 
			(matrix[1][2] == 1 || matrix[1][2] == 3) && (matrix[0][3] == 1 || matrix[0][3] == 3)) {
				cout << "Case #" << test + 1 << ": X won" << endl;
				continue;
		}
		if((matrix[3][0] == 2 || matrix[3][0] == 3) && (matrix[2][1] == 2 || matrix[2][1] == 3) && 
			(matrix[1][2] == 2 || matrix[1][2] == 3) && (matrix[0][3] == 2 || matrix[0][3] == 3)) {
				cout << "Case #" << test + 1 << ": O won" << endl;
				continue;
		}
		if((matrix[0][0] == 2 || matrix[0][0] == 3) && (matrix[1][1] == 2 || matrix[1][1] == 3) && 
			(matrix[2][2] == 2 || matrix[2][2] == 3) && (matrix[3][3] == 2 || matrix[3][3] == 3)) {
				cout << "Case #" << test + 1 << ": O won" << endl;
				continue;
		}

		if((matrix[0][0] == 2 || matrix[0][0] == 3) && (matrix[0][1] == 2 || matrix[0][1] == 3) && 
			(matrix[0][2] == 2 || matrix[0][2] == 3) && (matrix[0][3] == 2 || matrix[0][3] == 3)) {
				cout << "Case #" << test + 1 << ": O won" << endl;
				continue;
		}
		if((matrix[1][0] == 2 || matrix[1][0] == 3) && (matrix[1][1] == 2 || matrix[1][1] == 3) && 
			(matrix[1][2] == 2 || matrix[1][2] == 3) && (matrix[1][3] == 2 || matrix[1][3] == 3)) {
				cout << "Case #" << test + 1 << ": O won" << endl;
				continue;
		}
		if((matrix[2][0] == 2 || matrix[2][0] == 3) && (matrix[2][1] == 2 || matrix[2][1] == 3) && 
			(matrix[2][2] == 2 || matrix[2][2] == 3) && (matrix[2][3] == 2 || matrix[2][3] == 3)) {
				cout << "Case #" << test + 1 << ": O won" << endl;
				continue;
		}
		if((matrix[3][0] == 2 || matrix[3][0] == 3) && (matrix[3][1] == 2 || matrix[3][1] == 3) && 
			(matrix[3][2] == 2 || matrix[3][2] == 3) && (matrix[3][3] == 2 || matrix[3][3] == 3)) {
				cout << "Case #" << test + 1 << ": O won" << endl;
				continue;
		}

		for(int i = 0; i < 4; i++) {
			for(int j = i + 1; j < 4; j++) {
				swap(matrix[i][j], matrix[j][i]);
			}
		}
		
		if((matrix[0][0] == 2 || matrix[0][0] == 3) && (matrix[0][1] == 2 || matrix[0][1] == 3) && 
			(matrix[0][2] == 2 || matrix[0][2] == 3) && (matrix[0][3] == 2 || matrix[0][3] == 3)) {
				cout << "Case #" << test + 1 << ": O won" << endl;
				continue;
		}
		if((matrix[1][0] == 2 || matrix[1][0] == 3) && (matrix[1][1] == 2 || matrix[1][1] == 3) && 
			(matrix[1][2] == 2 || matrix[1][2] == 3) && (matrix[1][3] == 2 || matrix[1][3] == 3)) {
				cout << "Case #" << test + 1 << ": O won" << endl;
				continue;
		}
		if((matrix[2][0] == 2 || matrix[2][0] == 3) && (matrix[2][1] == 2 || matrix[2][1] == 3) && 
			(matrix[2][2] == 2 || matrix[2][2] == 3) && (matrix[2][3] == 2 || matrix[2][3] == 3)) {
				cout << "Case #" << test + 1 << ": O won" << endl;
				continue;
		}
		if((matrix[3][0] == 2 || matrix[3][0] == 3) && (matrix[3][1] == 2 || matrix[3][1] == 3) && 
			(matrix[3][2] == 2 || matrix[3][2] == 3) && (matrix[3][3] == 2 || matrix[3][3] == 3)) {
				cout << "Case #" << test + 1 << ": O won" << endl;
				continue;
		}
		
		if((matrix[0][0] == 1 || matrix[0][0] == 3) && (matrix[0][1] == 1 || matrix[0][1] == 3) && 
			(matrix[0][2] == 1 || matrix[0][2] == 3) && (matrix[0][3] == 1 || matrix[0][3] == 3)) {
				cout << "Case #" << test + 1 << ": X won" << endl;
				continue;
		}
		if((matrix[1][0] == 1 || matrix[1][0] == 3) && (matrix[1][1] == 1 || matrix[1][1] == 3) && 
			(matrix[1][2] == 1 || matrix[1][2] == 3) && (matrix[1][3] == 1 || matrix[1][3] == 3)) {
				cout << "Case #" << test + 1 << ": X won" << endl;
				continue;
		}
		if((matrix[2][0] == 1 || matrix[2][0] == 3) && (matrix[2][1] == 1 || matrix[2][1] == 3) && 
			(matrix[2][2] == 1 || matrix[2][2] == 3) && (matrix[2][3] == 1 || matrix[2][3] == 3)) {
				cout << "Case #" << test + 1 << ": X won" << endl;
				continue;
		}
		if((matrix[3][0] == 1 || matrix[3][0] == 3) && (matrix[3][1] == 1 || matrix[3][1] == 3) && 
			(matrix[3][2] == 1 || matrix[3][2] == 3) && (matrix[3][3] == 1 || matrix[3][3] == 3)) {
				cout << "Case #" << test + 1 << ": X won" << endl;
				continue;
		}

		if(!cnt) {
			cout << "Case #" << test + 1 << ": Draw" << endl;
			continue;
		}
		else {
			cout << "Case #" << test + 1 << ": Game has not completed" << endl;
			continue;
		}
	}
	return 0;
}