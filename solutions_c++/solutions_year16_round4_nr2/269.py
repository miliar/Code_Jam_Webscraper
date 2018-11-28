// VSCF.cpp : Defines the entry point for the console application.
//
#include <iomanip>
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
typedef long double LD;
#define int long long



#undef int
int main() {
#define int long long
	int t;
	cin >> t;
	cout << fixed << setprecision(10);
	REP(q, t) {
		int n, k;
		cin >> n >> k;
		vector<LD> inp(n);
		REP(i, n) {
			cin >> inp[i];
		}
		sort(ALL(inp));
		LD score = 0;
		REP(i, k + 1) {
			vector<LD> inp2;
			REP(j, i) {
				inp2.push_back(inp[j]);
			}
			REP(j, k - i) {
				inp2.push_back(inp[n - j - 1]);
			}
			map<int, LD> pstwo;
			pstwo[0] = 1;
			for (LD p : inp2) {
				map<int, LD> pstwo2;
				for (pair<int, LD> x : pstwo) {
					pstwo2[x.first + 1] += x.second * p;
					pstwo2[x.first - 1] += x.second * (1 - p);
				}
				swap(pstwo, pstwo2);
			}
			score = max(score, pstwo[0]);
		}
		cout << "Case #" << q + 1 << ": " << score << "\n";
	}
	return 0;
}

