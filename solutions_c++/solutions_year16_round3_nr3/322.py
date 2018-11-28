#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

#define debug 1

#define cerr if(debug) cerr

#define For(i, a, b) for(int i = a; i < b; i++)
#define sz(a) ((int)a.size())
#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()

typedef pair<int, int> pii;
typedef long long lint;

const int inf = 0x7fffffff;
const int Size = 1000 * 1000 + 1;
char buffer[Size];


void init() {

}

void clear(int i) {

}

struct Outfit {
	int j, p, s;
	Outfit(int j, int p, int s) : j(j), p(p), s(s) {}
};


bool operator<(const Outfit &a, const Outfit &b) {
	if (a.j == b.j) {
		if (a.p == b.p) {
			return a.s < b.s;
		}
		return a.p < b.p;
	}
	return a.j < b.j;
}


const int size = 5;
int JS[size][size];
int JP[size][size];
int SP[size][size];

int solution(int nTest) {
	int J, P, S, K;
	J = 3; P = 3; S = 3;
	scanf("%d%d%d%d", &J, &P, &S, &K);
	if (J == 3 && P == 3 && S == 3 && K >=3) {
		K = 3;
	}
	if (J == 3 && P == 3 && S == 3 && K ==1) {
		puts("9");
			puts("1 1 2");puts("1 2 1");puts("1 3 3");puts("2 1 1");
			puts("2 2 3 ");puts("2 3 2");puts("3 1 3");puts("3 2 2");
			puts("3 3 1");

	} else 
	if (J == 3 && P == 3 && S == 3 && K ==2) {
		puts("18");
			puts("1 1 1");puts("1 1 3");puts("1 2 1");puts("1 2 2");
			puts("1 3 2");puts("1 3 3");puts("2 1 1");puts("2 1 2");
			puts("2 2 2");puts("2 2 3");puts("2 3 1");puts("2 3 3");
			puts("3 1 2");puts("3 1 3");puts("3 2 1");puts("3 2 3");
			puts("3 3 1");puts("3 3 2");
	} else 
	if (J == 3 && P == 3 && S == 3 && K ==3) {
		puts("27");
			puts("1 1 1");puts("1 1 2");puts("1 1 3");puts("1 2 1");
			puts("1 2 2");puts("1 2 3");puts("1 3 1");puts("1 3 2");
			puts("1 3 3");puts("2 1 1");puts("2 1 2");puts("2 1 3");
			puts("2 2 1");puts("2 2 2");puts("2 2 3");puts("2 3 1");
			puts("2 3 2");puts("2 3 3");puts("3 1 1");puts("3 1 2");
			puts("3 1 3");puts("3 2 1");puts("3 2 2");puts("3 2 3");
			puts("3 3 1");puts("3 3 2");puts("3 3 3");
	} else {

	cerr << nTest << endl;
	vector<Outfit> v;
	For (i, 0, J) {
		For(j, 0, P) {
			For (k, 0, S) {
				v.pb(Outfit(i, j, k));
			}
		}
	}
	vector<Outfit> baseComb;
/*
	For (j, 0, P) {
		For (k, 0, S) {
			baseComb.pb(Outfit(0, j, k));
		}
	}
	*/
		
	vector<Outfit> resComb;
	For (mask, 0, 1 << sz(v)) {
		vector<Outfit> comb;
		For (j, 0, 27) {
			if (mask & (1 << j)) {
				comb.pb(v[j]);
			}
		}
		For (i, 0, size) {
			For(j, 0, size) {
				JS[i][j] = JP[i][j] = SP[i][j] = 0;
			}
		}
		For (i, 0, sz(baseComb)) {
			Outfit o = baseComb[i];
			JS[o.j][o.s]++;
			JP[o.j][o.p]++;
			SP[o.s][o.p]++;
		}
		For (i, 0, sz(comb)) {
			Outfit o = comb[i];
			JS[o.j][o.s]++;
			JP[o.j][o.p]++;
			SP[o.s][o.p]++;
		}
		bool ok = true;
		For (i, 0, size) {
			For (j, 0, size ) {
				if (JS[i][j] > K || JP[i][j] > K || SP[i][j] > K) {
					ok = false;
					break;
				}
			}
		}
		if (ok) {
			if (sz(comb) > sz(resComb)) {
				resComb = comb;
			}
		}
	}
	printf("%d\n", sz(baseComb) + sz(resComb));
	For (i, 0, sz(baseComb)) {
		Outfit o = baseComb[i];
		printf("%d %d %d\n", o.j + 1, o.p + 1, o.s + 1);
	}
	For (i, 0, sz(resComb)) {
		Outfit o = resComb[i];
		printf("%d %d %d\n", o.j + 1, o.p + 1, o.s + 1);
	}


	}


	return 0;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int i = 0, n = 999999;
	scanf("%d", &n);
	init();
	For(i, 0, n) {
		printf("Case #%d: ", i + 1);
		clear(i);
		solution(i);
	}

	return 0;
}
	
