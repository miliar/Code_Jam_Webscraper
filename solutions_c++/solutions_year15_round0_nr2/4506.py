#include<bits/stdc++.h>
using namespace std;

bool cmp(int a, int b) {
	return a > b;
}

int main() {
	int N, n;
	int T;
	scanf("%d", &T);
	for (int ans1 = 1; ans1 <= T; ans1++) {
		scanf("%d", &N);
		vector<int> din, din2;
		int ans2 = 0;
		for (int i = 0; i < N; i++) {
			scanf("%d", &n);
			ans2 = max(ans2, n);
			din.push_back(n);
			din2.push_back(n);
		}

		int temp = 0;
		while (true) {
			if (din.size() == 0) break;
			sort(din.begin(), din.end(), cmp);
			int cur = din[0];
			int tt = temp + cur;
			ans2 = min(ans2, tt);
			if (cur <= 3)
				break;
			if (cur == 6) {
				din[0] = 3;
				din.push_back(3);
			} else if (cur == 9) {
				din[0] = 3;
				din.push_back(6);
			} else if (cur % 2 == 0) {
				din[0] = cur / 2;
				din.push_back(cur / 2);
			} else {
				din[0] = cur / 2 + 1;
				din.push_back(cur / 2);
			}
			temp++;
		}

		temp = 0;
		while (true) {
			if (din2.size() == 0) break;
			sort(din2.begin(), din2.end(), cmp);
			int cur = din2[0];
			int tt = temp + cur;
			ans2 = min(ans2, tt);
			if (cur <= 3)
				break;
			if (cur % 2 == 0) {
				din2[0] = cur / 2;
				din2.push_back(cur / 2);
			} else {
				din2[0] = cur / 2 + 1;
				din2.push_back(cur / 2);
			}
			temp++;
		}

		printf("Case #%d: %d\n", ans1, ans2);
	}
}
