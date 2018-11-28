#include <cstdio>
#include <iostream>
#include <cstring>
#define MAX 1005
using namespace std;

int main () {
	int t, n, current, need, added, x;
	char line[MAX];
	scanf("%d", &t);
	for (int num_case = 1; num_case <= t; num_case++) {
		scanf("%d %s", &n, line);
		added = 0;
		current = line[0] - '0';
		// printf("curr: %d\n", current);
		for (int i = 1; i <= n; i++) {
			need = line[i] - '0';
			// printf("need: %d\n", need);
			if (i  > current && need != 0) {
				added += (i - current);
				current += added;
			}
			current += need;
			// printf("current: %d\n", current);
		}
		printf("Case #%d: %d\n", num_case, added);
	}
	return 0;
}