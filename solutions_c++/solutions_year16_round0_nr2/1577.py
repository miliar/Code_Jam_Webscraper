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
	char s[120];
	char temp[120];
	fgets(s, 120, f);
	int n = strlen(s);
	while (s[n - 1] != '+' && s[n - 1] != '-')
		n--;

	int cnt = 0;
	while (true) {
		while (n > 0 && s[n - 1] == '+')
			n--;
		if (n <= 0)
			break;

		strncpy(temp, s, n);
		if (s[0] == '-') {
			for (int i = 0; i < n; i++)
				s[n - i - 1] = temp[i] == '+' ? '-' : '+';
		}
		else {
			int r = n;
			while (s[r - 1] == '-')
				r--;
			for (int i = 0; i < r; i++)
				s[r - i - 1] = temp[i] == '+' ? '-' : '+';
		}
		cnt++;
	}

	printf("%d\n", test + 1);
	fprintf(g, "Case #%d: %d\n", test + 1, cnt);
}

int main(int argc, char* argv[])
{
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

