#include "assert.h"
#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <time.h>
#include <vector>
#include <unordered_set>

#if LOCAL
	#define DO_NOT_SEND
#endif

typedef long long LL;

int IntMaxVal = (int) 1e20;
int IntMinVal = (int) -1e20;
LL LongMaxVal = (LL) 1e20;
LL LongMinVal = (LL) -1e20;

#define FOR(i, a, b) for(int i = a; i < b ; ++i)
#define FORD(i, a, b) for(int i = a; i >= b; --i)

template<typename T> inline void minimize(T &a, T b) { a = std::min(a, b); }
template<typename T> inline void maximize(T &a, T b) { a = std::max(a, b); }

#define all(v) v.begin(),v.end()

using namespace std;

#define endl '\n'
template<typename T> struct argument_type;
template<typename T, typename U> struct argument_type<T(U)> { typedef U type; };
#define next(t, i) argument_type<void(t)>::type i; cin >> i;

template <typename T1, typename T2> istream& operator >>(istream& is, pair<T1, T2>& s) { is >> s.first >> s.second; return is; }
template <typename T> ostream& operator << (ostream& os, const vector<T> &v) { for (int i = 0 ; i < v.size() ; i++) os << v[i] << ' '; os << endl; return os; }
template <typename T1, typename T2> ostream& operator <<(ostream& s, const pair<T1, T2>& t) { s << t.first << ' ' << t.second; return s; }
template <typename T> vector<T> readVector(int n) { vector<T> res(n); for (int i = 0 ; i < n ; i++) cin >> res[i]; return res; }

const int BUF_SIZE = 100000;

int solve() {
	next(int, n);
	int maxMask = 1 << (n - 2);
	static char buff[BUF_SIZE];
	cin.getline(buff, BUF_SIZE);
	
	map<string, int> words_mapping;
	
	vector<vector<int>> sentences(n);
	FOR (i, 0, n) {
		cin.getline(buff, BUF_SIZE);
		istringstream iss(buff);
		string word;
		while (iss >> word) {
			int x;
			if (words_mapping.count(word)) x = words_mapping[word];
			else {
				x = words_mapping.size();
				words_mapping[word] = x;
			}
			sentences[i].push_back(x);
		}
	}
	
	int res = IntMaxVal;

	vector<vector<int>> cntr(2);
	if (cntr[0].size() <  words_mapping.size()) {
		cntr[0].resize(words_mapping.size());
		cntr[1].resize(words_mapping.size());
	}
	
	for (auto &w : sentences[0]) {
		cntr[0][w]++;
	}
	int cur2 = 0;
	for (auto &w : sentences[1]) {
		if (cntr[1][w]) continue;
		if (cntr[0][w]) cur2++;
		cntr[1][w]++;
	}
	FOR (m2, 0, maxMask) {
		int mask = (m2 << 2) + 2;
		int cur = cur2;
		
		FOR (i, 2, n) {
			int c = (mask >> i) & 1;
			
			for (auto &w : sentences[i]) {
				if (cntr[c][w] == 0 && cntr[1 - c][w] != 0) cur++;
				cntr[c][w]++;
			}
		}
		FOR (i, 2, n) {
			int c = (mask >> i) & 1;
			
			for (auto &w : sentences[i]) {
				cntr[c][w]--;
			}
		}
		
		minimize(res, cur);
	}
	
	
	return res;
}

int main() {
	srand (time(NULL));
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	
	next(int, t);
	FOR (i, 0, t) {
		cout << "Case #" << i + 1 << ": " << solve() << endl;
	}
}