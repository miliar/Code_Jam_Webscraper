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


void main2() {
	string s;
	cin >> s;
	map<char, int> cnt;
	for (auto ele : s) {
		cnt[ele]++;
	}
	vector<int> ans(10, 0);
	ans[0] = cnt['Z'];
	string z = "ZERO";
	for (auto ele : z) cnt[ele] -= ans[0];
	ans[2] = cnt['W'];
	z = "TWO";
	for (auto ele : z) cnt[ele] -= ans[2];
	ans[4] = cnt['U'];
	z = "FOUR";
	for (auto ele : z) cnt[ele] -= ans[4];
	ans[6] = cnt['X'];
	z = "SIX";
	for (auto ele : z) cnt[ele] -= ans[6];
	ans[8] = cnt['G'];
	z = "EIGHT";
	for (auto ele : z) cnt[ele] -= ans[8];
	ans[1] = cnt['O'];
	z = "ONE";
	for (auto ele : z) cnt[ele] -= ans[1];
	ans[7] = cnt['S'];
	z = "SEVEN";
	for (auto ele : z) cnt[ele] -= ans[7];
	ans[3] = cnt['R'];
	z = "THREE";
	for (auto ele : z) cnt[ele] -= ans[3];
	ans[5] = cnt['F'];
	z = "FIVE";
	for (auto ele : z) cnt[ele] -= ans[5];
	ans[9] = cnt['I'];
	for (int i = 0; i <= 9; i++) {
		for (int j = 0; j < ans[i]; j++) {
			cout << i;
		}
	}
	cout << endl;
}