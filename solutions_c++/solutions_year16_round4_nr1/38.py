#include <bits/stdc++.h>
using namespace std;
#define REP(i,a,b) for (int i = (a); i <= (b); ++i)
#define REPD(i,a,b) for (int i = (a); i >= (b); --i)
#define FORI(i,n) REP(i,1,n)
#define FOR(i,n) REP(i,0,int(n)-1)
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define vi vector<int>
#define ll long long
#define SZ(x) int((x).size())
#define DBG(v) cerr << #v << " = " << (v) << endl;
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
#define fi first
#define se second

void test() {
	string P="P", R="R", S="S";
	int n, p, r, s;
	scanf("%d%d%d%d", &n, &r, &p, &s);
	while (n>0) {
		int pp = (p+r-s) / 2, rr = (p+s-r) / 2, ss = (r+s-p) / 2;
		if (pp<0 || rr<0 || ss<0) {
			printf("IMPOSSIBLE\n");
			return;
		}
		string PP = P+R, RR = P+S, SS = R+S;
		p=pp; r=rr; s=ss;
		P=PP; R=RR; S=SS;
		n--;
	}
	string res = p ? P : r ? R : S;
	printf("%s\n", res.c_str());
}

int main() {
	int ttn;
	scanf("%d", &ttn);
	for (int i = 1; i <= ttn; i++) {
		printf("Case #%d: ", i);
		test();
	}
	return 0;
}
