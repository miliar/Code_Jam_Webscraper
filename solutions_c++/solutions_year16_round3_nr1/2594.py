#include <stdio.h>
#include <algorithm>
#include <vector>
using namespace std;

int T;

int mps[26];

std::vector<int> find_maxes(int n[], int s) {
	std::vector<int> res;
	res.push_back(-1);
	for(int i = 0; i < s; ++i) {
		if (res[0] == -1) {
			if (n[i] > 0) {
				res.clear();
				res.push_back(i);
			}
			continue;
		}
		if (n[i] > n[res[0]]) {
			res.clear();
			res.push_back(i);
			continue;
		}
		if (n[i] == n[res[0]]) {
			res.push_back(i);
			continue;
		}
	}
	if (res[0] < 0) {
		res.clear();
	}
	return res;
}

int main() {
	int i, T, n, j;
	scanf("%d", &T);
	i = 0;
	while (i < T) {
		j = 0;
		printf("Case #%d: ", ++i);
		scanf("%d", &n);
		while (j < n)
			scanf("%d", &mps[j++]);
		std::vector<int> p;
		while (!(p = find_maxes(mps, n)).empty()) {
			if (p.size() % 2) {
				int a = p.back();
				p.pop_back();
				printf("%c ", a + 'A');
				mps[a]--;
			}
			while (!p.empty()) {
				int a = p.back();
				p.pop_back();
				int b = p.back();
				p.pop_back();
				printf("%c%c ", a + 'A', b + 'A');
				mps[a]--; mps[b]--;

			}
		}
		putchar('\n');
	}
}
