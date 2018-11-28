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
	//pre();
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


void main2() {
	int n;
	S(n);
	vector<int> cnt(n + 5, 0);
	for (int i = 0; i < n; i++) S(cnt[i]);
	bool ini = false;
	while (true) {
		if (ini) cout << ' ';
		ini = true;
		int max_val = -1, c = 1, ind = -1;
		int one = 0;
		int count = 0;
		for (int i = 0; i < n; i++) {
			if (cnt[i] == 1) one = 1;
			if (cnt[i] > 0) count++;
			if (cnt[i] > max_val) {
				c = 1;
				max_val = cnt[i];
				ind = i;
			} else if (cnt[i] == max_val) {
				c++;
			}
		}
		if (count == 0) break;
		if (max_val == 1 && count == 2) {
			for (int i = 0; i < n; i++) {
				if (cnt[i] == 1) {
					cout << (char)('A' + i);
					cnt[i]--;
				}
			}
			continue;
		}
		if (max_val > 1 && count == 2 && one == 1) {
			if (max_val % 2 == 1) {
				cnt[ind] -= 2;
				cout << (char)('A' + ind) << (char)('A' + ind);
			}
			else {
				cnt[ind] -= 1;
				cout << (char)('A' + ind);
			}
			continue;
		}
		if (c >= 2) {
			if (c % 2 == 1) c = 1;
			else c = 2;
			for (int i = 0; i < n; i++) {
				if (cnt[i] == max_val) {
					cnt[i]--;
					cout << (char)('A' + i);
					c--;
					if (c == 0) {
						break;
					}
				}
			}
			continue;
		}
		cnt[ind] --;
		cout << (char)('A' + ind);
	}
	cout << endl;
}
