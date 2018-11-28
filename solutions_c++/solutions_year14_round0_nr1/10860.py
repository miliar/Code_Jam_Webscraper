#include<iostream>
#include<cstring>

using namespace std;

#define SIZE 16

int main() {
	int T;
	cin >> T;

	int testcase = 0;

	while (++testcase <= T) {
		int N, answer, count = 0;

		int arr[SIZE];

		memset(arr, 0, sizeof(int) * SIZE);

		for (int i = 0; i < 2; ++i) {
			cin >> N;
			for (int loop = 0; loop < SIZE; ++loop) {
				int a;
				cin >> a;

				if (loop / 4 == N - 1) {
					++arr[a - 1];
					if (arr[a - 1] == 2) {
						answer = a;
						++count;
					}
				}
			}
		}

		if (0 == count) {
			cout << "Case #" << testcase << ": Volunteer cheated!\n";
		} else if (1 == count) {
			cout << "Case #" << testcase << ": " << answer << "\n";
		} else {
			cout << "Case #" << testcase << ": Bad magician!\n";
		}

	}
}
