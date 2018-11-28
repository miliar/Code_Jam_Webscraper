#include <cstdio>

bool process() {
	int map[100][100] = {0};
	int row[100] = {0}, col[100] = {0};
	int m,n;
	scanf("%d%d", &n, &m);

	for(int i = 0; i < n; i++)
		for(int j = 0; j < m; j++){
			scanf("%d", &(map[i][j]));
			if(map[i][j] > row[i]) row[i] = map[i][j];
			if(map[i][j] > col[j]) col[j] = map[i][j];
		}

	for(int i = 0; i < n; i++)
		for(int j = 0; j < m; j++)
			if(map[i][j] != row[i] && map[i][j] != col[j])
				return false;
	return true;
}

int main() {
	int n;
	scanf("%d", &n);

	for(int i = 0; i < n; i++){
		printf("Case #%d: %s\n", i + 1, process() ? "YES" : "NO");
	}

	return 0;
}