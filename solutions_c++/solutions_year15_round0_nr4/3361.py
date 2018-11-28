#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define _CRT_SECURE_NO_WARNINGS
#define FOR(i,a,b) for(int i=(a);i<(int)(b);i++)
#define REP(i,a) for(int i=0;i<(int)(a);i++)
#define ALL(i) i.begin(),i.end()
#define rALL(i) i.rbegin(),i.rend()
#define PB push_back

using namespace std;
string rr = "RICHARD";
string gg = "GABRIEL";
string winner(int min, int max, int x) {
	//1 3 2
	//3 4 1 => 1 4 3

	int total = min * max;
	if (total%x != 0) {
		return rr;
	}
	if (x == 1) return gg;
	if (x == 2) {
		if (min == 1 && max == 1) return rr;
		if (min == 1 && max == 2) 
		return gg;
	}
	if (x == 3) {
		if (min == 3 && max == 3) return gg;
		if (min == 4 && max == 4) return rr;
		return gg;
	}
	if (x == 4) {
		if (min == 3 && max == 4) return gg;
		return rr;
	}
}

string winner2(int min, int max, int x) {
	if (x == 1) return gg;
	if (min == 1 && max == 1) {
		if (x == 2) return rr;
		if (x == 3) return rr;
		if (x == 4) return rr;
	}

	if (min == 1 && max == 2) {
		if (x == 2) return gg;
		if (x == 3) return rr;
		if (x == 4) return rr;
	}



	if (min == 1 && max == 3) {
		if (x == 2) return rr;
		if (x == 3) return rr;
		if (x == 4) return rr;
	}

	if (min == 1 && max == 4) {
		if (x == 2) return gg;
		if (x == 3) return rr;
		if (x == 4) return rr;
	}


	if (min == 2 && max == 2) {
		if (x == 2) return gg;
		if (x == 3) return rr;
		if (x == 4) return rr;
	}

	if (min == 2 && max == 3){
		if (x == 2) return gg;
		if (x == 3) return gg;
		if (x == 4) return rr;
	}


	if (min == 2 && max == 4){
		if (x == 2) return gg;
		if (x == 3) return rr;
		if (x == 4) return rr;
	}


	if (min == 3 && max == 3) {
		if (x == 2) return rr;
		if (x == 3) return gg;
		if (x == 4) return rr;
	}


	if (min == 3 && max == 4) {
		if (x == 2) return gg;
		if (x == 3) return gg;
		if (x == 4) return gg;
	}

	if (min == 4 && max == 4){
		if (x == 2) return gg;
		if (x == 3) return rr;
		if (x == 4) return gg;
	}

}

int main() {
	int cases;

	freopen("D-small-attempt4.in", "r", stdin);
	freopen("D-small-attempt4.out", "w", stdout);

	scanf("%d", &cases);
	REP(k, cases) {
		int x, r, c; //2 1 3
		scanf("%d %d %d", &x, &r, &c);
		int maxw = max(r, c), minw = min(r, c);
		//minw maxw x
		string res = winner2(minw, maxw, x);
		cout << "Case #" << (k + 1) << ": " << res << endl;
	}
	return 0;
}
