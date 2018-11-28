#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <utility>
#include <string>
#include <fstream>
#include <map>
#include <set>
#include <queue>
#include <memory.h>

using namespace std;

typedef vector<int> VI;
typedef pair<int, int> PI;
typedef vector<PI> VPI;

#define FOR(i,a,n) for (int i = (a); i < (n); ++i)
#define FORE(i,a,n) for (int i = (a); i <= (n); ++i)
#define FORD(i,a,b) for (int i = (a); i >= (b); --i)
#define REP(i,n) FOR(i,0,n)
#define REPE(i,n) FORE(i,0,n)
#define LL long long
#define FIR(n) REP(i,n)
#define FJR(n) REP(j,n)
#define ALL(v) v.begin(), v.end()

#define FI FIR(n)
#define FJ FJR(n)
#define FR(i,a) FOR(i,a,n)
#define REPN(i) REP(i,n)

#define GI(n) scanf("%d", &n)
#define GI2(n,m) scanf("%d %d", &n, &m)

int n;
int need[3];
int have[3];

void go(int w, int round) {
	if (round == 0) {
		++have[w];
		return;
	}

	int l = (w + 1) % 3;
	go(w, round - 1);
	go(l, round - 1);
}

string gor(int w, int round) {
	if (round == 0) {
		string s;
		s += "PRS"[w];
		return s;
	}

	int l = (w + 1) % 3;
	string s1 = gor(w, round - 1);
	string s2 = gor(l, round - 1);

	string t1 = s1 + s2;
	string t2 = s2 + s1;

	if (t1 < t2)
		return t1;
	return t2;
}


void solve() {
	GI(n);
	FIR(3) GI(need[i]);
	swap(need[0], need[1]);

	string best;

	REP(w, 3) {
		memset(have, 0, sizeof have);
		go(w, n);
		bool ok = true; FJR(3) if (have[j] != need[j]) ok = false;

		if (ok) {
			string res = gor(w, n);
			if (best.empty() || best > res)
				best = res;
		}
	}

	if (best.empty())
		best = "IMPOSSIBLE";

	cout << best << endl;
}

void prepare_input();
int main() {
	prepare_input();
	
	int ntc; GI(ntc);
	FORE(tc, 1, ntc) {
		printf("Case #%d: ", tc);
		solve();
	
	}
}


void prepare_input()  {
	bool LOCAL = false;
	char TASK = 'A';

	static char in_file[200], out_file[200];
	if (LOCAL) {
		freopen("input.txt", "rt", stdin);
	} else {

		int ATTEMPT = 1;
		bool LARGE = true;

		if (LARGE) {
			sprintf(in_file, "%c-large.in", TASK);
			sprintf(out_file, "%c-large.out", TASK);
		} else {
			sprintf(in_file, "%c-small-attempt%d.in", TASK,  ATTEMPT);
			sprintf(out_file, "%c-small-attempt%d.out", TASK,  ATTEMPT);
		}

		cerr << in_file <<  endl; freopen(in_file, "rt", stdin);
		cerr << out_file << endl; freopen(out_file, "w", stdout);
	}
}
