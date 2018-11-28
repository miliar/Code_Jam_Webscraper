#include <stdio.h>
#include <functional>
#include <bitset>
#include <math.h>
#include <time.h>
#include <stdlib.h>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <bitset>
#include <string.h>
using namespace std;

int L, X;
string src;

inline void assert(bool v)
{
	if(!v) throw "ERROR";
}

enum qstate {
	one, mone,
	i, mi,
	j, mj,
	k, mk,
	qstatesize
};

qstate chtostate(char ch)
{
	switch(ch) {
		case 'i': return qstate::i;
		case 'j': return qstate::j;
		case 'k': return qstate::k;
		default: assert(false);
	}
}

qstate qmul[qstatesize][qstatesize];

qstate invert(qstate q)
{
	switch(q) {
		case one: return mone;
		case mone: return one;
		case i: return mi;
		case mi: return i;
		case j: return mj;
		case mj: return j;
		case k: return mk;
		case mk: return k;
		default: assert(false);
	}
}

bool qsign(qstate q)
{
	return q == mone || q == mi || q == mj || q == mk;
}

void initqmul()
{
	for(int _a = 0; _a < qstatesize; _a++) {
		for(int _b = 0; _b < qstatesize; _b++) {
			qstate a = (qstate)_a;
			qstate b = (qstate)_b;
			bool sign = false;
			if(qsign(a)) sign ^= true, a = invert(a);
			if(qsign(b)) sign ^= true, b = invert(b);
			
			qstate res = qstatesize;
			if(a == one) {
				res = b;
			} else if(a == i) {
				switch(b) {
					case one: res = i; break;
					case i: res = mone; break;
					case j: res = k; break;
					case k: res = mj; break;
				}
			} else if(a == j) {
				switch(b) {
					case one: res = j; break;
					case i: res = mk; break;
					case j: res = mone; break;
					case k: res = i; break;
				}
			} else if(a == k) {
				switch(b) {
					case one: res = k; break;
					case i: res = j; break;
					case j: res = mi; break;
					case k: res = mone; break;
				}
			}
			if(sign) res = invert(res);
			
			qmul[qstate(_a)][qstate(_b)] = res;
		}
	}
}

void readCase()
{
	cin >> L >> X;
	cin >> src;
}

void solve()
{
	vector<qstate> s;

	for(int i = 0; i < X; i++) {
		for(int j = 0; j < L; j++) {
			s.push_back(chtostate(src[j]));
		}
	}

	const int N = L * X;
	assert(s.size() == N);


	qstate a = one;

	for(int i = 0; i < N - 2; i++) {
		a = qmul[a][s[i]];
		if(a != qstate::i) continue;

		qstate b = one;
		for(int j = i + 1; j < N - 1; j++) {
			b = qmul[b][s[j]];
			if(b != qstate::j) continue;

			qstate c = one;
			for(int k = j + 1; k < N; k++) {
				c = qmul[c][s[k]];
			}

			if(c == qstate::k) {
				cout << "YES";
				return;
			}
		}
	}

	cout << "NO";
}

int main()
{
	initqmul();

	string fname = "./test/C-example.in";
	//string fname = "./test/C-small-attempt0.in";
	//string fname = "./test/C-small-attempt1.in";
	//string fname = "./test/C-large.in";
	//string fname = "./test/C-large-2.in";

	freopen(fname.c_str(),"r",stdin);freopen((fname+".out").c_str(),"w",stdout);

	int analizeCase = -1;
	
	int T;
	scanf("%d", &T);
	for(int tCase = 1; tCase <= T; tCase++) {
		printf("Case #%d: ", tCase);
		readCase();
		if(analizeCase < 0 || analizeCase == tCase) solve();
		printf("\n");
		fflush(stdout);
		fprintf(stderr, "Done %d %%     \r", 100 * tCase / T );
	}
	return 0;
}

