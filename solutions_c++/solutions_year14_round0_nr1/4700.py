#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

#define EPS 1e-8
#define MAXN 100005
#define MAXE 1005

typedef pair<int, int> pii;
typedef long long ll;

int T;
int g[2];
int a[2][4][4];

int main() {
	scanf("%d", &T);
	for (int nCase = 1; nCase <= T; ++nCase) {
		for (int k = 0; k < 2; ++k) {
			scanf("%d", g + k); g[k]--;
			for (int i = 0; i < 4; ++i) {
				for (int j = 0; j < 4; ++j) {
					scanf("%d", &a[k][i][j]);
				}
			}
		}
		
		vector<int> same;
		for (int c1 = 0; c1 < 4; ++c1) {
			for (int c2 = 0; c2 < 4; ++c2) {
				if (a[0][ g[0] ][c1] == a[1][ g[1] ][c2]) {
					same.push_back(a[0][ g[0] ][c1]);
					break;
				}
			}
		}

		printf("Case #%d: ", nCase);
		int n = same.size();
		if (n == 1) {
			printf("%d\n", same[0]);
		} else if (n > 1) {
			printf("Bad magician!\n");
		} else {
			printf("Volunteer cheated!\n");
		}
	}

	return 0;
}


