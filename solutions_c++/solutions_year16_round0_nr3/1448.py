#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;
typedef long long ll;

void printJamCoin(int n, int a, int b, int c, int d, int e, int f) {
	vector<int> v(n,0);
	v[a] = v[b] = v[c] = v[d] = v[e] = v[f] = 1;

	for(const auto &c : v)
		printf("%d", c);

	for(int i=2 ; i<=10 ; i++)
		printf(" %d", i+1);
	printf("\n");
	return;
}

void solve(int n, int J) {
	int cnt = 0;

	for(int i=1 ; i<n-1 ; i++) {
		for(int j=i+1 ; j<n-1 ; j+=2) {
			for(int k=j+1 ; k<n-1 ; k+=2) {
				for(int l=k+1 ; l<n-1 ; l+=2) {
					cnt++;
					printJamCoin(n,0,i,j,k,l,n-1);

					if(cnt == J) return;
				}
			}
		}
	}
}

int main() {

	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);

	int T;
	scanf("%d", &T);

	for (int tc = 1; tc <= T; tc++) {
		int n, j;
		scanf("%d%d", &n, &j);

		printf("Case #%d:\n", tc);
		solve(n, j);
	}

	return 0;
}