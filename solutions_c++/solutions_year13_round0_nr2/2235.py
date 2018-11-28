#include<iostream>
using namespace std;

const int MAXN = 200;
int map[MAXN][MAXN];
int wmax[MAXN], hmax[MAXN];
int n, m;

bool test() {
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++) {
			//printf("map[%d][%d] = %d, wmax = %d, hmax = %d\n", i, j, map[i][j], wmax[i], hmax[j]);

			if (map[i][j] < wmax[i] && map[i][j] < hmax[j] 
				|| map[i][j] > 100)
				return false;
		}
	return true;
}

int main() {
	int testcases;
	cin >> testcases;
	for (int t = 0; t < testcases; t++) {
		cin >> n >> m;
		//printf("Case #%d: \n", t);
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				cin >> map[i][j];
				//printf("%d\t", map[i][j]);
			}
			//printf("\n");
		}
		for (int i = 0; i < n; i++) {
			wmax[i] = 1;
		}
		for (int i = 0; i < m; i++) {
			hmax[i] = 1;
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (map[i][j] > wmax[i])
					wmax[i] = map[i][j];
			}
		}
		for (int j = 0; j < m; j++) {
			for (int i = 0; i < n; i++) {
				if (map[i][j] > hmax[j])
					hmax[j] = map[i][j];
			}
		}
		printf("Case #%d: ", t + 1);
		if (test())
			printf("YES\n");
		else
			printf("NO\n");
	}
	return 0;
}