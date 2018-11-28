#include <cstdio>
#include <vector>

using namespace std;

int size;
int relation[10];
vector<int> circle;
int circleSize;
int isAdded[10] = {};

int ans;

void calc() {
	int i;

	// Case THIS_IS_ENOUGH
	bool check = true;
	for (i = 0; i < circleSize; i++) {
		int left = circle[(i + 1) % circleSize];
		int right = circle[(i + circleSize - 1) % circleSize];
		if (relation[circle[i]] != left && relation[circle[i]] != right) {
			check = false;
			break;
		}
	}
	if (check) {
		if (circleSize > ans) {
			ans = circleSize;
		}
	}

	// Case I_WANT_MORE
	for (i = 0; i < size; i++) {
		if (isAdded[i] == 0) {
			isAdded[i] = 1;
			circle[circleSize] = i;
			circleSize++;
			
			calc();
			
			isAdded[i] = 0;
			circleSize--;
		}
	}
}

void calcCase() {
	int i, j;

	scanf("%d", &size);
	circle.resize(size);
	for (i = 0; i < size; i++) {
		scanf("%d", &relation[i]);
		relation[i]--;
		isAdded[i] = 0;
	}

	circleSize = 0;
	ans = 0;

	calc();

	printf("%d\n", ans);
}

int main() {
	int tc, t;

	scanf("%d", &tc);
	for (t = 1; t <= tc; t++) {
		printf("Case #%d: ", t);
		calcCase();
	}
	return 0;
}