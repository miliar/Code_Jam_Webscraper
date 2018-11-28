#pragma comment(linker, "/STACK:12000000")

#include <algorithm>
#include <vector>
#include <iostream>
#include <fstream>
#include <iterator>
#include <cmath>
#include <cassert>
#include <iomanip>

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

vector<double> ken;
vector<double> naomi;

int ken_move_idx(double chosen_naomi) {
	int i = 0;
	while (i < ken.size() && ken[i] < chosen_naomi + 1e-9) ++i;
	if (i == ken.size()) return 0;
	else return i;
}

// Naomi win?
bool weight(int naomi_idx, int ken_idx) {
	bool result = naomi[naomi_idx] > ken[ken_idx];
	ken.erase(ken.begin() + ken_idx);
	naomi.erase(naomi.begin() + naomi_idx);
	return result;
}

pair<int, double> naomy_choose_1() {
	if (naomi[0] > ken[0]) return make_pair(0, ken[ken.size() - 1] + 1e-7);
	else return make_pair(0, ken[ken.size() - 1] - 1e-7);
}

int naomi_move_war() {
	return 0;
}

int main() {

#if defined(M_H_HOME) && (0)
    ifstream ___ifs("d.in.1");
    cin.rdbuf(___ifs.rdbuf());
#endif

   	int T, casen;
	cin >> T;
	for (casen = 1; casen <= T; ++casen) {

		int n, naomi_score_1 = 0, naomi_score_2 = 0;
		cin >> n;
		vector<double> ken_inp(n), naomi_inp(n);
		FORN(i, n) cin >> naomi_inp[i];
		FORN(i, n) cin >> ken_inp[i];
		sort(naomi_inp.begin(), naomi_inp.end());
		sort(ken_inp.begin(), ken_inp.end());

		// Deceitful
		naomi.assign(naomi_inp.begin(), naomi_inp.end());
		ken.assign(ken_inp.begin(), ken_inp.end());
		while (!naomi.empty()) {
			pair<int, double> naomy = naomy_choose_1();
			int ken_idx = ken_move_idx(naomy.second);
			if (weight(naomy.first, ken_idx)) ++naomi_score_1;
		}

		// War
		naomi.assign(naomi_inp.begin(), naomi_inp.end());
		ken.assign(ken_inp.begin(), ken_inp.end());
		while (!naomi.empty()) {
			int naomi_idx = naomi_move_war();
			int ken_idx = ken_move_idx(naomi[naomi_idx]);
			if (weight(naomi_idx, ken_idx)) ++naomi_score_2;
		}

		cout << "Case #" << casen << ": " << naomi_score_1 << " " << naomi_score_2 << '\n';
	}

    return 0;
}
