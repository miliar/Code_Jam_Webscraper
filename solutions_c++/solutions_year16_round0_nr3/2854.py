#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>

using namespace std;

const int N_MAX = 16;
const int J_MAX = 50;

int tab[N_MAX] = {1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1};

long long int get_smallest_divisor(long long int n) {
	if (n % 2 == 0) return 2;
	else {
		long long int n_sqrt = (long long int) floor(sqrt(n));
		for (long long int i = 3; i < n_sqrt; ++i) {
			if (n % i == 0) return i;
		}
		return -1;
	}
}

long long int convert(int base) {
	long long int result = 0;
	long long int b = 1;
	for (int i = N_MAX - 1; i >= 0; --i) {
		if (tab[i] == 1)
			result += b;
		b *= base;
	}
	return result;
}

void print_result(long long int *r) {
	for (int i = 0; i < N_MAX; ++i) {
		printf("%d", tab[i]);
	}
	printf(" ");
	for (int b = 2; b <= 10; ++b) {
		printf("%lld ", r[b]);
	}
	printf("\n");
}

int check() {
	int ile = 0;
	long long int result[10];
	for (int b = 2; b <= 10; ++b) {
		result[b] = get_smallest_divisor(convert(b));
		if (result[b] > 1) {
			++ile;
		}
	}
	if (ile == 9) {
		print_result(result);
		return 1;
	}
	return 0;
}

void add() {
    for (int i = N_MAX - 2; i > 0; --i) {
    	if (tab[i] == 1) {
    		tab[i] = 0;
    	} else {
    		tab[i] = 1;
    		return;
    	}
    }
}

void print_array(int n, int *A) {
	for (int i = 0; i < n; ++i) {
		printf("%d", A[i]);
	}
	printf("\n");
}

int main() {
	int j = 0;
	printf("Case #1:\n");
	while (j < J_MAX) {
		j += check();
    	add();
	}
	return 0;
}