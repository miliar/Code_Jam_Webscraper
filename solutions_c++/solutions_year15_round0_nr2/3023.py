// Infinite House of Pancakes

#include <cstdio>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

void calc() {
	int dishCount;
	vector<int> pancakes;
	int i, j;
	int ans, temp;

	scanf("%d", &dishCount);
	pancakes.resize(dishCount);
	for (i = 0; i < dishCount; i++) {
		scanf("%d", &pancakes[i]);
	}

	sort(pancakes.begin(), pancakes.end(), greater<int>());

	for (i = 1; i <= 1000; i++) {
		temp = min(i, pancakes[0]);
		for (j = 0; j < dishCount; j++) {
			temp += pancakes[j] / i - (pancakes[j] % i == 0 ? 1 : 0);
		}
		if (i == 1 || temp < ans) {
			ans = temp;
		}
	}

	printf("%d\n", ans);
}

int main() {
	int testcase, t;

	scanf("%d", &testcase);
	for (t = 1; t <= testcase; t++) {
		printf("Case #%d: ", t);

		calc();
	}

	return 0;
}