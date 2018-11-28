#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

const int Max = 200;

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests, a, b, k;
	scanf("%d", &tests);

	char s1[Max], s2[Max];
	int n, n1, n2;
	vector< pair<char, int> > v1;
	vector< pair<char, int> > v2;

	for (int t = 1; t <= tests; t++) {
		scanf("%d", &n);
		scanf("%s %s", s1, s2);
		n1 = strlen(s1);
		n2 = strlen(s2);

		v1.clear();
		v2.clear();

		v1.push_back(make_pair(s1[0], 1));
		for (int i = 1; i < n1; i++) {
			if (s1[i] == s1[i - 1]) {
				pair<char, int> prev = v1[v1.size() - 1];
				v1.pop_back();
				v1.push_back(make_pair(prev.first, prev.second + 1));
			} else {
				v1.push_back(make_pair(s1[i], 1));
			}
		}

		v2.push_back(make_pair(s2[0], 1));
		for (int i = 1; i < n2; i++) {
			if (s2[i] == s2[i - 1]) {
				pair<char, int> prev = v2[v2.size() - 1];
				v2.pop_back();
				v2.push_back(make_pair(prev.first, prev.second + 1));
			} else {
				v2.push_back(make_pair(s2[i], 1));
			}
		}

		if (v1.size() != v2.size()) {
			printf("Case #%d: Fegla Won\n", t);
			continue;
		}

		bool mismatch = false;
		for (int i = 0; i < v1.size(); i++) {
			if (v1[i].first != v2[i].first) {
				mismatch = true;
			}
		}

		if (mismatch) {
			printf("Case #%d: Fegla Won\n", t);
			continue;
		}

		int steps = 0;
		for (int i = 0; i < v1.size(); i++) {
			steps += abs(v1[i].second - v2[i].second);
		}

		printf("Case #%d: %d\n", t, steps);
	}
	
	return 0;
}
/*
5
2
mmaw
maw
2
gcj
cj
2
aaabbb
ab
2
abc
abc
2
aabc
abcc
*/