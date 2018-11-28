#include <iostream>
#include <string>
#include <cstring>
#include <vector>
using namespace std;

int main() {
	int N;
	cin >> N;
	for (int c = 1; c <= N; ++c) {
		string s;
		cin >> s;
		vector<int> v(s.size(), 0);
		for (int i = 0; i < s.size(); ++i)
			v[i] = s[i] == '+' ? 1 : 0;
		int r = 0;
		int cur = v.size() - 1;
		while (cur >= 0) {
			while (cur >= 0 && v[cur]) --cur;
			if (cur < 0)
				break;
			for (int i = 0; i <= cur; ++i)
				v[i] ^= 1;
			++r;
		}
		cout << "Case #" << c << ": " << r << endl;
	}
	
	return 0;
}
