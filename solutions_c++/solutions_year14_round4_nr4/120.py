#include <cstdio>
#include <cstring>
#include <string>
#include <map>
#include <set>
#include <utility>
#include <vector>
#include <algorithm>
#include <cstdint>
#include <cmath>
#include <iostream>
using namespace std;
const uint64_t maxn=1001;
const uint64_t mod = 1000000007;
uint64_t c[maxn][maxn];
uint64_t n, m;

class TrieNode {
public:
	bool word = false;
	uint64_t cnt = 0LL;
	TrieNode* child[26];

	void addString(char* str, int len, int pos) {
		cnt++;
		if (pos >= len) {
			word = true;
			return;
		}
		int cur = str[pos] - 'A';
		if (child[cur] == nullptr) {
			child[cur] = new TrieNode();
		}
		child[cur]->addString(str, len, pos + 1);
	}

	pair<uint64_t, uint64_t> calc() {
		uint64_t tcnt = min(cnt, n);
		uint64_t ans = tcnt;
		uint64_t* f = new uint64_t[tcnt + 1];
		if (word) {
			f[1] = tcnt;
		} else {
			f[0] = 1LL;
		}
		for (uint64_t i = 0; i < 26; i++) {
			if (child[i] == nullptr) {
				continue;
			}
			auto t = child[i]->calc();
			ans += t.first;
			uint64_t cur = min(child[i]->cnt, n);
			uint64_t* tf = new uint64_t[tcnt + 1];
			for (uint64_t j = cur; j <= tcnt; j++) {
				uint64_t st = max((uint64_t)0, j - cur);
				for (uint64_t k = st; k <= j; k++) {
					uint64_t tans = f[k] * c[tcnt - k][j - k];
					tans %= mod;
					tans *= c[k][cur - j + k];
					tans %= mod;
					tans *= t.second;
					tans %= mod;
					tf[j] = (tf[j] + tans) % mod;
				}
			}
			f = tf;
		}
		return make_pair(ans, f[tcnt]);
	}
};

TrieNode* tree;

void preprocess() {
	memset(c, 0, sizeof(c));
	c[0][0] = 1LL;
	for (uint64_t i = 1; i < maxn; i++) {
		c[i][0] = 1LL;
		for (uint64_t j = 1; j <= i; j++) {
			c[i][j] = c[i - 1][j - 1] + c[i - 1][j];
			c[i][j] %= mod;
		}
	}
	return;
}

void init() {
	scanf("%lld%lld", &m, &n);
	tree = new TrieNode();
	for (uint64_t i = 0; i < m; i++) {
		char str[maxn];
		scanf("%s", str);
		tree->addString(str, strlen(str), 0);
	}
	return;
}

int main() {
	uint64_t tcase;
	scanf("%lld", &tcase);
	preprocess();
	for (uint64_t i = 1; i <= tcase; i++) {
		init();
		auto ans = tree->calc();
		printf("Case #%lld: %lld %lld\n", i, ans.first, ans.second);
	}
	return 0;
}