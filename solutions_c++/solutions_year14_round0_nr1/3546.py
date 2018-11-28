#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <cassert>
#include <cstring>
#include <vector>

using namespace std;

int a, b, t, f[5][5];
int A[20];

void solve(int t) {
	scanf("%d", &a);
	memset(A, 0, sizeof(A));

	for (int i = 1 ; i <= 4 ; i ++)
		for (int j = 1 ; j <= 4 ; j ++) {
			scanf("%d", &f[i][j]);
			if (i == a) 
				A[f[i][j]] ++;
		}
	
	scanf("%d", &a);
	vector<int> ansv;
	for (int i = 1 ; i <= 4 ; i ++)
		for (int j = 1 ; j <= 4 ; j ++) {
			scanf("%d", &f[i][j]);
			if (i == a && A[f[i][j]] == 1) {
				ansv.push_back(f[i][j]);
			}
		}
	if (ansv.size() == 0) 
		printf("Case #%d: Volunteer cheated!\n", t);
	else if (ansv.size() > 1)
		printf("Case #%d: Bad magician!\n", t);
	else
		printf("Case #%d: %d\n", t, ansv[0]);
}



int main() {
	//assert(freopen("input.txt", "r", stdin));
	//assert(freopen("output.txt", "w", stdout));
	scanf("%d", &t);
	for (int i = 1 ; i <= t ; i ++) {
		solve(i);
	}
	return 0;
}