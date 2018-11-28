/*
 * Codejam 2013: Round 2
 * Author: Mahmoud Aladdin (aladdin3)
 * 
 */
 
#include <map>
#include <set>
#include <list>
#include <cmath>
#include <deque>
#include <stack>
#include <ctime>
#include <cstdio>
#include <vector>
#include <bitset>
#include <cstdlib>
#include <cstring>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <iostream>
#include <algorithm>
#include <functional>

using namespace std;

typedef long long _int64;
typedef vector<int> _vi;
typedef vector<_int64> _vll;
typedef vector<string> _vs;

#define MX(a, b) ((a) > (b)? (a): (b))
#define MN(a, b) ((a) < (b)? (a): (b))
#define ABS(x) (((x) < 0)? -(x): (x))

#define ALL(V) (V).begin(), (V).end()
#define SZ(V) ((int)(V).size())
#define VPSH(V, X) (V).push_back(X)
#define REVA(V, S) reverse(V, V + s)
#define REV(V) reverse(ALL(V))

#define BTST(X, i) ((X) & (1 << (i)))
#define BSET(X, i) (X) |= (1 << (i))
#define BCLR(X, i) (X) &= ~(1 << (i))
#define BFLP(X, i) (X) ^= (1 << (i))

#define FOR(i, a, b, step) for(int (i) = (a); (((step) < 0)? ((i) > (b)): ((i) < (b))); (i) += (step)) 
#define REP(i, n) FOR(i, 0, n, 1)

#define filename_in "B.in"
#define filename_out "B.out"

bool canUn(_int64 num, _int64 goal, _int64 total) {
	_int64 before = num;
	_int64 after = total - 1 - num;
	string done = "";
	while(after > 0 || before > 0) {
		if (before > 0) { // LOSE
			done += "L";
			before--;
			int beatafter = before % 2;
			before >>= 1;
			after += beatafter;
			after >>= 1;
		} else { // win
			done += "W";
			after--;
			after >>= 1;
		}
	}
	_int64 rank = 0;
	for(int i = 0; i < SZ(done); i++) {
		rank <<= 1;
		if(done[i] == 'L') {
			rank += 1;
		}
	}
	//fprintf(stderr, "NUM:%lld done:%s, rank:%lld\n", num, done.c_str(), rank);
	return rank < goal;
}

_int64 binarySearchUn(_int64 start, _int64 end, _int64 goal, _int64 total) {
	_int64 ans = 0;
	while (end > start) {
		_int64 mid = (start + end) >> 1;
		if(canUn(mid, goal, total)) {
			ans = mid;
			start = mid + 1;
		} else {
			end = mid;
		}
	}
	return ans;
}

bool can(_int64 num, _int64 goal, _int64 total) {
	_int64 after = num;
	_int64 before = total - 1 - num;
	string done = "";
	while(after > 0 || before > 0) {
		if (before > 0) { // LOSE
			done += "W";
			before--;
			_int64 beatafter = before % 2;
			before >>= 1;
			after += beatafter;
			after >>= 1;
		} else { // win
			done += "L";
			after--;
			after >>= 1;
		}
	}
	_int64 rank = 0;
	for(int i = 0; i < SZ(done); i++) {
		rank <<= 1;
		if(done[i] == 'L') {
			rank += 1;
		}
	}
	//fprintf(stderr, "ORDERED: NUM:%lld done:%s, rank:%lld\n", num, done.c_str(), rank);
	return rank < goal;
}

_int64 binarySearch(_int64 start, _int64 end, _int64 goal, _int64 total) {
	_int64 ans = 0;
	while (end > start) {
		_int64 mid = (start + end) >> 1;
		if(can(mid, goal, total)) {
			ans = mid;
			start = mid + 1;
		} else {
			end = mid;
		}
	}
	return ans;
}


int main() {
	FILE *fin = fopen(filename_in, "r");
	FILE *fout = fopen(filename_out, "w");
	
	int TC; fscanf(fin, "%d", &TC);
	REP(tc, TC) {
		_int64 nT, P;
		int N; 
		fscanf(fin, "%d %lld", &N, &P);
		nT = 1LL << N;
		//printf("%d, %lld, %lld\n", N, P, nT);
		_int64 unordered, ordered;
		unordered = binarySearchUn(0, nT, P, nT);
		ordered = binarySearch(0, nT, P, nT);
		fprintf(fout, "Case #%d: %lld %lld\n", tc + 1, unordered, ordered);
		printf("Case #%d: %lld %lld\n", tc + 1, unordered, ordered);
	}

	fclose(fin);
	fclose(fout);
	return 0;
}
