#include <bits/stdc++.h>
using namespace std;

#define fr(i,a,b) for (int i = (a), _b = (b); i <= _b; i++)
#define frr(i,a,b) for (int i = (a), _b = (b); i >= _b; i--)
#define rep(i,n) for (int i = 0, _n = (n); i < _n; i++)
#define repr(i,n) for (int i = (n) - 1; i >= 0; i--)
#define foreach(it, ar) for ( typeof(ar.begin()) it = ar.begin(); it != ar.end(); it++ )
#define fill(ar, val) memset(ar, val, sizeof(ar))

#define uint64 unsigned long long
#define int64 long long
#define all(ar) ar.begin(), ar.end()
#define pb push_back
#define mp make_pair
#define ff first
#define ss second

typedef pair<int, int> ii;
typedef pair<int, ii> iii;
typedef vector<ii> vii;
typedef vector<int> vi;

#define PI  3.1415926535897932385
#define EPS 1e-7
#define MOD 1000000007
#define INF 1500111222
#define MAX 1000111

int n, m;
char buffer[MAX];
map<string, int> idx;
vi words[222];
vi value;

int getIndex(string word) {
	if (idx.count(word))
		return idx[word];
	value.pb(0);
	return idx[word] = ++m;
}

void parse(int k) {
	words[k].clear();
	int len = strlen(buffer), i = 0;
	while (i < len) {
		while (i < len && !isalpha(buffer[i])) i++;
		string word = "";
		while (i < len && isalpha(buffer[i]))
			word += buffer[i++];
		if (word.length() != 0)
			words[k].pb(getIndex(word));
	}
}

void readInput() {
	scanf(" %d ", &n);
	m = 0;
	idx.clear();
	value.resize(1);
	rep(i, n) {
		gets(buffer);
		parse(i);
	}
}

int getBoth(int stt) {
	map<int, int> tmpValue;
	fr(i, 2, n - 1) {
		int val = (stt & (1 << (i - 2))) ? 1 : 2;
		rep(j, words[i].size())
			tmpValue[words[i][j]] |= val;
	}
	int res = 0;
	foreach(it, tmpValue) {
		if (value[it->ff] == 3)
			continue;
		int val = it->ss | value[it->ff];
		if (val == 3) res++;
	}
	return res;
}

int res;

void step(int i, int curRes) {
	// printf("%d %d\n", i, curRes);
	if (curRes >= res) return;
	if (i >= n) {
		res = min(res, curRes);
		return;
	}

	int added = 0;
	vi mem(words[i].size());
	set<int> mark;
	rep(j, words[i].size())
		mem[j] = value[words[i][j]];
	rep(j, words[i].size()) {
		value[words[i][j]] |= 1;

		if (mem[j] != 3 && value[words[i][j]] == 3) {
			mark.insert(words[i][j]);
		}
	}
	added = mark.size();
	mark.clear();

	step(i + 1, curRes + added);

	added = 0;
	rep(j, words[i].size())
		value[words[i][j]] = mem[j];
	rep(j, words[i].size()) {
		value[words[i][j]] |= 2;

		if (mem[j] != 3 && value[words[i][j]] == 3) {
			mark.insert(words[i][j]);
		}
	}
	added = mark.size();
	mark.clear();

	// if (i == 3) {
	// 	rep(j, words[i].size()) printf("%d ", mem[j]); puts("");
	// 	rep(j, words[i].size()) printf("%d ", value[words[i][j]]); puts("");
	// 	printf("cr %d added %d\n", curRes, added);
	// }

	step(i + 1, curRes + added);

	rep(j, words[i].size()) {
		value[words[i][j]] = mem[j];
	}
}

int solve() {
	rep(i, 2) {
		rep(j, words[i].size())
			value[words[i][j]] |= (i + 1);
	}
	int sure = 0;
	fr(i, 1, m)
		if (value[i] == 3)
			sure++;
	if (n <= 2) return sure;

	// puts("marked");
	// rep(i, 2) {
	// 	rep(j, words[i].size()) printf("%d ", value[words[i][j]]); puts("");
	// }

	res = INF;
	// fr(i, 1, m) printf("%d ", value[i]); puts("");
	step(2, sure);
	// fr(i, 1, m) printf("%d ", value[i]); puts("");

	// int bit = 1 << (n - 2);
	// rep(stt, bit) {
	// 	res = min(res, sure + getBoth(stt));
	// }

	// rep(i, n) {
	// 	rep(j, words[i].size())
	// 		printf("%d ", words[i][j]);
	// 	puts("");
	// }

	return res;
}

int main() {
	#ifndef ONLINE_JUDGE
	    freopen("csmall.inp", "r", stdin);
	    freopen("csmall2.out", "w", stdout);
	#endif
	int cases, caseNo = 0;
	for (scanf("%d", &cases); cases--; ) {
		readInput();
		printf("Case #%d: %d\n", ++caseNo, solve());
	}
	return 0;
}

// Viet P. Lam - lamphanviet@gmail.com - http://blog.lamphanviet.com