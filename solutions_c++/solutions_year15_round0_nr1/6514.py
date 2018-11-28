#include <set>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <cstdio>
#include <vector>
#include <string>
#include <bitset>
#include <cctype>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <numeric>
#include <complex>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <cassert>
#include <iostream>
#include <iterator>
#include <algorithm>
#include <climits>
using namespace std;

typedef long long ll;
const double EPS = 1e-9;
const int INF = INT_MAX / 4;
typedef vector<int> vint;
typedef pair<int, int> pint;
typedef vector<vector<int> > mat;

#define rep(i, n) REP(i, 0, n)
#define ALL(v) v.begin(), v.end()
#define MSG(a) cout << #a << " " << a << endl;
#define REP(i, x, n) for(int i = x; i < n; i++)
#define pb push_back
#define mp make_pair


int main() {
	// your code goes here
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int smax, ans = 0, cnt = 0;
		cin >> smax;
		string s;
		cin >> s;
		cnt = s[0] - '0';
		for (int i = 1; i <= smax; i++) {
			if (cnt < i) {
				ans += (i - cnt);
				cnt += (i - cnt);
				cnt += (s[i] - '0');
			} else {
				cnt += (s[i] - '0');
			}
		}
		cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}

