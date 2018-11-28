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

int n;
int a[50][50];
FILE * infile;
FILE * outfile;
int best;

int search(int worker, int lesson, int current) {
	//printf("%d %d %d\n", worker, lesson, current);
	if (worker == n) {
		for (int i = 0; i < n; i ++)
			for (int j = i + 1; j < n; j ++) {
				int flag = 1;
				for (int k = 0; k < n; k ++)
					if ((a[i][k] == 1 && a[j][k] == 0) || (a[i][k] == 0 && a[j][k] == 1))
						flag = 0;
				//printf("check(%d %d): %d\n", i, j, flag);
				//for (int k = 0; k < n; k ++)	printf("values[%d]: %d %d\n", k, a[i][k], a[j][k]);
				if (flag == 0) {
					flag = 1;
					for (int k = 0; k < n; k ++)
						if (a[i][k] == 1 && a[j][k] == 1)
							flag = 0;
					if (flag == 0)
						return 0;
				}
			}
		for (int i = 0; i < n; i ++) {
			int cnt = 0;
			for (int j = 0; j < n; j ++)
				cnt += a[i][j];
			if (cnt == 0)	return 0;
			int s = 0;
			for (int j = 0; j < n; j ++) {
				int flag = 1;
				for (int k = 0; k < n; k ++)
					if (a[i][k] != a[j][k])
						flag = 0;
				s += flag;
			}
			if (cnt != s)	return 0;
		}
		//printf("check ok %d\n", current);
		//for (int i = 0; i < n; i ++) {
		//	for (int j = 0; j < n; j ++)
		//		printf("%d", a[i][j]);
		//	printf("\n");
		//}
		if (current < best)	best = current;
		return 0;
	}
	if (lesson == n) {
		search(worker + 1, 0, current);
		return 0;
	}
	if (current > best)	return 0;
	search(worker, lesson + 1, current);
	if (a[worker][lesson] == 0) {
		a[worker][lesson] = 1;
		search(worker, lesson + 1, current + 1);
		a[worker][lesson] = 0;
	}
}

int main() {
	infile = fopen("D-small-attempt0.in", "rb");
	outfile = fopen("d.out", "w");
	int testNum;
	fscanf(infile, "%d", &testNum);
	REP(tid, 1, testNum + 1) {
		fscanf(infile, "%d\n", &n);
		REP(i, 0, n) {
			REP(j, 0, n){
				char c;
				fscanf(infile, "%c", &c);
				if (c == '1')
					a[i][j] = 1;
				else
					a[i][j] = 0;
			}
			fscanf(infile, "\n");
		}
		best = 100;
		search(0, 0, 0);
		fprintf(outfile, "Case #%d: %d\n", tid, best);
	}
	return 0;
}
