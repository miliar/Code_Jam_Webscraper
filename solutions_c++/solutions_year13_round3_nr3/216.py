#include <algorithm>
#include <cstdio>
#include <vector>
using namespace std;

#define mp(x, y) make_pair(x, y)

struct utok {
	int kdy;
	int w, e;
	int s;
	utok(int a, int b, int c, int d) {kdy=a; w=b; e=c; s=d;}
	bool operator<(const utok &u) const {return kdy<u.kdy;}
};

int T;
int N;
vector<utok> att;
int zed[500];
int nzed[500];
int succ;
int za[500];
int nza[500];

int main()
{
	scanf("%d", &T);

for(int q=1; q<=T; q++) {
	scanf("%d", &N);
	att.clear();
	succ=0;
	for(int i=0; i<N; i++) {
		int d, n, w, e, s, dd, dp, ds;
		scanf("%d%d%d%d%d%d%d%d", &d, &n, &w, &e, &s, &dd, &dp, &ds);
		for(int j=0; j<n; j++) {
			att.push_back(utok(d+j*dd, 200+w+j*dp, 200+e+j*dp, s+j*ds));
		}
	}
	sort(att.begin(), att.end());
	for(int i=0; i<=400; i++) zed[i]=nzed[i]=za[i]=nza[i]=0;
	for(int i=0; i<att.size(); i++) {
		if(i>0 && att[i].kdy!=att[i-1].kdy) {
			for(int j=0; j<=400; j++) zed[j]=nzed[j];
			for(int j=0; j<=400; j++) za[j]=nza[j];
		}
		int ok=0;
		for(int j=att[i].w; j<=att[i].e; j++) if(zed[j]<att[i].s) {ok=1; break;}
		for(int j=att[i].w; j<att[i].e; j++) if(za[j]<att[i].s) {ok=1; break;}
		succ+=ok;
		for(int j=att[i].w; j<=att[i].e; j++) nzed[j]=max(nzed[j], att[i].s);
		for(int j=att[i].w; j<att[i].e; j++) nza[j]=max(nza[j], att[i].s);
	}
	printf("Case #%d: %d\n", q, succ);
}

	return 0;
}
