#include<stdio.h>
#include<iostream>
#include<math.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#define print(Z,a,b) for (int __z = a; __z < b; __z ++) cout << Z[__z] << " ";
#define scan(Z,a,b) for (int __z = a; __z < b; __z ++) cin >> Z[__z];
#define bit(_z) (1ll << _z)
using namespace std;

int t;
int M[11][11];

int r, c, m;

bool dfs(int y, int x, int tot) {
	if (tot == r * c - m)
		return true;
	if (tot > r * c - m)
		return false;
		
	int tot2 = tot;
	
	for (int i = max(y-1, 0); i <= min(y+1, r-1); i ++) {
		for (int j = max(x-1, 0); j <= min(x+1, c-1); j ++) {
			if (M[i][j] == 0) {
				M[i][j] = tot;
				++ tot2;
			}
		}
	}
	
	for (int i = max(y-1, 0); i <= min(y+1, r-1); i ++) {
		for (int j = max(x-1, 0); j <= min(x+1, c-1); j ++) {
			if (M[i][j] == tot) {
				if (dfs(i, j, tot2))
					return true;
			}
		}
	}
	
	for (int i = max(y-1, 0); i <= min(y+1, r-1); i ++) {
		for (int j = max(x-1, 0); j <= min(x+1, c-1); j ++) {
			if (M[i][j] == tot) {
				M[i][j] = 0;
			}
		}
	}
	
	return false;
}

int main () {
	cin >> t;
	
	int caze = 0;
	while (t --) {
		++ caze;
		
		cin >> r >> c >> m;
		
		printf("Case #%d:\n", caze);
		
		bool any = false;
		
		for (int y = 0; y < r and !any; y ++) {
		for (int x = 0; x < c and !any; x ++) {
		
			memset(M, 0, sizeof M);
			M[y][x] = 1;
			
			if (dfs(y, x, 1)) {
				for (int i = 0; i < r; i ++)
					for (int j = 0; j < c; j ++) {
						if (i == y and j == x)
							cout << "c";
						else if (M[i][j] > 0)
							cout << ".";
						else
							cout << "*";
						
						if (j == c - 1)
							cout << endl;
					}
				any = true;
			}
		}
		}
				
		if (!any)
			printf("Impossible\n");
	}
	
	return 0;
}  	
