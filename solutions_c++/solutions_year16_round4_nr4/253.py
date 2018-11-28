// VSCF.cpp : Defines the entry point for the console application.
//
#include <iomanip>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <iterator>
#include <string>
#include <vector>
#include <set>
#include <deque>
#include <map>

using namespace std;
typedef long long LL;
typedef pair<int, int> PII;
#define MP make_pair
#define FOR(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define REP(i,n) for(int i=0;i<(n);++i)
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second
#define SIZE(x) (int)x.size()
#define ALL(c) c.begin(),c.end()
typedef long double LD;
#define int long long

template <typename Iterator>
inline bool next_combination(const Iterator first, Iterator k, const Iterator last) {
	/* Credits: Thomas Draper */
	if ((first == last) || (first == k) || (last == k))
		return false;
	Iterator itr1 = first;
	Iterator itr2 = last;
	++itr1;
	if (last == itr1)
		return false;
	itr1 = last;
	--itr1;
	itr1 = k;
	--itr2;
	while (first != itr1) {
		if (*--itr1 < *itr2) {
			Iterator j = k;
			while (!(*itr1 < *j)) ++j;
			std::iter_swap(itr1, j);
			++itr1;
			++j;
			itr2 = k;
			std::rotate(itr1, j, last);
			while (last != j) {
				++j;
				++itr2;
			}
			std::rotate(k, itr2, last);
			return true;
		}
	}
	std::rotate(first, k, last);
	return false;
}

int n;

bool checkHlp(int row, vector<bool> taken, const vector<vector<bool>> &matr) {
	if (row == n) {
		REP(i, n) {
			if (!taken[i]) {
				return false;
			}
		}
		return true;
	}
	bool flag = true;
	int co = 0;
	REP(i, n) {
		vector<bool> temptaken = taken;
		if (!taken[i] && matr[row][i]) {
			temptaken[i] = true;
			flag = flag && checkHlp(row + 1, temptaken, matr);
			co++;
		}
	}
	return co && flag;
}

bool check(vector<vector<bool>> matr) {
	bool flag = true;
	sort(ALL(matr));
	do {
		flag = flag && checkHlp(0, vector<bool>(n, false), matr);
	} while (next_permutation(ALL(matr)));
	return flag;
}

int backtrack(vector<vector<bool>> matr, int i, int j) {
	if (j == n) {
		i++;
		j = 0;
	}
	if (i == n) {
		if (check(matr)) {
			return 0;
		} else {
			return 1e3;
		}
	}
	if (matr[i][j]) {
		return backtrack(matr, i, j + 1);
	} else {
		int score = backtrack(matr, i, j + 1);
		matr[i][j] = 1;
		score = min(score, 1 + backtrack(matr, i, j + 1));
		return score;
	}
}



#undef int
int main() {
#define int long long
	int t;
	cin >> t;
	REP(q, t) {
		cin >> n;
		vector<vector<bool>> s(n,vector<bool>(n));
		
		REP(i, n) {
			string str;
			cin >> str;
			REP(j, n) {
				s[i][j] = str[j] == '1';
			}
		}
		int score = backtrack(s, 0, 0);
		cout << "Case #" << q + 1 << ": " << score << "\n";
	}
	return 0;
}

