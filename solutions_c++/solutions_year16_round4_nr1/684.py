/*  */
#include <iostream>
#include <sstream>
#include <string>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <deque>
#include <bitset>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cstring>
#include <climits>
#include <cctype>
#include <cassert>
#include <functional>
#include <iterator>
#include <iomanip>
using namespace std;
//#pragma comment(linker,"/STACK:102400000,1024000")

#define sti				set<int>
#define stpii			set<pair<int, int> >
#define mpii			map<int,int>
#define vi				vector<int>
#define pii				pair<int,int>
#define vpii			vector<pair<int,int> >
#define rep(i, a, n) 	for (int i=a;i<n;++i)
#define per(i, a, n) 	for (int i=n-1;i>=a;--i)
#define clr				clear
#define pb 				push_back
#define mp 				make_pair
#define fir				first
#define sec				second
#define all(x) 			(x).begin(),(x).end()
#define SZ(x) 			((int)(x).size())
#define lson			l, mid, rt<<1
#define rson			mid+1, r, rt<<1|1

#define PR 1
#define RS 2
#define SP 3

typedef vector<string> vstr;
int n, r, p, s;
vstr ans[13];
map<pii,int> tb[13];
map<pii,int>::iterator iter;

void init() {
	vstr& vtmp = ans[1];
	
	vtmp.pb("PR");
	vtmp.pb("RS");
	vtmp.pb("PS");
	tb[1][mp(1, 1)] = 0;
	tb[1][mp(0, 1)] = 1;
	tb[1][mp(1, 0)] = 2;
	
	rep(i, 1, 12) {
		vstr& nvc = ans[i+1];
		map<pii,int>& ntb = tb[i+1];
		const vstr& vc = ans[i];
		const int sz = SZ(vc);
		rep(j, 0, sz) {
			const string& s = vc[j];
			const int len = s.length();
			string tmp = "";
			int p = 0, r = 0;
			for (int i=0; i<len; i+=2) {
				if (s[i] == 'P') {
					if (s[i+1] == 'R') {
						tmp += "PRRS";
						p += 1;
						r += 2;
					} else {
						tmp += "PRPS";
						p += 2;
						r += 1;
					}
				} else if (s[i] == 'R') {
					if (s[i+1] == 'S') {
						tmp += "PSRS";
						++p;
						++r;
					} else {
						tmp += "PRRS";
						p += 1;
						r += 2;
					}
				} else {
					if (s[i+1] == 'R') {
						tmp += "PSRS";
						++p;
						++r;
					} else {
						tmp += "PRPS";
						p += 2;
						r += 1;
					}
				}
			}
			// #ifndef ONLINE_JUDGE
			// printf("tmp = %s\n", tmp.c_str());
			// #endif
			pii pi = pii(p, r);
			iter = ntb.find(pi);
			if (iter == ntb.end()) {
				ntb[pi] = SZ(nvc);
				nvc.pb(tmp);
			} else {
				// printf("123\n");
				if (tmp < nvc[iter->sec]) {
					nvc[iter->sec] = tmp;
				}
			}
		}
	}
}

void solve() {
	vstr& cvc = ans[n];
	map<pii,int>& ctb = tb[n];
	pii pi = mp(p, r);
	iter = ctb.find(pi);
	
	if (iter == ctb.end()) {
		puts("IMPOSSIBLE");
		return ;
	}
	
	printf("%s\n", cvc[iter->sec].c_str());
}

int main() {
	ios::sync_with_stdio(false);
	#ifndef ONLINE_JUDGE
		freopen("data.in", "r", stdin);
		freopen("data.out", "w", stdout);
	#endif
	
	int t;
	
	init();
	scanf("%d", &t);
	rep(tt, 1, t+1) {
		scanf("%d%d%d%d", &n,&r,&p,&s);
		printf("Case #%d: ", tt);
		solve();
	}
	
	// #ifndef ONLINE_JUDGE
		// printf("time = %ldms.\n", clock());
	// #endif
	
	return 0;
}
