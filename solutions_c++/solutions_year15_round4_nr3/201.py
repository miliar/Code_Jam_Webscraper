#include <algorithm>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <queue>
#include <map>
#include <vector>
#include <set>
#include <string>
#include <sstream>
using namespace std;

#define mp make_pair
typedef pair<int, int> pii;

#define MAX_VERT 10000005
#define MAX_ARC 100001000
#define INF 1<<30
typedef int flowtype;
const int kFirst = MAX_VERT - 3, kLast = MAX_VERT - 2;
const int kInf = INF;

map<string, int> w;
set<int> en, fr;
vector<int> words[55];

void Solve() {
	int n;
	cin >> n;
	w.clear();
	string sent;
	getline(cin, sent);
	int q = 0;
	for (int i = 0; i < n; ++i) {
		getline(cin, sent);
		words[i].clear();
		stringstream ss(sent);
		string word;
		while (ss >> word) {
			if (w.count(word) == 0) {
				w[word] = q++;
			}
			words[i].push_back(w[word]);
		}
	}
	en.clear();
	fr.clear();
	int mn = 0;
	for (int i = 0; i < words[0].size(); ++i) {
		en.insert(words[0][i]);
	}
	for (int i = 0; i < words[1].size(); ++i) {
		fr.insert(words[1][i]);
	}
	for (const auto& word : en) {
		if (fr.count(word)) {
			++mn;
		}
	}

	int ans = 1 << 30;
	#pragma openmp parallel for shared(ans)
	for (int i = 0; i < (1 << n); ++i) {
		set<int> en2, fr2;
		en2.clear();
		fr2.clear();
		if ((i & 3) != 1) {
			continue;
		}
		for (int j = 2; j < n; ++j) {
			if (i & (1 << j)) {
				for (int k = 0; k < words[j].size(); ++k) {
					if (!en.count(words[j][k])) {
						en2.insert(words[j][k]);
					}
				}
			} else {
				for (int k = 0; k < words[j].size(); ++k) {
					if (!fr.count(words[j][k])) {
						fr2.insert(words[j][k]);
					}
				}
			}
		}
		int ret = mn;
		for (const auto& word : en2) {
			if (fr2.count(word) || fr.count(word)) {
				++ret;
			}
		}
		for (const auto& word : fr2) {
			ret += en.count(word);
		}
		ans = min(ans, ret);
	}
	cout << ans << endl;
}


int main() {
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int I = 0; I < T; ++I) {
		printf("Case #%d: ", I + 1);
		Solve();
	}
	return 0;
}