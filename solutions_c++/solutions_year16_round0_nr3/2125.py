#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstring>
#include <string>
#include <map>
#include <queue>
#include <set>
#include <ctime>
#include <cstdlib>

#define LL long long int
#define FOR(i, s, e) for (int i=(s); i<(e); i++)
#define FOE(i, s, e) for (int i=(s); i<=(e); i++)
#define CLR(x, a) memset(x, a, sizeof(x))

using namespace std;

int test;

int p[11] = {0, 0, 3, 2, 5, 2, 7, 2, 3, 2, 11};

int mod[11][100];
int x[100], c[11];

int ans[505][100];

int n = 32, Q = 500, cnt = 0;

int main(){
	
	srand(time(0));
	
	FOR(i, 2, 11) {
		mod[i][0] = 1;
		FOR(j, 1, n) mod[i][j] = (mod[i][j - 1] * i) % p[i];
	}
	
	printf("Case #1:\n");
	
	x[0] = x[n - 1] = 1;
	
	while (Q) {
		FOR(i, 2, 11) c[i] = (mod[i][n - 1] + mod[i][0]) % p[i];
		
		FOR(j, 1, n - 1) {
			x[j] = rand() % 2;
			if (x[j] == 1) {
				FOR(i, 2, 11)
					c[i] = (c[i] + mod[i][j]) % p[i];
			}
		}
		
		int ok = 1;
		FOR(i, 2, 11) if (c[i] != 0) ok = 0;
		
		if (ok) {
			
			int yes = 1;
			FOR(i, 0, cnt) {
				int ok = 0;
				FOR(j, 0, n) if (x[j] != ans[i][j]) {ok = 1; break;}
				if (!ok) { yes = 0; break; }
			}
			
			if (yes) {
				FOR(j, 0, n) ans[cnt][j] = x[j];
				cnt++;
				for (int i=n-1; i>=0; i--) printf("%d", x[i]);
				FOR(i, 2, 11) printf(" %d", p[i]);
				printf("\n");
				Q--;
			}
		}
	}

	return 0;
}
