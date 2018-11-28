#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>

const int MAXN = 1111;

char pancake[MAXN];
bool flip[MAXN];

int main() {
	int task;
	scanf("%d", &task);
	for (int task_index = 1; task_index <= task; ++ task_index) {
		int k;
		scanf(" %s %d", pancake, &k);
		int n = strlen(pancake);
		for (int i = 0; i < n; ++ i) {
			flip[i] = false;
		}
		bool b = 0, ret = 1;
		int way = 0;
		for (int i = 0; i < n; ++ i) {
			if (i >= k && flip[i - k]) {
				b = !b;
			}
			if ((pancake[i] == '-') ^ b) {
				if (i + k <= n) {
					b = !b;
					++ way;
					flip[i] = 1;
				}
				else {
					ret = 0;
					break;
				}
			}
		}
		if (ret) {
			printf("Case #%d: %d\n", task_index, way);
		}
		else {
			printf("Case #%d: IMPOSSIBLE\n", task_index);
		}
	}
	return 0;
}

