#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>
#include <memory.h>
using namespace std;

// 1, 2, 3, 11, 22
int main() {
	int cases;
	int caseId = 1;

	freopen("input", "r", stdin);
	freopen("output", "w", stdout);

	scanf("%d", &cases);
	while (cases--) {
		int A, B, answer = 0;
		scanf("%d%d", &A, &B);
		if (A <= 1 && 1 <= B)
			answer++;
		if (A <= 4 && 4 <= B)
			answer++;
		if (A <= 9 && 9 <= B)
			answer++;
		if (A <= 121 && 121 <= B)
			answer++;
		if (A <= 484 && 484 <= B)
			answer++;
		printf("Case #%d: %d\n", caseId++, answer);
	}
	return 0;
}

