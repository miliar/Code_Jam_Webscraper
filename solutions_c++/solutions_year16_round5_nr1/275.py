// VSCF.cpp : Defines the entry point for the console application.
//
#include <list>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <iterator>
#include <string>
#include <vector>
#include <set>
#include <deque>
#include <map>
#include <iomanip>

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
	ios_base::sync_with_stdio(0);
	int t;
	cin >> t;
	REP(q, t) {
		string str;
		cin >> str;
		int n = str.size();
		int s = 0;
		int j = 0;
		int result = 0;
		list<char> inp;
		REP(i, n) {
			if (inp.empty()) {
				inp.push_back(str[i]);
				continue;
			}
			if (inp.back() == str[i]) {
				result += 10;
				inp.pop_back();
			} else {
				inp.push_back(str[i]);
			}
		}
		result += inp.size() / 2 * 5;
		cout << "Case #" << q + 1 << ": " << result << "\n";
	}
	return 0;
}

