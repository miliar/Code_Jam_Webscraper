#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>


int T;

int helper[17];

void init() {
	for (int i = 1; i < 17; ++i)
		helper[i] = 0;
}

void solveCase() {
	init();
	int a[2];
	int v1, v2, v3, v4;
	for (int j = 0; j < 2; ++j) {
		std::cin >> a[j];
		for (int i = 1; i <= 4; ++i) {
			std::cin >> v1 >> v2 >> v3 >> v4;
			if (i == a[j]) {
				helper[v1]++;
				helper[v2]++;
				helper[v3]++;
				helper[v4]++;
			}
		}
	}

	int correct = -1;
	for (int i = 1; i < 17; i++) {
		if (helper[i] == 2) {
			correct = correct == -1 ? i : 17;
		}
	}
	switch (correct)
	{
	case 17: std::cout << "Bad magician!"; break;
	case -1: std::cout << "Volunteer cheated!"; break;
	default: std::cout << correct; break;
	}
}

int main() {
	freopen("A-small.in", "r", stdin);
	freopen("A-small.out", "w", stdout);
	std::cin >> T;
	for (int i = 1; i < T + 1; ++i)
	{
		std::cout << "Case #" << i << ": ";
		solveCase();
		if (i < T)
			std::cout << std::endl;
	}
	return 0;
}