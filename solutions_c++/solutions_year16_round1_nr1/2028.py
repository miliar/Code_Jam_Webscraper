#include <cstdio>
#include <algorithm>
using namespace std;

int getIdx(const string& word, int st, int en) {
	int max = -1, maxi = -1;
	for (int i = st; i < en; ++i) {
		if (word[i] >= max) {
			maxi = i;
			max = word[i];
		}
	}
	return maxi;
}

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		char buf[2000];
		scanf(" %s ", buf);
		string word = buf;
		string ans;
		ans.resize(word.size());
		int st = 0, en = word.size();
		int fillloc = 0;
		while (1) {
			int idx = getIdx(word, 0, en);
			ans[st] = word[idx];
			for (int i = idx + 1; i < en; ++i)
				ans[i + st] = word[i];
			st++;
			en = idx;
			if (en <= 0) break;
		}
		printf("Case #%d: %s\n", t, ans.c_str());
	}
}