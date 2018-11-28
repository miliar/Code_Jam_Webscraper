#ifndef FLLD
#ifdef WIN32
#define FLLD "%I64d"
#else
#define FLLD "%lld"
#endif
#endif

#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <ctime>
#include <tuple>
#include <random>
#include <sstream>
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <string.h>
#include <queue>

#define SZ(x) ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#define NOKEY(x, y) ((x).find(y) == (x).end())
#define EXISTKEY(x, y) ((x).find(y) != (x).end())
#define INCMAP(x, y) ((x)[y] = MAPINTV(x, y) + 1)
#define MAPINTV(x, y) (EXISTKEY(x, y) ? (x)[y] : 0)
#define REP(i, a, b) for (int i = (a), _end_ = (b); i < _end_; i ++)
#define FORALL(x, l) for (const auto & x : l)
#define DEBUGLEVEL 5
#define DEBUG(debuglevel, ...) if(debuglevel <= DEBUGLEVEL) fprintf(stderr, ##__VA_ARGS__);
typedef long long ll;

using namespace std;

#define MAXN 12

int total;
FILE * infile;
FILE * outfile;

int smaller(vector<int> a1, vector<int> a2) {
	REP(i, 0, a1.size())
		if (a1[i] < a2[i])
			return 1;
	return 0;
}

vector<int> get_result(int n, int winv) {
	vector<int> result; result.resize(0);
	if (n == 1) {
		result.push_back(winv);
		return result;
	}
	vector<int> result1 = get_result(n - 1, winv);
	vector<int> result2 = get_result(n - 1, (winv + 2) % 3);
	if (smaller(result1, result2)) {
		REP(i, 0, result1.size())	result.push_back(result1[i]);
		REP(i, 0, result2.size())	result.push_back(result2[i]);
	} else {
		REP(i, 0, result2.size())	result.push_back(result2[i]);
		REP(i, 0, result1.size())	result.push_back(result1[i]);
	}
	//REP(i, 0, result.size())
	//	printf("%d", result[i]);
	//printf("\n");
	return result;
}

int check(int n, int r, int p, int s, int winv) {
	vector<int> res = get_result(n, winv);
	int a1 = 0;
	int a2 = 0;
	int a3 = 0;
	FORALL(v, res) {
		if (v == 0)	a1 ++;
		if (v == 1)	a2 ++;
		if (v == 2)	a3 ++;
	}
	//printf("%d %d %d %d\n", n, a1, a2, a3);
	if (a1 == p && a2 == r && a3 == s) {
		REP(i, 0, res.size()) {
			if (res[i] == 0)	fprintf(outfile, "P");
			if (res[i] == 1)	fprintf(outfile, "R");
			if (res[i] == 2)	fprintf(outfile, "S");
		}
		fprintf(outfile, "\n");
		return 1;
	}
	return 0;
}

int main() {
	infile = fopen("A-large.in", "r");
	outfile = fopen("a.out", "w");
	int testNum;
	fscanf(infile, "%d", &testNum);
	REP(tid, 1, testNum + 1) {
		int n, r, p, s;
		fscanf(infile, "%d%d%d%d", &n, &r, &p, &s);
		n ++;
		fprintf(outfile, "Case #%d: ", tid);
		//printf("%d\n", n);
		if (!check(n, r, p, s, 0))
			if (!check(n, r, p, s, 1))
				if (!check(n, r, p, s, 2))
					fprintf(outfile, "IMPOSSIBLE\n");
	}
	return 0;
}
