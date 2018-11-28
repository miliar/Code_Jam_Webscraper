#include <cstdio>
#include <cmath>

static unsigned int A, B, a, b;
static char number[4];

void get_arguments() {
	scanf("%d%d", &A, &B);
	a = ceil(sqrt((double)A)); b = floor(sqrt((double)B));
}

bool palyndromous(int n) {
	bool ret = true;
	int size = 0;
	while (n > 0) {
		number[size] = n%10;
		n /= 10;
		++size;
	}
	for (int i = 0; ret && i < size/2; ++i) {
		if (number[i] != number[size-1-i]) ret = false;
	}
	return ret;
}

int solve_problem() {
	int ret = 0;
	for (int n = a; n <= b; ++n) {
		if (palyndromous(n) && palyndromous(n*n)) ++ret;
	}
	return ret;
}

int main(int argc, char *argv[]) {
	int ncases;
	scanf("%d", &ncases);
	for (int n = 0; n < ncases; ++n) {
		get_arguments();
		printf("Case #%d: %d\n", n+1, solve_problem());
	}
	return 0;
}