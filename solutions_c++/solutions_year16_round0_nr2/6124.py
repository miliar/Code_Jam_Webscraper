#include <iostream>
#include <fstream>
#include <unordered_map>
#include <string.h>

using namespace std;

int main () {
	int caseNo;
	char str[105];

	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	
	scanf("%d", &caseNo);
	int c = 1;

	while (c <= caseNo) {
		scanf("%s", str);

		int len = strlen(str);
		int cost = 0;
		if (str[0] == '-') {
			cost = 1;
		}

		for (int i = 1; i < len; i++) {
			if (str[i] == '-') {
				if (str[i-1] == '+') {
					cost += 2;
				}
			}
		}

		printf("Case #%d: %d\n", c, cost);
		c++;
	}

	return 0;
}