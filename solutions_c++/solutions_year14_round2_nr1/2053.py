#include <iostream>
#include <vector>
#include <string>
using namespace std;

int calc(const vector<int> &v) {
    int b = *min_element(v.begin(), v.end());
    int e = *max_element(v.begin(), v.end());

    int res = 1000;
    for (int i = b; i <= e; i++) {
	int a = 0;
	for (int x : v) {
	    a += abs(x - i);
	}
	res = min(res, a);
    }
    return res;
}

int calc(string s, vector<string> strs) {
    int res = 0;
    while (!s.empty()) {
	char c = s.back();
	s.pop_back();
	vector<int> v;
	for (auto &str : strs) {
	    int i = 0;
	    while (str.back() == c) {
		str.pop_back();
		i++;
	    }
	    v.push_back(i);
	}
	res += calc(v);
    }
    return res;
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
	int N;
	cin >> N;
	vector<string> strs(N);
	for (int i = 0; i < N; i++) {
	    cin >> strs[i];
	    //	    cout << "strs: " << strs[i] << endl;
	}

	auto m = strs[0];
	auto s = string(m.begin(), unique(m.begin(), m.end()));
	//	cout << "s: " << s << endl;

	bool invalid = false;
	for (auto str : strs) {
	    //	    cout << "str:" << str << endl;
	    //	    cout << string(str.begin(), unique(str.begin(), str.end())) << endl;
	    if (s != string(str.begin(), unique(str.begin(), str.end()))) {
		invalid = true;
		break;
	    }
	}

	if (invalid) {
	    cout << "Case #" << t << ": " << "Fegla Won" << endl;
	    continue;
	}

	cout << "Case #" << t << ": " << calc(m, strs) << endl;
    }
    return 0;
}
