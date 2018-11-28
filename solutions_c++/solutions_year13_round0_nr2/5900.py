#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <memory.h>
using namespace std;

int direct[4][2] = {1 , 0 , -1 , 0 , 0 , 1 , 0 , -1 };
int a[150][150];
bool gash[150][150];

bool dfs(int x , int y , int d , int n , int m , int target) {
	if (x < 0 || x >= n || y < 0 || y >= m) return true;
	if (a[x][y] > target) return false;
	int tempx = x + direct[d][0];
	int tempy = y + direct[d][1];
	bool temp = dfs(tempx , tempy , d , n , m , target);
	if (temp) {
		if (a[x][y] == target)
			gash[x][y] = true;
		return true;
	}
	else {
		return false;
	}
}
 
int main() {
	//freopen("B-small-attempt0.in" , "r" , stdin);
	//freopen("B-small-out" , "w" , stdout);

	int T;
	int n , m;
	int cas = 0;
	scanf("%d" , &T);
	while (T--) {
		cas++;
		scanf("%d %d" , &n , &m);
		for (int i=0 ; i<n ; i++) {
			for (int j=0 ; j<m ; j++) {
				scanf("%d" , &a[i][j]);
			}
		}
		
		memset(gash , 0 , sizeof(gash));
		if (a[0][0] != 100) {
			dfs(0 , 0 , 0 , n , m , a[0][0]);
			dfs(0 , 0 , 2 , n , m , a[0][0]);
		}
		if (a[0][m - 1] != 100) {
			dfs(0 , m - 1 , 0 , n , m , a[0][m - 1]);
			dfs(0 , m - 1 , 3 , n , m , a[0][m - 1]);
		}
		if (a[n - 1][0] != 100) {
			dfs(n - 1 , 0 , 1 , n , m , a[n - 1][0]);
			dfs(n - 1 , 0 , 2 , n , m , a[n - 1][0]);
		}
		if (a[n - 1][m - 1] != 100) {
			dfs(n - 1 , m - 1 , 1 , n , m , a[n - 1][m - 1]);
			dfs(n - 1 , m - 1 , 3 , n , m , a[n - 1][m - 1]);
		}

		for (int i=0 ; i<m ; i++) {
			if (a[0][i] != 100) {
				dfs(0 , i , 0 , n , m , a[0][i]);
			}
			if (a[n - 1][i] != 100) {
				dfs(n - 1 , i , 1 , n , m , a[n - 1][i]);
			}
		}

		for (int i=0 ; i<n ; i++) {
			if (a[i][0] != 100) {
				dfs(i , 0 , 2 , n , m , a[i][0]);
			}
			if (a[i][m - 1] != 100) {
				dfs(i , m - 1 , 3 , n , m , a[i][m - 1]);
			}
		}

		bool ans = true;
		for (int i=0 ; i<n ; i++) {
			for (int j=0 ; j<m ; j++) {
				if (a[i][j] != 100 && gash[i][j] == false) {
					ans = false;
					break;
				}
			}
			if (!ans) break;
		}
		if (ans)
			printf("Case #%d: YES\n" , cas);		
		else 
			printf("Case #%d: NO\n" , cas);
	}	
	return 0;
}
