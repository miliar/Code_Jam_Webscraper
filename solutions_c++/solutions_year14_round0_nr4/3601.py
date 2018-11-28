#include <cstdio>
#include <algorithm>
#define NMAX 1024
using namespace std;

void solve() {
	char Uz[NMAX];
	double A[NMAX], B[NMAX];
	int n;
	
	scanf("%d", &n);
	for(int i = 0; i < n; ++i)
		scanf("%lf", A + i), Uz[i] = 0;
	for(int i = 0; i < n; ++i)
		scanf("%lf", B + i);
	
	sort(A, A + n);
	sort(B, B + n);
	
	int p = 0;
	for(int i = 0; i < n; ++i)
		if(A[i] > B[p])
			++p;
	printf("%d ", p);
	
	p = 0;
	for(int i = 0; i < n; ++i) {
		int j = 0;
		for(;j < n; ++j)
			if(!Uz[j] && B[j] > A[i]) {
				Uz[j] = 1;
				break;
			}
		if(j == n)
			++p;
	}
	printf("%d\n", p);
}

int main() {
	// freopen("input.txt", "r", stdin);
	freopen("D-large.in.txt", "r", stdin);
	freopen("D-large.out", "w", stdout);
	
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; ++i) {
		printf("Case #%d: ", i);
		solve();
	}
	
	return 0;
}