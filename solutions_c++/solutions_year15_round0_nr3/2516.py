#include <iostream>
#include <string>
#include <cstdlib>
using namespace std;

enum {
	I = 2,
	J,
	K
};

// 1 
int table[5][5] = {
	{ 0 },
	{ 0, 1, I, J, K },
	{ 0, I, -1, K, -J },
	{ 0, J, -K, -1, I },
	{ 0, K, J, -I, -1 },
};

int main() {
	int T; cin >> T;
	for (int tc = 1; tc <= T; ++tc) {
		int L, X;
		cin >> L >> X;
		string str;
		cin >> str;

		string xstr;
		for (int i = 0; i < X; ++i) xstr.append(str);

		int ijk = table[table[I][J]][K];

		int m = 1;
		for (int i = 0; i < xstr.size(); ++i) {
			int sign = m >= 0 ? 1 : -1;
			
			m = table[abs(m)][xstr[i] - 'i' + I]; // m * xstr[i]
			m *= sign;
		}

		bool ok = false;
		if (m == ijk) {
			int fst = 1;
			for (int i = 0; i < xstr.size(); ++i) {
				int signFst = fst >= 0 ? 1 : -1;
				fst = table[abs(fst)][xstr[i] - 'i' + I]; // fst * xstr[i]
				fst *= signFst;

				if (fst != I) continue;

				int snd = 1;
				for (int j = i + 1; j < xstr.size(); ++j) {
					int signSnd = snd >= 0 ? 1 : -1;
					snd = table[abs(snd)][xstr[j] - 'i' + I]; // snd * xstr[j]
					snd *= signSnd;

					if (snd != J) continue;

					ok = true;
					break;
				}

				if (ok) break;
			}
		}

		cout << "Case #" << tc << ": " << (ok ? "YES" : "NO") << endl;
	}
}