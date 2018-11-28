#include <iostream>
#include <fstream>
#include <unordered_map>

using namespace std;

bool mark[10];
unordered_map<int, bool> *numberSeenMap;

int main () {
	int caseNo, N;
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	scanf("%d", &caseNo);
	int c = 1;

	while (c <= caseNo) {
		for (int j = 0; j < 10; j++) {
			mark[j] = false;
		}

		scanf("%d", &N);
		numberSeenMap = new unordered_map<int, bool>();

		int i = 1;
		while (true) {
			//printf("%d %d\n", i, N);
			int newN = i * N;
			if (numberSeenMap->find(newN) == numberSeenMap->end()) {
				numberSeenMap->insert(make_pair(newN, true));

				int tempN = newN;
				while (tempN > 0) {
					int digit = tempN % 10;
					mark[digit] = true;
					tempN /= 10;
				}

				bool allSet = true;
				for (int j = 0; j < 10; j++) {
					if (!mark[j]) {
						//printf("%d is not set\n", j);
						allSet = false;
						break;
					}
				}
				if (allSet) {
					printf("Case #%d: %d\n", c, newN);
					break;
				}

			} else {
				printf("Case #%d: INSOMNIA\n", c);
				break;
			}
			i++;
		}
		c++;
	}

	return 0;
}