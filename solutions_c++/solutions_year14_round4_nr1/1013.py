#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <utility>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;
typedef long long ll;
typedef pair<int, int> P;


int N, X;
int pack[701];
int solve() {
	int tot=0;
	while (N > 0) {
		for (int i = 1; i <= X; i++)
		{
			if (pack[i] > 0) {
				pack[i] -= 1;
				--N;
				for (int j = X; j >= 1; j--)
				{
					if (j <= X-i && pack[j] > 0) {
						--N;
						--pack[j];
						break;
					}
				}
				++tot;
			}
		}
	}
	return tot;
}
int main() {
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; ++i) {
		scanf("%d %d", &N, &X);
		fill(pack, pack+X+1, 0);
		for (int j = 0; j < N; ++j) {
			int dx;
			scanf("%d", &dx);
			pack[dx] += 1;
		}
		int p = solve();
		printf("Case #%d: %d\n", i+1, p);
	}
	return 0;
}