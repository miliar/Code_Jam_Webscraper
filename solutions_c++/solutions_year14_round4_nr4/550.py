#include <climits>

#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

const int N = 9;
int n, m, result_max, result_cnt, v[N];
string str[N];

int prefix(string p, string q) {
	int ret = 0;
	for (size_t i = 0; i < p.size() && i < q.size(); ++ i) {
		if (p[i] != q[i]) break;
		++ ret;
	}
	return ret;
}

int calc_single(int y) {
	int ret = 1;
	string pre("");
	for (int i = 0; i < n; ++ i) {
		if (v[i] != y) continue;
		ret += str[i].size() - prefix(pre, str[i]);
		pre = str[i];
	}
	return ret;
}

int calc() {
	int ret = 0;
	for (int i = 0; i < m; ++ i) {
		bool exist = false;
		for (int j = 0; !exist && j < n; ++ j) {
			if (v[j] == i) exist = true;
		}
		if (!exist) return INT_MIN;
	}
	for (int i = 0; i < m; ++ i) {
		ret += calc_single(i);
	}
	return ret;
}

void search(int k) {
	if (k == n) {
		int r = calc();
		if (r > result_max) {
			result_max = r;
			result_cnt = 1;
		} else if (r == result_max) {
			++ result_cnt;
		}
	} else {
		for (int i = 0; i < m; ++ i) {
			v[k] = i;
			search(k + 1);
		}
	}
}

int main(void) {
	int test_count;
	cin >> test_count;
	for (int test = 1; test <= test_count; ++ test) {
		cin >> n >> m;
		for (int i = 0; i < n; ++ i) {
			cin >> str[i];
		}
		sort(str, str + n);
		result_max = result_cnt = 0;
		search(0);
		cout << "Case #" << test << ": " << result_max << ' ' << result_cnt << endl;
	}
	return 0;
}
