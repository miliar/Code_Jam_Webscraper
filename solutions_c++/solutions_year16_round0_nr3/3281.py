#include <bits/stdc++.h>

using namespace std;

int64_t inbase(int64_t base, const string &str) {
	int64_t thing = 0, p = 1;
	for (int64_t i = 0; i < str.size(); ++i) {
		thing += (str[i] == '1') * p;
		p *= base;
	}
	return thing;
}

int64_t getdiv(int64_t N) {
	for (int64_t d = 2; d*d <= N; ++d) {
		if (N%d == 0)
			return d;
	}
	return -1;
}

int main() {
	int T, N, J;
	cin >> T >> N >> J;
	vector<pair<string, vector<int64_t>>> ans;
	for (int bs = 0; bs < (1<<(N-2)); ++bs) {
		string str = "1";
		for (int i = 0; i < (N-2); ++i)
			str.push_back(bs&(1<<i) ? '1' : '0');
		str.push_back('1');
		vector<int64_t> divs;
		for (int b = 2; b <= 10; ++b) {
			reverse(str.begin(), str.end());
			int64_t val = inbase(b, str);
			reverse(str.begin(), str.end());
			int64_t d = getdiv(val);
			if (d != -1)
				divs.push_back(d);
		}
		if (divs.size() == 9) {
			//cout << str << endl;
			ans.push_back({str, divs});
		}
		//cout << str << " " << divs.size() << endl;
		if (ans.size() == J) {
			break;
		}
	}
	cout << "Case #1: " << endl;
	for (auto &p : ans) {
		cout << p.first << " ";
		for (int64_t i : p.second)
			cout << i << " ";
		cout << endl;
	}
}