#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

#define MIN(a, b) (a < b ? a : b)
#define MAX(a, b) (a < b ? b : a)

void execute_next(int test, FILE *f, FILE *g) {
	int n;
	fscanf(f, "%d\n", &n);

	if (n == 0) {
		printf("%d\n", test + 1);
		fprintf(g, "Case #%d: %s\n", test + 1, "INSOMNIA");
		return;
	}
	set<int> digits;
	/*while (n % 10 == 0) {
		digits.insert(0);
		n /= 10;
	}*/

	unsigned long long m = n, temp;
	while (true) {
		temp = m;
		int i = 0;
		while (temp > 0) {
			i++;
			digits.insert(temp % 10);
			temp /= 10;
		}
		if (i >= 60) {
			printf("Attention!");
			abort();
		}
		if (digits.size() >= 10)
			break;
		m += n;
	}

	printf("%d\n", test + 1);
	fprintf(g, "Case #%d: %d\n", test + 1, m);
}

int main(int argc, char* argv[])
{

	/*FILE *ff = fopen("in.txt", "w");
	int n = 1000000;
	fprintf(ff, "%d\n", n+1);
	for (int i = 0; i <= n; i++) {
		fprintf(ff, "%d\n", i);
	}
	fclose(ff);
	return 0;*/

	FILE *f = fopen((argc > 1 ? argv[1] : "in.txt"), "r");
	FILE *g = fopen("out.txt", "w");
	int t;
	fscanf(f, "%d\n", &t);
	for (int test = 0; test < t; test++) {
		execute_next(test, f, g);
	}
	fclose(f);
	fclose(g);
	return 0;
}

