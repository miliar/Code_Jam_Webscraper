#include <cstdio>
#include <vector>

int main(void) {
	int t;
	char pen[200];
	freopen("B-large.in", "r", stdin);
	freopen("outputL.txt", "w", stdout);
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		scanf("%s", pen);
		std::vector<bool> data;
		for (int i = 0; pen[i] != '\0'; i++) {
			data.push_back(pen[i] == '+' ? 1 : 0);
		}
		int count = 0;
		for (int i = data.size() - 1; i >= 0; i--) {
			if (data[i] == 0) {
				int flag = 0;
				for (int j = 0;; j++) {
					if (data[j] == 1) {
						data[j] = 0;
						flag = 1;
					}
					else break;
				}
				if (flag) count++;
				std::reverse(data.begin(), data.begin() + i + 1);
				for (int j = 0; j <= i; j++) {
					data[j] = (data[j] == 0 ? 1 : 0);
				}
				count++;
			}
		}
		printf("Case #%d: %d\n",i, count);
	}
}