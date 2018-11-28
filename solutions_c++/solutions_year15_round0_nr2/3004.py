#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
const int N = 1010;

int n, a[N];

inline void GMAX(int &x, int y){ x = x < y ? y : x; }

int main(){
	
	int tcase; scanf("%d", &tcase);
	for (int i = 1; i <= tcase; ++ i){
		scanf("%d", &n);
		int r = -1, ans = -1;
		for (int j = 1; j <= n; ++ j) scanf("%d", &a[j]), GMAX(r, a[j]);
		for (int j = 1; j <= r; ++ j){
			int tmp = 0;
			for (int k = 1; k <= n; ++ k)
				if (a[k] > j) tmp += (a[k] - 1) / j;
			tmp += j;
			if (tmp < ans || ans == -1) ans = tmp;
		}
		printf("Case #%d: %d\n", i, ans);
	}

	return 0;
}
