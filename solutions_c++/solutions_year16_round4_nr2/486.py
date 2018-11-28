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
typedef long double ldouble;

using namespace std;

int n, k;
vector<ldouble> a;
FILE * infile;
FILE * outfile;

vector<ldouble> solve(vector<ldouble> v) {
	vector<ldouble> result; result.resize(0);
	vector<ldouble> tmp; tmp.resize(0); tmp.push_back(1);
	int kk = v.size();
	//printf("%d\n", kk);
	REP(i, 0, kk) {
		result.resize(0);
		REP(j, 0, i + 2)	result.push_back(0);
		REP(j, 0, i + 2) {
			if (j > 0)	result[j] += tmp[j - 1] * v[i];
			if (j < i + 1)	result[j] += tmp[j] * (1 - v[i]);
		}
		//REP(j, 0, i + 2)	printf("%Lf\t", result[j]);
		//printf("\n");
		tmp = result;
	}
	return result;
}

int main() {
	infile = fopen("B-large.in", "rb");
	outfile = fopen("b.out", "w");
	int testNum;
	fscanf(infile, "%d", &testNum);
	REP(tid, 1, testNum + 1) {
		fscanf(infile, "%d%d", &n, &k);
		a.resize(0);
		REP(i, 0, n) {
			ldouble x;
			fscanf(infile, "%Lf", &x);
			a.push_back(x);
		}
		sort(a.begin(), a.end());
		ldouble best_prob = 0;
		REP(smallnum, 0, k + 1) {
			vector<ldouble> v1;
			REP(i, 0, smallnum) {
				v1.push_back(a[i]);
			}
			REP(i, 0, k - smallnum) {
				v1.push_back(a[n - 1 - i]);
			}
			//printf("%d %d %d\n", k, v1.size(), v2.size());
			vector<ldouble> prob1 = solve(v1);
			//vector<ldouble> prob2 = solve(v2);
			ldouble prob = prob1[k / 2];
			if (prob > best_prob)	best_prob = prob;
		}
		fprintf(outfile, "Case #%d: %.20Lf\n", tid, best_prob);
	}
	return 0;
}
