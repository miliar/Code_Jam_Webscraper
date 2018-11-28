#include <iostream>
#include <cstdio>
using namespace std;


int main() {
	freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

	int N, A, B;
	cin >> N;

	int nums[] = {1, 4, 9, 121, 484};

	for (int i = 1; i <= N; ++i)
	{
		cin >> A >> B;
		int counter = 0;
		for (int j = 0; j < 5; ++j) {
			if (B < nums[j]) {
				break;
			}
			if (A <= nums[j] && nums[j] <= B) {
				++counter;
			}
		}
		printf("Case #%d: %d\n", i, counter);
	}				

	return 0;
}