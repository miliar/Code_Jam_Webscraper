#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;

int main()
{
	int T;

	cin >> T;
	for (int i = 1; i <= T; i++) {
		int N;
		int num[5000];

		cin >> N;
		for (int j = 0; j < 2 * N*N - N; j++)
			cin >> num[j];

		printf("Case #%d: ", i);

		sort(num, num + 2*N*N - N);
		for (int j = 0; j < 2 * N*N - N; j++) {
			if (num[j] == num[j + 1]) {
				j++; continue;
			}
			printf("%d ", num[j]);
		}
		printf("\n");
	}

	return 0;
}