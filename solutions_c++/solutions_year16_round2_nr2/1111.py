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
	int tests = 1;
	scanf("%d", &tests);
	for (int i = 1; i <= tests; i++) {
		printf("Case #%d: ", i);
        main2();
	}
}

int ans = INT_MAX;
int n1, n2;

void go(string s1, string s2) {
    //cout << s1 << ' '<< s2 << endl;
    bool ok = false;
    for (int i = 0; i < s1.size(); i++) {
        if (s1[i] == '?') ok = true;
        if (s2[i] == '?') ok = true;
    }
    if (ok == false) {
        int t1 = stoi(s1);
        int t2 = stoi(s2);
        int tt = abs(t1 - t2);
        if (tt < ans) {
            ans = tt;
            n1 = t1;
            n2 = t2;
            return;
        }
        if (tt == ans) {
            if (t1 < n1) {
                n1 = t1;
                n2 = t2;
                return;
            }
            if (t1 == n1 && t2 < n2) {
                n1 = t1;
                n2 = t2;
                return;
            }
        }
        return;
    }
    for (int i = 0; i < s1.size(); i++) {
        if (s1[i] == '?') {
            for (char t = '0'; t <= '9'; t++) {
                s1[i] = t;
                go(s1, s2);
            }
        }
        if (s2[i] == '?') {
            for (char t = '0'; t <= '9'; t++) {
                s2[i] = t;
                go(s1, s2);
            }
        }
    }
}

void main2() {
	string sc, sj;
	cin >> sc >> sj;
   //    cout << sc << sj << endl;
	int len = sc.size();
    ans = INT_MAX;
    go(sc, sj);
    string a1 = to_string(n1), a2 = to_string(n2);
    while (a1.size() < len) a1.insert(a1.begin(), '0');
    while (a2.size() < len) a2.insert(a2.begin(), '0');
	cout << a1 << ' ' << a2 << endl;
}