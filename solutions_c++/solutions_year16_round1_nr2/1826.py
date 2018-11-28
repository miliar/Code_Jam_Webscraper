#include <stdio.h>
#include <algorithm>
#include <string>
#include <cstring>

using namespace std;

const int N = 105, K = 2505;
int a[N][N];
int u[K];



void solve2() {

	int n;
	scanf("%d", &n);
	for (int i = 0; i < 2 * n - 1; i++) {
		for (int j = 0; j < n; j++) {
			scanf("%d", &a[i][j]);
			++u[a[i][j]];
		}
	}

	for (int i = 0; i < K; i++) {
		if( u[i] & 1 )
			printf("%d ", i);
		u[i] = 0;
	}

	puts("");
}

int main() {
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for(int R=1; R<=T; R++){
		printf("Case #%d: ", R);
		solve2();
		
	}

}