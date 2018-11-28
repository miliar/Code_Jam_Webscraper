#include <iostream>
#include <stdio.h>
#include <set>
using namespace std;
char grid[101][101];
int tc, row, col;
int answer = 0;
typedef pair<int,int> pi;
set<pi> s;
set<pi> s2;

bool cycle(int a, int b){
	if (grid[a][b] == '^'){
		
		for (int i = a - 1; i >= 0; i--){
			if (grid[i][b] != '.') return true;
		}
		
		answer = answer + 1;
		return false;
		
	} else if (grid[a][b] == 'v'){
		
		for (int i = a + 1; i < row; i++){
			if (grid[i][b] != '.') return true;
		}
		
		answer = answer + 1;
		return false;
		
	} else if (grid[a][b] == '>'){
		
		for (int i = b + 1; i < col; i++){
			if (grid[a][i] != '.') return true;
		}
		
		answer = answer + 1;
		return false;
		
		
	} else {
		
		for (int i = b - 1; i>= 0; i--){
			if (grid[a][i] != '.') return true;
		}
		
		answer = answer + 1;
		return false;
		
	}
}

bool check(int a, int b){
	

	for (int i = a - 1; i >= 0; i--){
		if (grid[i][b] != '.') return true;
	}
		
	for (int i = a + 1; i < row; i++){
		if (grid[i][b] != '.') return true;
	}
		
	for (int i = b + 1; i < col; i++){
		if (grid[a][i] != '.') return true;
	}
		
	for (int i = b - 1; i>= 0; i--){
		if (grid[a][i] != '.') return true;
	}
	
	
	return false;
}

int main(){
	
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	bool skip = false;
	scanf("%d", &tc);
	for (int i = 0; i < tc; i++){
		scanf("%d%d", &row, &col);
		answer = 0;
		s.clear();
		s2.clear();
		for (int j = 0; j < row; j++){
			for (int k = 0; k < col; k++){
				scanf(" %c", &grid[j][k]);
				if (grid[j][k] != '.'){
					s2.insert(make_pair(j, k));
				}
			}
		}
		
		bool skip = false;
		
		for (set<pi>::iterator it = s2.begin(); it != s2.end(); it++){
			if (cycle(it -> first, it -> second) == false){
				s.insert(*it);
			}
		}
		
		for (set<pi>::iterator it = s.begin(); it != s.end(); it++){
			if (check(it -> first, it -> second) == false){
				printf("Case #%d: IMPOSSIBLE\n", i + 1);
				skip = true;
				break;
			}
		}
		
		if (skip == true){
			continue;
		}
		
		printf("Case #%d: %d\n", i + 1, answer);
		
		
	}
	
	
	
	
	
	
}
