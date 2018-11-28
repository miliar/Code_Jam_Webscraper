#include <iostream>
#include <vector>
#include <string>
#define LL long long

using namespace std;

int main() {
	std::iostream::sync_with_stdio(false);
	LL T; cin >> T; cin.get();
	for (LL t = 1; t <= T; ++t) {
		LL out = 0;
		string s;
		getline(cin, s);
		char prev = s[0];
		for (LL i = 1; i < s.size(); ++i) {
			if (s[i] == prev) continue;
			++out;
			prev = s[i];
		}
		if (prev == '-') ++out;
		cout << "Case #" << t << ": " << out << endl;
	}
}