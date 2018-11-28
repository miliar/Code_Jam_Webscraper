#include <iostream>
#include <list>
#include <set>
#include <vector>
#include <cmath>
#include <cstdio>
#include <ctime>
#include <map>
#include <iomanip>
#include <cmath>
#include <limits>
#include <stack>
#include <algorithm>
#include <climits>
#include <queue>
#include <cstdio>
#include <fstream>
#include <cstring>
#include <string>
#include <sstream>
#include <cassert>
using namespace std;
void main2();
#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define all(x) (x).begin(),(x).end()
#define times(ZZtimes) for(int XYZtimes=0;XYZtimes<ZZtimes;XYZtimes++)
#define MS(ZZtarget,ZZvalue) memset(ZZtarget,ZZvalue,sizeof(ZZtarget))
#define S(SCQW) scanf("%d",&SCQW)
#define SS(SCQW,ZSCQW) scanf("%d%d",&SCQW,&ZSCQW);
#define SSS(SCQW,ZSCQW,ZZSCQW) scanf("%d%d%d",&SCQW,&ZSCQW,&ZZSCQW)
#define SSSS(SCQW,ZSCQW,ZZSCQW,ZZZSCQW) scanf("%d%d%d%d",&SCQW,&ZSCQW,&ZZSCQW,&ZZZSCQW)
#define P(PRQW) printf("%d\n",PRQW)
#define PB push_back
#define MP make_pair
#define eps 1e-8
#define PP(PRQW) printf("%d ",PRQW)
#define ST(qeVECTORXMO) sort(qeVECTORXMO.begin(),qeVECTORXMO.end())
#define ff first
#define ss second
typedef long double ld;
inline ld gett() { return ld(clock()) / CLOCKS_PER_SEC; }
typedef long long ll;
#define MO 1000000007
#define mod 1000000007

int main() {
#ifdef SHERLORE
	freopen("C:\\cygwin64\\home\\orzzzl\\uva\\in", "r", stdin);
	freopen("C:\\cygwin64\\home\\orzzzl\\uva\\out", "w", stdout);
#endif
	int tests = 1;
	scanf("%d", &tests);
	for (int i = 1; i <= tests; i++) {
#ifdef SHERLORE
		printf("Case #%d: ", i);
		ld stime = gett();
#endif
		main2();
#ifdef SHERLORE
		cerr << "running test " << i << endl;
		cerr << "Time: " << gett() - stime << endl;
#endif
	}
}
int N;
vector<pair<string, string> > x;
void main2() {
	x.clear();
	S(N);
	for (int i = 0; i < N; i++) {
		string a, b;
		cin >> a >> b;
		x.push_back(make_pair(a, b));
	}
	set<string> ff, ss;
	int ans = 0;
	
	for (int mask = 0; mask < (1 << N); mask++) {
		ff.clear();
		ss.clear();
		set<pair<string, string> > vis;
		bool ok = true;
		for (int i = 0; i < N; i++) {
			if (mask & (1 << i)) {
				ff.insert(x[i].first);;
				ss.insert(x[i].second);;
				vis.insert(x[i]);
			}
		}
		for (int i = 0; i < N; i++) {
			if (ok == false) break;
			if (!(mask & (1 << i))) {
				if (ff.find(x[i].first) == ff.end()) {
					ok = false;
					break;
				}
				if (ss.find(x[i].second) == ss.end()) {
					ok = false;
					break;
				}
				if (vis.find(x[i]) != vis.end()) {
					ok = false;
					break;
				}
				vis.insert(x[i]);
			}
		}
		if (ok) {
			int cnt = 0;
			for (int i = 0; i < N; i++) {
				if (!(mask & (1 << i))) cnt++;
			}
			ans = max(ans, cnt);
		}
	}
	cout << ans << endl;
}