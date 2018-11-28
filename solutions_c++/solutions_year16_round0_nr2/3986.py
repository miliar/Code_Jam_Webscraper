#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <functional>
#include <algorithm>
#include <iostream>
using namespace std;

int T;
string pancake;

int flip(int cur, int num, int tot) {
	int ret = 0;

	int rest = cur & ((1 << (tot - num)) - 1);
	cur >>= (tot - num);

	for (int i = 0; i < num; i++) {
		ret = (ret << 1) | (!(cur & 1));
		cur >>= 1;
	}

	return (ret << (tot - num)) | rest;
}

int main() {
	scanf("%d", &T);
	for (int test = 1; test <= T; test++) {
		cin >> pancake;
		int size = pancake.size();
		printf("Case #%d: ", test);

		queue<int> que;
		map<int, int> step;

		int first = 0;
		for (int i = 0; i < size; i++) {
			first = (first << 1) | (pancake[i] == '+' ? 0 : 1);
		}

		if (first == 0) {
			puts("0");
			continue;
		}

		que.push(first);
		step[first] = 0;
		while (!que.empty()) {
			int head = que.front(); que.pop();

			for (int i = 1; i <= size; i++) {
				int next = flip(head, i, size);
				if (!step.count(next)) {
					step[next] = step[head] + 1;
					if (next == 0) goto result;
					que.push(next);
				}
			}
		}

result:
		printf("%d\n", step[0]);
	}
	return 0;
}
