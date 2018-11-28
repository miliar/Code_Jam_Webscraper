#pragma comment(linker, "/STACK:12000000")

#include <algorithm>
#include <vector>
#include <iostream>
#include <fstream>
#include <iterator>
#include <cmath>
#include <cassert>
#include <iomanip>
#include <string>

using namespace std;

// --------------------- Template ---------------------------------------------

#define FOR(i, f, t) for (int i = (int)(f); i < (int)(t); ++i)
#define FORN(i, n) for (int i = 0; i < (int)(n); ++i)

template <class T, class IT>
inline void PRINT(IT i1, IT i2) {
    cout << '['; copy(i1, i2, ostream_iterator<T>(cout, ", ")); cout << "]\n";
}

#if defined(M_H_HOME) && (0)
#define DBG(x) (x)
#else
#define DBG(x)
#endif

typedef long long ll;
typedef long double ld;

// ------------------ Template end --------------------------------------------

bool check(const vector<string>& carriages, const vector<int>& prm) {
	int last_pos[26];
	int abs_pos = 0;
	fill(last_pos, last_pos + 26, -1);
	FORN(i, prm.size()) {
		FORN(j, carriages[prm[i]].size()) {
			char new_char = carriages[prm[i]][j];
			if (last_pos[new_char - 'a'] == -1 || last_pos[new_char - 'a'] == abs_pos - 1) {
				last_pos[new_char - 'a'] = abs_pos;
			} else {
				return false;
			}
			++abs_pos;
		}
	}
	return true;
}

int main() {

#if defined(M_H_HOME) && (0)
    ifstream ___ifs("b.in.1");
    cin.rdbuf(___ifs.rdbuf());
#endif

	int T;
	cin >> T;
	for (int tc = 1; tc <= T; ++tc) {
		int n;
		cin >> n;
		vector<string> carriages(n);
		vector<int> prm(n);
		FORN(i, n) prm[i] = i;
		FORN(i, n) cin >> carriages[i];
		long count = 0;
		do {
			if (check(carriages, prm)) ++count;
		} while (next_permutation(prm.begin(), prm.end()));
		cout << "Case #" << tc << ": " << count << '\n';
	}

    return 0;
}
