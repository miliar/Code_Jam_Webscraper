#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>
#include <utility>
#include <cstring>
#include <set>
#include <sstream>
using namespace std;
#define LINE_SIZE 20000
#define NN 20

typedef long long ll;
char line[LINE_SIZE];

int main() {
	int t;
	scanf("%d", &t);
	for (int ti = 0; ti < t; ++ti) {
		int N;
		scanf("%d\n", &N);
		vector<string> lines;
		set<string> words;
		map<string,int> w2;
		for (int i = 0; i < N; ++i) {
			fgets(line, sizeof(line), stdin);
			string s(line);
			lines.push_back(s);
			istringstream iss(s);
			do {
				string w;
				iss >> w;
				if (!w.empty()) {
					words.insert(w);
				}
			} while (iss);
		}
		int count = 0;
		for (auto &w: words) {
			w2[w] = count;
			++count;
		}
		vector<vector<int>> v(N);
		for (int i = 0; i < N; ++i) {
			istringstream iss(lines[i]);
			do {
				string w;
				iss >> w;
				if (!w.empty()) {
					v[i].push_back(w2[w]);
					//printf("v[%d].push_back(%d)\n", i, w2[w]);
				}
			} while (iss);
		}

		int limit = 1 << N;
		size_t best = 999999;
		for (int j = 0; j < limit; j += 4) {
			vector<char> e(words.size());
			vector<char> f(words.size());
			for (int i = 0; i < N; ++i) {
				bool eng = false;
				if (i == 0) {
					eng = true;
				} else if (i == 1) {
					eng = false;
				} else {
					eng = (j >> i)&1;
				}
				for (auto w: v[i]) {
					if (eng) {
						e[w] = 1;
					} else {
						f[w] = 1;
					}
				}
			}
			size_t count = 0;
			for (size_t i = 0; i < words.size(); ++i) {
				if (e[i] && f[i]) ++count;
			}
			if (best > count) {
				best = count;
			}
		}
		printf("Case #%d: %zu\n", ti+1, best);
		fflush(stdout);
	}
	return 0;
}

/* vim: set ts=4 sw=4 noet: */
