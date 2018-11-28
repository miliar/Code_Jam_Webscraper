#include <iostream>
#include <chrono>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

void flip(char& ch) {
	switch (ch) {
	case '+': ch = '-'; break;
	case '-': ch = '+'; break;
	default: assert(false);
	}
}

int main(int argc, char** argv) {

	unsigned test_count; cin >> test_count;
	for (unsigned ti = 1; ti <= test_count; ++ti) {
		string s; unsigned w; cin >> s >> w;
		unsigned mpos = 0;
		unsigned steps = 0;
		while (mpos < s.size() && s[mpos] != '-') ++mpos;
#ifdef DBG
		cout << mpos << ' ' << s << endl;
#endif
		while (mpos + w <= s.size()) {
			for (unsigned i = mpos; i < mpos + w; ++i)
				flip(s[i]);
			++steps;

			while (mpos < s.size() && s[mpos] != '-') ++mpos;
#ifdef DBG
			cout << mpos << ' ' << s << endl;
#endif
		}

		cout << "Case #" << ti << ": ";
		if (mpos == s.size()) cout << steps << endl;
		else cout << "IMPOSSIBLE" << endl;
	}

    return 0;
}
