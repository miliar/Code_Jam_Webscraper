#include <iostream>
#include <cstdio>
#include <utility>

using namespace std;

int row_max[100];
int col_max[100];

int grass[100][100];

int main(){
	int T, N, M;
	
	cin >> T;
	for(int t = 1; t <= T; t++){
		cin >> N >> M;
		
		for(int i = 0; i < N; i++){
			for(int j = 0; j < M; j++){
				cin >> grass[i][j];
				
				if(i == 0)
					col_max[j] = grass[i][j];
				else
					col_max[j] = max(col_max[j], grass[i][j]);
					
				if(j == 0)
					row_max[i] = grass[i][j];
				else
					row_max[i] = max(row_max[i], grass[i][j]);
			}
		}
		
		bool ok = true;
		for(int i = 0; ok && i < N; i++){
			for(int j = 0; ok && j < M; j++){
				if(grass[i][j] != row_max[i] && grass[i][j] != col_max[j])
					ok = false;
			}
		}
		
		cout << "Case #" << t << ": " << (ok ? "YES" : "NO") << "\n";
	}	
}
