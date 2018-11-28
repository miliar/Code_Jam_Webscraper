#include <functional>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <numeric>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <string>
#include <vector>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <list>
#include <set>
#include <map>
#include <complex>
using namespace std;

#define FOR(i, a, b) for(int i = a, __up = b; i < __up; ++i)
#define REP(n) FOR(i, 0, n)
#define CLR(a) memset(a, 0, sizeof a)

typedef complex<double> point;
typedef long long ll;

// S E N W
int dx[]={1,0,-1,0};
int dy[]={0,1,0,-1};

void solve() {
	int r;
	vector<int> v[2], inter;
	int t;
	REP(2) {
		cin >> r;
		--r;
		FOR(j, 0, 4) {
			FOR(k, 0, 4) {
				cin >> t;
				if (j == r) {
					v[i].push_back(t);
				}
			}
		}
		sort(v[i].begin(), v[i].end());
	}

	set_intersection(v[0].begin(), v[0].end(),
                    v[1].begin(), v[1].end(),
					back_inserter(inter));
	switch (inter.size()) {
	case 0:
		cout << "Volunteer cheated!";
		break;
	case 1:
		cout << inter[0];
		break;
	default:
		cout << "Bad magician!";
	}
	puts("");
}
int main()
{
	int T;
	cin >> T;
	REP(T) {
		printf("Case #%d: ", i+1);
		solve();
	}

	return 0;
}
