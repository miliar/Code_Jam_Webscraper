#include <iostream>
#include <cstdio>

using namespace std;

int main(void) {
	ios_base::sync_with_stdio(false), cin.tie(0);
	freopen("Problem A.in", "r", stdin);
	freopen("Problem A.out", "w", stdout);

	int T;
	scanf("%d\n", &T);
	for (int test = 1; test <= T; test++) {
		int sMax = 0;
		char audience[1002] = { 0 };
		scanf("%d %s", &sMax, &audience);
		
		int result = 0, prevSum = 0;
		for (int i = 0; i <= sMax; i++) {
			audience[i] -= '0';
			if (prevSum < i) {
				result += i - prevSum;
				prevSum = i;
			}
			prevSum += audience[i];
		}

		printf("Case #%d: %d\n", test, result);

	}

	cout.flush();
	return 0;
}
