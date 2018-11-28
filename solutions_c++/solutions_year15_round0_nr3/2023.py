#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>

#include<algorithm>
#include<utility>
#include<string>

#include<deque>
#include<list>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<vector>

using namespace std;

#define REP(i,N) for (int i = 0; i < (N); i++)
#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define FORD(i, b, a) for (int i = (b) - 1; i >= a; i--)
#define DP(arg...) fprintf(stderr, ## arg) //COMPILER SPECIFIC!!!

typedef long long ll;

struct quat {
	int v, sgn;
	quat() : v(1), sgn(1) {}
	quat(int _v,int _sgn) : v(_v), sgn(_sgn) {}
	quat operator*(const quat& b) const {
		quat r;
		if (v == 1) {
			r.v = b.v;
			r.sgn = b.sgn * sgn;
		}
		else if (b.v == 1) {
			r.v = v;
			r.sgn = b.sgn * sgn;
		}
		else if (v == b.v) {
			r.v = 1; r.sgn = sgn * b.sgn * -1;
		}
		else {
			r.sgn = b.sgn * sgn;
			if (!(b.v == v + 1 || (v == 4 && b.v == 2)))
				r.sgn *= -1;
			r.v = 9 - v - b.v;
		}
		return r;
	}
	bool is_i() const {
		return (v == 2 && sgn == 1);
	}
	bool is_j() const {
		return (v == 3 && sgn == 1);
	}
	bool is_k() const {
		return (v == 4 && sgn == 1);
	}
	void print() {
		//printf("%c%d\n", sgn == 1 ? ' ' : '-', v);
	}
};

int T;
int L, X;

quat S[100000];
char str[100000];

void solve(int _case) {
	scanf("%d%d", &L, &X);
	scanf(" %s", str);
	//printf("--%s\n", str);
	REP(l,L) {
		S[l].sgn = 1;
		if (str[l] == 'i') S[l].v = 2;
		if (str[l] == 'j') S[l].v = 3;
		if (str[l] == 'k') S[l].v = 4;
	}
	for (int x = 1; x < X; x++) {
		REP(l,L) {
			S[x*L+l].v = S[l].v;
			S[x*L+l].sgn = 1;
		}
	}
	quat q;
	int N = X*L;
	REP(n,N) {
		q = q * S[n];
		//S[n].print();
		//q.print();
	}
	q.print();

	bool OK = false;
	if (q.v == 1 && q.sgn == -1) {
		int a;
		quat qa;
		for (a = 0; a < N && !qa.is_i(); a++) {
			 qa = qa * S[a];
			 qa.print();
		}
		//printf("--");
		a--;
		int b;
		quat qb;
		for  (b = N-1; b >= 0 && !qb.is_k(); b--) {
			qb = S[b] * qb;
			qb.print();
		}
		if (a < b) OK = true;
		//printf("res %d %d\n", a, b);
	}

	printf("Case #%d: %s\n", _case, OK ? "YES" : "NO");
}

int main() {
	scanf("%d", &T);
	REP(t,T) solve(t+1);
	return 0;
}
