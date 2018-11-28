
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

typedef long long i8;

int tst;
int d,n,w,e,s,dd,dp,ds;
int he[600];

struct Att {
	int day, we, es, st;
};

bool operator<(const Att &x, const Att &y) {
	return x.day<y.day;
}

vector<Att> att;

int solve() {
	fill(he,he+600,0);
	att.clear();

	int ct;
	scanf("%d",&ct);
	for (int t=0; t<ct; t++) {
		scanf("%d%d%d%d%d%d%d%d",&d,&n,&w,&e,&s,&dd,&dp,&ds);
		Att ak;
		for (int a=0; a<n; a++) {
			ak.day=d+dd*a;
			ak.we=w+dp*a+300;
			ak.es=e+dp*a+300;
			ak.st=s+ds*a;
			att.push_back(ak);
		}
	}
	
	sort(att.begin(),att.end());
	int re=0, od=-1;
	for (int i=0; i<att.size(); i++) {
		Att &a=att[i];
		//printf("   att day=%d [%d,%d] st=%d\n", a.day, a.we, a.es, a.st);
		if (a.day>od) {
			for (int j=i-1; j>=0; j--) {
				Att &b=att[j];
				if (b.day!=od) break;
				for (int x=b.we; x<b.es; x++) he[x]=max(he[x],b.st);
			}
			od=a.day;
		}
		bool ok=false;
		for (int x=a.we; !ok && x<a.es; x++) {
			if (he[x]<a.st) ok=true;
		}
		if (ok) re++;
	}
	
	return re;
}

main() {
	scanf("%d", &tst);
	for (int cas=1; cas<=tst; cas++) {
		printf("Case #%d: %d\n", cas, solve());
	}
}
