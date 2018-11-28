// VSCF.cpp : Defines the entry point for the console application.
//
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <iterator>
#include <string>
#include <vector>
#include <set>
#include <deque>
#include <map>

using namespace std;
typedef long long LL;
typedef pair<int, int> PII;
#define MP make_pair
#define FOR(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define REP(i,n) for(int i=0;i<(n);++i)
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second
#define SIZE(x) (int)x.size()
#define ALL(c) c.begin(),c.end()
#define int long long


#undef int
int main() {
#define int long long
	int t;
	
	vector<vector<string>> dyn(13, vector<string>(3));
	vector<string> trans = {
		"PR",
		"RS",
		"PS"
	};
	vector<PII> trans2 = {
		{0, 1},
		{1, 2},
		{0, 2}
	};
	FOR(i, 1, 12) {
		if (i == 1) {
			dyn[i] = trans;
		} else {
			REP(j, 3) {
				int one1 = trans2[j].first ;
				int one2 = trans2[j].second;
				string s1 = dyn[i - 1][one1];
				string s2 = dyn[i - 1][one2];
				if (s1 > s2) {
					swap(s1, s2);
				}
				dyn[i][j] = s1 + s2;
			}
		}
	}
	cin >> t;
	REP(q, t) {
		int n, r, p, s;
		cin >> n >> r >> p >> s;
		vector<string> poss;
		REP(i, 3) {
			string str = dyn[n][i];
			int r1 = 0;
			int p1 = 0;
			int s1 = 0;
			REP(i, str.size()) {
				switch (str[i]) {
				case 'R':
					r1++;
					break;
				case 'S':
					s1++;
					break;
				case 'P':
					p1++;
					break;
				}
				//cerr << r1 << " " << p1 << " " << s1 << " " << str << endl;
			}
			
			if (r1 == r && p1 == p && s1 == s) {
				poss.push_back(str);
			}
		}
		sort(ALL(poss));
		cout << "Case #" << q + 1<<": ";
		if (poss.empty()) {
			cout << "IMPOSSIBLE";
		} else {
			cout << poss[0];
		}
		cout << "\n";
	}
	return 0;
}

