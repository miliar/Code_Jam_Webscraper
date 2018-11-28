#include <iostream>
#include <stdio.h>
#include <vector>
using namespace std;

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int T, first, second;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i) {
		int data[16] = {0};

		scanf("%d", &first);
		for (int j = 0; j < 4; ++j) {
			for (int k = 0; k < 4; ++k) {
				int tmp;
				scanf("%d", &tmp);
				if (j == first-1) {
					++data[tmp-1];
				}
			}
		}

		vector<int> result;
		scanf("%d", &second);
		for (int j = 0; j < 4; ++j) {
			for (int k = 0; k < 4; ++k) {
				int tmp;
				scanf("%d", &tmp);
				if (j == second-1) {
					++data[tmp-1];
					if (data[tmp-1] == 2) {
						result.push_back(tmp);
					}
				}
			}
		}

		printf("Case #%d: ", i);
		if (result.size() == 0) {
			printf("Volunteer cheated!\n");
		} else if (result.size() == 1) {
			printf("%d\n", result[0]);
		} else {
			printf("Bad magician!\n");
		}
	}
	return 0;
}