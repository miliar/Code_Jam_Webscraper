#include <cstdio>
#include <algorithm>

bool carryOut() {
	const int MAX = 100;
	int N, M, lawn[MAX][MAX], rowMax[MAX], columnMax[MAX];
	
	scanf("%d %d", &N, &M);
	
	for(int i = 0; i < std::max(N, M); ++i)
		rowMax[i] = columnMax[i] = 1;
	
	for(int y = 0; y < N; ++y) {
		for(int x = 0; x < M; ++x) {
			scanf("%d", &lawn[y][x]);
			//printf( "(%d, %d) : %d rowMax[%d] %d colMax[%d] %d\n", x, y, lawn[y][x], y, rowMax[y], x, columnMax[x]);
			rowMax[y] = std::max(rowMax[y], lawn[y][x]);
			columnMax[x] = std::max(columnMax[x], lawn[y][x]);
		}
	}
	
	for(int y = 0; y < N; ++y) {
		for(int x = 0; x < M; ++x) {
			if(lawn[y][x] < rowMax[y] && lawn[y][x] < columnMax[x]) {
				//printf("(%d, %d) = %d : row %d col %d\n", x, y, lawn[y][x], rowMax[x], columnMax[y]);
				return false;
			}
		}
	}
	
	return true;
}

int main() {
	int T;
	
	scanf("%d", &T);
	for(int testCase = 1; testCase <= T; ++testCase) {
		if(carryOut())
			printf("Case #%d: YES\n", testCase);
		else
			printf("Case #%d: NO\n", testCase);
	}
}
