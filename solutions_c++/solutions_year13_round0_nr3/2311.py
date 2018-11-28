#include <algorithm>
#include <cstdio>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

vector<long long> v;
vector<long long> vv;

bool is_palidrome(string s) {
	for (int i = 0; i < (int)s.size() - i; i++) {
		if (s[i] != s[(int)s.size() - i - 1]) return false;
	}
	return true;
}

void rec(string s) {
	if (s.size() > 8) return;
  if (s[0] != '0') {
    stringstream ss(s);
    long long val;
    ss >> val;
    v.push_back(val);
  }
  for (char ch = '0'; ch <= '9'; ch++) {
    rec(ch + s + ch);
  }
}

int main() {
	int T;

	freopen("C-large-1.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	for (char ch = '0'; ch <= '9'; ch++) {
		stringstream ss;
		string s;
		ss << ch;
		ss >> s;
		rec(s);
		rec(s + s);
	}

	for (int i = 0; i < v.size(); i++) {
		long long square = v[i] * v[i];
		ostringstream convert;
		convert << square;
		if (is_palidrome(convert.str())) {
			vv.push_back(square);
		}
	}
	sort(vv.begin(), vv.end());

	scanf_s("%d", &T);
	for (int t = 1; t <= T; t++) {
		long long low, high;

		scanf_s("%lld %lld\n", &low, &high);

		int low_i = -1, high_i = -1;
		for (int i = 0; i < vv.size(); i++) {
			if (low_i == -1 && vv[i] >= low) {
				low_i = i;
			}
			if (vv[i] > high) {
				high_i = i;
				break;
			}
		}
		printf("Case #%d: %d\n", t, high_i - low_i);
	}
	return 0;
}
