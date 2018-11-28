#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <sstream>
using namespace std;

struct Item {
	Item(char c, int repeat) : c(c), repeat(repeat) {}
	char c;
	int repeat;
};

void split(string &str, vector<Item> &items) {
	items.push_back(Item(str[0], 1));
	for (int i = 1; i < str.size(); ++i) {
		if (str[i] == items.back().c)
			items.back().repeat++;
		else
			items.push_back(Item(str[i], 1));
	}
}

int dist(vector<int> &repeats) {
	auto mid = repeats.begin() + repeats.size() / 2;
	nth_element(repeats.begin(), mid, repeats.end());
	int ret = 0;
	for (int i = 0; i < repeats.size(); ++i) {
		ret += abs(repeats[i] - *mid);
	}
	return ret;
}

int solve(vector<vector<Item>> items) {
	for (int i = 0; i < items.size(); ++i) {
		if (items[i].size() != items[0].size())
			return -1;
	}

	int sum = 0;
	for (int j = 0; j < items[0].size(); ++j) {
		char c = items[0][j].c;
		vector<int> repeats;
		for (int i = 0; i < items.size(); ++i) {
			if (items[i][j].c != c)
				return -1;
			repeats.push_back(items[i][j].repeat);
		}
		sum += dist(repeats);
	}
	return sum;
}

int main() {
	int T; scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		int N; scanf("%d", &N);
		vector<string> strings;
		for (int i = 0; i < N; ++i) {
			char buff[111];
			scanf("%s", buff);
			strings.push_back(buff);
		}

		vector<vector<Item>> items;
		for (int i = 0; i < N; ++i) {
			items.push_back(vector<Item>());
			split(strings[i], items.back());
		}
		printf("Case #%d: ", t);
		int ans = solve(items);
		if (ans == -1)
			printf("Fegla Won\n");
		else
			printf("%d\n", ans);
	}
	return 0;
}