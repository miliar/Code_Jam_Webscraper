#include <cstdio>
#include <map>
#include <string>
#include <algorithm>

using std::map;
using std::string;
using std::max;
using std::min;

struct tuple {
	int p, r, s;
	bool operator<(const tuple&t2) const {
		if(p != t2.p) return p<t2.p;
		if(r != t2.r) return r<t2.r;
		return s<t2.s;
	}
	tuple(int _p=0, int _r=0, int _s=0) {
		p=_p;
		r=_r;
		s=_s;
	}
	tuple operator+(const tuple&t2) const {
		return tuple(p+t2.p, r+t2.r, s+t2.s);
	}
};

map<tuple, string> rec;

int T, N;
int R, P, S;

int main() {
	// construct
	tuple ot[3];
	string os[3];
	ot[0] = tuple(1,0,0);
	ot[1] = tuple(0,1,0);
	ot[2] = tuple(0,0,1);
	rec[ot[0]] = (os[0]="P");
	rec[ot[1]] = (os[1]="R");
	rec[ot[2]] = (os[2]="S");
	for(int n=1; n<=12; n++) {
		tuple nt[3];
		string ns[3];
		nt[0] = ot[1] + ot[2];
		ns[0] = min(os[1],os[2]) + max(os[1],os[2]);
		nt[1] = ot[0] + ot[2];
		ns[1] = min(os[0],os[2]) + max(os[0],os[2]);
		nt[2] = ot[0] + ot[1];
		ns[2] = min(os[0],os[1]) + max(os[0],os[1]);
		for(int i=0; i<3; i++) {
			rec[nt[i]] = ns[i];
			ot[i] = nt[i];
			os[i] = ns[i];
		}
	}
	scanf("%d", &T);
	for(int tc=1; tc<=T; tc++) {
		scanf("%d%d%d%d", &N, &R, &P, &S);
		auto it = rec.find(tuple(P,R,S));
		printf("Case #%d: %s\n", tc, it==rec.end() ? "IMPOSSIBLE" : it->second.c_str());
	}
	return 0;
}