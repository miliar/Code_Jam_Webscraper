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

#if defined(M_H_HOME) && (1)
#define DBG(x) (x)
#else
#define DBG(x)
#endif

typedef long long ll;
typedef long double ld;

// ------------------ Template end --------------------------------------------

const int MAX_LEN = 4444;
const int INFTY = 1000000;

vector<string> dictionary;

void loadDict(vector<string>& dict) {
	ifstream dictStream("dictionary.txt");
	char buf[1024];
	while (dictStream.good()) {
		dictStream.getline(&buf[0], 1024);
		int q = strlen(buf);
		for (int i = strlen(buf); i >= 0; --i) if (!isalpha(buf[i])) buf[i] = '\0';
		if (q != strlen(buf)) {cout << "!!!\n"; }
		if (strlen(buf) > 0)
			dict.push_back(buf);
	}
}

bool match(const char* from, size_t len, const string& word, int lastPos, int& lastRes, int& count) {
	if (len < word.size()) return false;
	lastRes = -lastPos;
	count = 0;
	FORN(i, word.size()) {
		if (from[i] != word[i]) {
			if (i - lastRes < 5) return false;
			++count;
			lastRes = i;
		}
	}
	return true;
}

int solve(string msg) {
	int state[MAX_LEN][8]; // min number of changes before position i for each relative position of the last change [1-5];
	FORN(i, MAX_LEN)
		FORN(j, 8)
			state[i][j] = INFTY;
	FORN(j, 8)
		state[0][j] = 0;

	FORN(i, msg.size()) {
		for(int lastPos = 1; lastPos <= 7; ++lastPos) 
		    if (state[i][lastPos] != INFTY) {
				for(int wi = 0; wi < dictionary.size(); ++wi) {
					int lastRes;
					int count;
					if (match(&msg[i], msg.size() - i, dictionary[wi], lastPos, lastRes, count)) {
						lastRes = min(7, (int)dictionary[wi].size() - lastRes);
						state[i + dictionary[wi].size()][lastRes] = min(state[i + dictionary[wi].size()][lastRes], state[i][lastPos] + count);
					}
				}
			}
	}

	int result = INFTY;
	FORN(j, 8) result = min(result, state[msg.size()][j]);
	return result;
}

int main() {

#if defined(M_H_HOME) && (0)
    ifstream ___ifs("c.in.1");
    cin.rdbuf(___ifs.rdbuf());
#endif

	loadDict(dictionary);

    int T;
	string str;
    cin >> T;
	FOR(i, 1, T+1) {
		cout << "Case #" << i << ": ";
		cin >> str;
		cout << solve(str) << '\n';
	}

    return 0;
}
