#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>

using namespace std;

int n, s0;
char able[30][30];
bool now_able[30][30];

bool check(int k) {
	vector<int> order;
	for (int i = 0; i < n; i++)
		if (now_able[k][i])
			order.push_back(i);
		
	bool all_permutation = true;
	while (all_permutation) {
		int done = 0;
		for (int i = 0; i < n && done < order.size(); i++)
			if (i != k && now_able[i][order[done]])
				done++;
		if (done >= order.size())
			return false;
		all_permutation = next_permutation(order.begin(), order.end());
	}
	return true;
}

int solve(int s) {
	int ret = 0;
	for (int i = 0; i < n * n; i++)
		if (((s >> i) & 1) < ((s0 >> i) & 1))
			return n * n;
		else if (((s >> i) & 1) > ((s0 >> i) & 1))
			ret++;

	int idx = 0;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			now_able[i][j] = (s >> (idx++)) & 1;

	for (int i = 0; i < n; i++) {
		if (!check(i))
			return n * n;
	}
	return ret;
}

void Work() {
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		scanf("%s", able[i]);
	int idx = 0;
	s0 = 0;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			s0 = s0 | ((able[i][j] == '1') << idx++);

	int ans = n * n;
	for (int s = 0; s < (1 << (n * n)); ++s){
		int now_ans = solve(s);
		ans = min(ans, now_ans);
	}
	printf("%d", ans);
}

int main(int argc, char** argv) {
	int case_number;
	scanf("%d", &case_number);
	for (int i = 0; i < case_number; i++) {
		printf("Case #%d: ", i + 1);
		Work();
		printf("\n");
	}
	return 0;
}
