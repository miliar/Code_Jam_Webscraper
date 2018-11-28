#include <cstdio>
using namespace std;

int counter = 0;
void make() {
	printf("Case #%d: ", ++counter);

	int r; 
	long long t;
	scanf("%d %lld", &r, &t);

	int n = 0;
	while(t > 0) {
		t -= ((r + 1) * (r + 1)) - (r * r);
		if(t >= 0)
			n++;

		r += 2;
	}

	printf("%d\n", n);
}

int main() {
	int t; scanf("%d", &t);
	while(t--) {
		make();
	}
	return 0;
}
