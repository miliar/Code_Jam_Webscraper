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

struct Node;
Node* new_node();

struct Node {
	Node* p[26];
	
	Node* follow (char c) {
		c -= 'A';
		if (p[c]== 0)
			p[c] = new_node();
		return p[c];
	}

	int size() {
		int res = 1;
		FIR(26) if (p[i])
			res +=  p[i]->size();
		return res;
	}
};

void follow(Node* root, const string& s) {
	FIR(s.size())
		root = root->follow(s[i]);
}



Node buf[100000];
int bufp;

string s[10];
int sv;
int n;
int pl[10];

Node* roots[5];
int cnt = 0;
int worst = -1;

void go(int pos) {
	if (pos == n) {
		bufp = 0;
		FIR(sv) roots[i] = 0;
		FI {
			Node* root = roots[pl[i]];
			if (root == 0) {
				roots[pl[i]] = root = new_node();
			}
			follow(roots[pl[i]], s[i]);
		}
		int q = 0;
		FIR(sv) if (roots[i]) q += roots[i]->size();
		if (q == worst) ++cnt;
		else if (q > worst) {
			worst = q;
			cnt = 1;
		}
	} else {
		FIR(sv)  {
			pl[pos] = i;
			go(pos+1);
		}
	}
}

Node* new_node() {
	Node* p = &buf[bufp++];
	FIR(26) p->p[i] = 0;
	return p;
}

PI solve() {
	GI2(n, sv);
	FI cin >> s[i];
	cnt = 0; worst =-1;
	go(0);
	
	return PI(worst, cnt);
}

void prepare_input();
int main() {
	prepare_input();
	
	int ntc; GI(ntc);
	FORE(tc, 1, ntc) {
		PI res = solve();
		printf("Case #%d: %d %d\n", tc, res.first, res.second);
	}
}


void prepare_input()  {
	bool LOCAL = false;
	char TASK = 'D';

	static char in_file[200], out_file[200];
	if (LOCAL) {
		freopen("input.txt", "rt", stdin);
	} else {

		int ATTEMPT = 0;
		bool LARGE = false;

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
