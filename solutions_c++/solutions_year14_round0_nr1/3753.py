#include <cstdio>
using namespace std;

void merge(int A[], int B[]) {
	int ans, nr = 0;
	for(int i = 0; i < 4; ++i)
		for(int j = 0; j < 4; ++j)
			if(A[i] == B[j])
				ans = A[i], ++nr;
	if(nr == 1)
		printf("%d\n", ans);
	if(!nr)
		printf("Volunteer cheated!\n");
	if(nr > 1)
		printf("Bad magician!\n");
}

void solve() {
	int A[4][4], B[4][4], r1, r2;
	scanf("%d", &r1);
	for(int i = 0; i < 4; ++i)
		for(int j = 0; j < 4; ++j)
			scanf("%d", &A[i][j]);
	scanf("%d", &r2);
	for(int i = 0; i < 4; ++i)
		for(int j = 0; j < 4; ++j)
			scanf("%d", &B[i][j]);
	
	merge(A[r1 - 1], B[r2 - 1]);
}

int main() {
	// freopen("A-small.in", "r", stdin);
	freopen("A-small-attempt0.in.txt", "r", stdin);
	freopen("A-small.out", "w", stdout);
	
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; ++i) {
		printf("Case #%d: ", i);
		solve();
	}
	
	return 0;
}