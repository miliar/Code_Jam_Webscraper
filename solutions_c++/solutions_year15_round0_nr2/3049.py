#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;
typedef long long ll;

int p[1111], D;
int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int _;
	scanf("%d", &_);
	for(int ca = 1; ca <= _; ++ca) {
		scanf("%d", &D);
		for(int i = 0; i < D; ++i) {
			scanf("%d", &p[i]);
		}
		int mint = 1000111;
		for(int len = 1; len <= 1000; ++len) {
			int ad = 0;
			for(int i = 0; i < D; ++i) {
				ad += (p[i] + len - 1) / len - 1;
			}
			mint = min(mint, ad + len);
		}
		printf("Case #%d: %d\n", ca, mint);
	}
	return 0;
}