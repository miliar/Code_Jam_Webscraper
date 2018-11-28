#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>

using namespace std;

const int N = 4096;

string num2char(int x) {
	switch (x) {
		case 0:
			return "R";
		case 1:
			return "P";
		case 2:
			return "S";
	}
}

string print(vector<int> &a, int l, int r) {
	if (l + 1 == r) {
		return num2char(a[l]);
	}
	int m = l + r >> 1;
	string lft = print(a, l, m), rgt = print(a, m, r);
	if (lft > rgt) {
		swap(lft, rgt);
	}
	return lft + rgt;
}

int main() {
	int testCases;
	scanf("%d", &testCases);
	for (int _ = 1; _ <= testCases; ++_) {
		int n, a, b, c;
		scanf("%d%d%d%d", &n, &a, &b, &c);
		int flag = false;
		vector<int> vec, tmpVec;
		for (int k = 0; k < 3; ++k) {
			vec.clear();
			vec.push_back(k);
			for (int i = 0; i < n; ++i) {
				tmpVec.clear();
				for (int j = 0; j < (int)vec.size(); ++j) {
					tmpVec.push_back(vec[j]);
					tmpVec.push_back((vec[j] + 2) % 3);
				}
				vec = tmpVec;
			}
			/*
			   for (int i = 0; i < (int)vec.size(); ++i) {
			   printf("%d", vec[i]);
			   }
			   printf("\n");
			 */
			int cnt[3];
			memset(cnt, 0, sizeof cnt);
			for (int i = 0; i < (int)vec.size(); ++i) {
				++cnt[vec[i]];
			}
			if (cnt[0] == a && cnt[1] == b && cnt[2] == c) {
				flag = true;
				break;
			}
		}
		printf("Case #%d: ", _);
		if (flag) {
			printf("%s\n", print(vec, 0, (int)vec.size()).c_str());
		} else {
			printf("IMPOSSIBLE\n");
		}
	}
	return 0;
}
