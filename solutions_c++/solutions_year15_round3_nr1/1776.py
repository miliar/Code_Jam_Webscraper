#include <cstdio>
#include <cstdlib>
using namespace std;
int go1(int r, int w) {
	return (r + w - 1) / w;
}
int go2(int r, int w) {
	if (r % w == 0) return r/w + w - 1;
	return r / w + w;
}
void Solve() {
	int a, b, c;
	scanf("%d%d%d", &a, &b, &c);
	printf("%d\n", (a-1)*go1(b,c)+go2(b,c));
}
int main() {
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		printf("Case #%d: ", i);
		Solve();
	}
	return 0;
}
