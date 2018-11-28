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
#define SHERLORE 1
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

vector<int> ans;
int max_val = 0;

int A, B, C, K;
int cntt = 0;
void go(vector<int> &path, map<int, int> &cnt, int ma, int val) {
	cntt++;
	if (cntt > 10000000) return;
	//cerr << val << endl;
	if (val <= ma) return;
	int a = val / 100;
	int c = val % 10;
	int b = val % 100 - c;
	b /= 10;
	int ac = a * 100 + c;
	int ab = a * 100 + b * 10;
	int bc = b * 10 + c;
	if (cnt[ac] >= K || cnt[ab] >= K || cnt[bc] >= K) return;
	path.push_back(val);
	cnt[ac]++;
	cnt[ab]++;
	cnt[bc]++;
	if (path.size() > max_val) {
		max_val = path.size();
		ans = path;
	}
	for (int a = 1; a <= A; a++) {
		for (int b = 1; b <= B; b++) {
			for (int c = 1; c <= C; c++) {
				int v = a * 100 + b * 10 + c;
				if (v > val) go(path, cnt, val, v);
			}
		}
	}
	path.pop_back();
	cnt[ac]--;
	cnt[ab]--;
	cnt[bc]--;
}

void main2() {
	cin >> A >> B >> C >> K;
	cntt = 0;
	ans.clear();
	max_val = 0;
	vector<int> path;
	map<int, int> cnt;
	set<int> vis;
	go(path, cnt, -999, 111);
	cout << max_val << endl;
	for (auto val : ans) {
		int a = val / 100;
		int c = val % 10;
		int b = val % 100 - c;
		b /= 10;
		cout << a << ' ' << b << ' ' << c << endl;
	}
}
