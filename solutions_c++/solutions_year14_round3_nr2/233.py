
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

typedef long long i8;

int tst, n, mo=1000000007;
char vag[105][8999];
bool take[105];

int solve() {
	for (int i=0; i<n; i++) {
		int le=strlen(vag[i]);
		*unique(vag[i], vag[i]+strlen(vag[i]))=0;
		vag[i][le]=0;
//printf("   %s\n", vag[i]);
	}

	i8 re=1;
	fill(take,take+n,true);
	vector<int> mdl;
	for (char c='a'; c<='z'; c++) {
		int lft=-1, rgt=-1, cos=0;
		mdl.clear();
		for (int i=0; i<n; i++) if (take[i]) {
			int le=strlen(vag[i]);
			bool sw=false, ew=false, all=(vag[i][0]==c && le==1);
			if (all) {
				mdl.push_back(i);
			} else {
				sw=vag[i][0]==c;
				ew=vag[i][le-1]==c;
				for (int p=1; p<le-1; p++) {
					if (vag[i][p]==c)
						cos++;
				}
				if (sw && ew) return 0;
				if (sw) { if (rgt>=0) return 0; rgt=i; }
				if (ew) { if (lft>=0) return 0; lft=i; }
			}		
		}
		
		if (lft>=0 || rgt>=0 || !mdl.empty()) cos++;
//printf("'%c' left=%d rgt=%d cos=%d\n", c,lft,rgt,cos);
		if (cos>1) return 0;
		
		if (lft>=0) { // take left
			int le=strlen(vag[lft]);
			vag[lft][le-1]='^';
			for (int j=0; j<mdl.size(); j++) {
				take[mdl[j]]=false;
				re=re*(1+j)%mo;
			}
			if (rgt>=0) {
				take[rgt]=false;
				int j=1;
				while (vag[rgt][j]) vag[lft][le++]=vag[rgt][j++];
				vag[lft][le]=0;
			}
		} else if (rgt>=0) { // take right
			vag[rgt][0]='^';
			for (int j=0; j<mdl.size(); j++) {
				take[mdl[j]]=false;
				re=re*(1+j)%mo;
			}
		} else { // middle only
			for (int j=0; j<mdl.size(); j++) {
				if (j) take[mdl[j]]=false;
				re=re*(1+j)%mo;
			}
		}
	}
	
	int cnt=0;
	for (int i=0; i<n; i++) {
		if (take[i]) cnt++;
	}
	for (int i=0; i<cnt; i++)
		re=re*(1+i)%mo;

	return re;
}

main() {
	scanf("%d", &tst);
	for (int cas=1; cas<=tst; cas++) {
		scanf("%d",&n);
		for (int i=0; i<n; i++)
			scanf("%s", vag[i]);
		printf("Case #%d: %d\n", cas, solve());
	}
}
