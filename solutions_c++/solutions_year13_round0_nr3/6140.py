#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <stdio.h>
#include <sstream>
#include <string>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <time.h>
#include <cstring>

using namespace std;

#define FOR(i,s,e) for (int i = int(s); i < int(e); i++)
#define FORIT(i,c) for (typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define ISEQ(c) (c).begin(), (c).end()
#define sz(v) (int) v.size()
#define mp make_pair
#define pb push_back
#define all(s) s.begin(), s.end()
#define foreach(i,c) for(__typeof((c).begin()) i = (c).begin() ; i != (c).end() ; i++)

int main() {
	freopen("C-small-attempt1.in", "rt", stdin);
	freopen("out.out", "wt", stdout);
	int T, A, B, count = 1;
	cin >> T;
	while (T--) {
		int res = 0;
		cin >> A >> B;
		FOR(i, A, B+1) {
			if (i == 1 || i == 4 || i == 9 || i == 121 || i == 484)
				res++;
		}
		cout << "Case #" << count++ << ": " << res << endl;
	}
	return 0;
}
