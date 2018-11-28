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

typedef std::pair<char, int> RepStrChar;
typedef vector<RepStrChar>   RepStr;

int test(const RepStr& a, const RepStr& b) {
	if (a.size() != b.size()) return -1;
	int count = 0;
	FORN(i, a.size()) {
		if (a[i].first != b[i].first) return -1;
		count += a[i].second > b[i].second ? a[i].second - b[i].second : b[i].second - a[i].second;
	}
	return count;
}

int main() {

#if defined(M_H_HOME) && (0)
    ifstream ___ifs("a.in.1");
    cin.rdbuf(___ifs.rdbuf());
#endif

	int T;
	cin >> T;
	for (int casen = 1; casen <= T; ++casen) {
		int N;
		cin >> N;
		vector<RepStr> x;
		int mins[27], maxs[27];
		fill(mins, mins + 27, 200);
		fill(maxs, maxs + 27, 0);
		FORN(i, N) {
			string str;
			cin >> str;
			RepStr current;
			FORN(j, str.size()) {
				if (!current.empty() && current.back().first == str[j]) {
					++current.back().second;
				} else {
					current.push_back(make_pair(str[j], 1));
				}
			}
			FORN(j, current.size()) {
				mins[current[j].first - 'a'] = min(mins[current[j].first - 'a'], current[j].second);
				maxs[current[j].first - 'a'] = max(maxs[current[j].first - 'a'], current[j].second);
			}
			x.push_back(current);
		}
		int best = std::numeric_limits<int>::max();
		FORN(i, x.size()) {
			// check if allign all to x[i]
			int moves = 0;
			bool possible = true;
			FORN(j, x.size()) if (i != j) {
				int c = test(x[j], x[i]);
				if (c == -1) {
					possible = false;
					break;
				} else {
					moves += c;
				}
			}
			if (possible) best = min(best, moves);
		}
		// try min-max solution
		if (best < std::numeric_limits<int>::max()) {
			int mm_sol = 0;
			FORN(i, x[0].size()) {
				// each string align to min-max
				int amin = 0, amax = 0;
				FORN(j, x.size()) {
					amin += x[j][i].second - mins[x[j][i].first - 'a'];
					amax += maxs[x[j][i].first - 'a'] - x[j][i].second;
				}
				mm_sol += min(amin, amax);
			}
			best = min(best, mm_sol);
		}

		if (best < std::numeric_limits<int>::max())
			cout << "Case #" << casen << ": " <<  best << "\n";
		else
			cout << "Case #" << casen << ": " <<  "Fegla Won\n";
	}

    return 0;
}
