#include <iostream>
#include <unordered_set>
#include <string>

using namespace std;

int TC, n, i;
long long last;
string s;

unordered_set<char> st;

int main() {
	cin >> TC;
	for (int tc = 1; tc <= TC; ++tc) {
		cin >> n;
		cout << "Case #" << tc << ": ";
		if (n == 0) {
			cout << "INSOMNIA\n";
			continue;
		}
		i = 1;
		st.clear();
		while (st.size() < 10) {
			last = n*i;
			//cout << last << "\n";
			s = to_string(last);
			for (auto &x : s)
				st.insert(x);
			++i;
		}
		cout << last << "\n";
	}
	return 0;
}