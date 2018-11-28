#include <iostream>
using namespace std;

char* check(int m, int n, int area[101][101], int max){
	int max_m[101], max_n[101];


	for(int i = 0; i < m; i++){
		max_m[i] = 0;
		for(int j = 0; j < n; j++){
			if(area[i][j] > max_m[i])
				max_m[i] = area[i][j];
		}
		
	}

	for(int j = 0; j < n; j++){
		max_n[j] = 0;
		for(int i = 0; i < m; i++){
			if(area[i][j] > max_n[j])
				max_n[j] = area[i][j];
		}
	}

	for(int i = 0; i < m; i++){
		for(int j = 0; j < n; j++){
			if(area[i][j] < max_m[i] && area[i][j] < max_n[j])
				return "NO";
		}
	}

	return "YES";
}


int main(){
	freopen("test.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int k, m, n, area[101][101];
	scanf("%d", &k);
	for(int l = 0; l < k; l++){
		scanf("%d %d", &m, &n);
		int max = 0;
		for(int i = 0; i < m; i++)
			for(int j = 0; j < n; j++){
				scanf("%d", &area[i][j]);
				if(area[i][j] > max) max = area[i][j];
			}
		printf("Case #%d: %s\n", l+1, check(m, n, area, max));
	}
	
}